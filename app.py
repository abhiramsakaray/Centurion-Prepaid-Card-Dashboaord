import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server, url_base_pathname='/')

students_df = pd.read_excel("database/students_data.xlsx")
transactions_df = pd.read_excel("database/transactions_data.xlsx")

app.layout = html.Div([
    html.Div(
        id="sidebar",
        children=[
            html.Img(
                src='assets/logo.png',
                alt="Logo",
                className="sidebar-logo"
            ),
            html.Ul(
                children=[
                    html.Li(
                        html.A("Home", href="/", className="sidebar-item"),
                        className="sidebar-item"
                    ),
                    html.Li(
                        html.A("Transactions", href="/transactions", className="sidebar-item"),
                        className="sidebar-item"
                    ),
                    html.Li(
                        html.A("Reports", href="/reports", className="sidebar-item"),
                        className="sidebar-item"
                    ),
                ],
                className="sidebar-list"
            )
        ]
    ),
    # Main content
    html.Div(
        id="main-content",
        children=[
            html.H1("Centurion University Prepaid Card Dashboard", className="main-title"),
            html.Label("Select Student Card", className="dropdown-label"),
            dcc.Dropdown(
                id='student-dropdown',
                options=[
                    {'label': row['student_erp'], 'value': row['card_number']} for index, row in students_df.iterrows()
                ],
                value=students_df['card_number'].iloc[0],
                style={'width': '50%', 'margin-bottom': '20px'}
            ),
            html.Div(
                id="card-container",
                children=[
                    html.Img(
                        src='/assets/card.png',
                        className="card-image",
                    ),
                    html.Div(
                        className="card-text-container",
                        children=[
                            html.Div(id="card-number", className="card-number-text"),
                            html.Div(id="card-expiry", className="card-expiry-text") 
                        ]
                    )
                ]
            ),
            dcc.Graph(id='transaction-graph'),
            dcc.Graph(id='transaction-pie-chart'),
            dcc.Graph(id='transaction-line-chart')
        ]
    )
])

@app.callback(
    [Output('transaction-graph', 'figure'),
     Output('transaction-pie-chart', 'figure'),
     Output('transaction-line-chart', 'figure'),
     Output('card-number', 'children'),
     Output('card-expiry', 'children')],
    [Input('student-dropdown', 'value')]
)
def update_graph_and_card(selected_card_number):
    filtered_df = transactions_df[transactions_df['card_number'] == selected_card_number]

    bar_figure = {
        'data': [
            {'x': filtered_df['transaction_date'], 'y': filtered_df['amount'], 'type': 'bar', 'name': 'Transactions'}
        ],
        'layout': {'title': f'Transaction Overview for Card: {selected_card_number}'}
    }

    spending_by_type = filtered_df.groupby('transaction_type')['amount'].sum().reset_index()
    pie_figure = {
        'data': [
            go.Pie(
                labels=spending_by_type['transaction_type'],
                values=spending_by_type['amount'],
                hoverinfo='label+percent',
                textinfo='label+value'
            )
        ],
        'layout': {'title': f'Spending Breakdown for Card: {selected_card_number}'}
    }

    filtered_df['transaction_date'] = pd.to_datetime(filtered_df['transaction_date'])
    daily_spending = filtered_df.groupby(filtered_df['transaction_date'].dt.date)['amount'].sum().reset_index()
    line_figure = {
        'data': [
            go.Scatter(
                x=daily_spending['transaction_date'],
                y=daily_spending['amount'],
                mode='lines+markers',
                name='Daily Spending'
            )
        ],
        'layout': {
            'title': f'Daily Spending Trend for Card: {selected_card_number}',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Total Amount'}
        }
    }

    card_number_text = f"{selected_card_number}"
    expiry_date_text = "2028"

    return bar_figure, pie_figure, line_figure, card_number_text, expiry_date_text

if __name__ == "__main__":
    app.run_server(debug=True)