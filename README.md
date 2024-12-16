# Centurion-Prepaid-Card-Dashboaord

Project Overview

The Centurion Prepaid Card Dashboard is a web-based application developed for managing and processing payments for various services within Centurion University. These services include library fees, coffee shop payments, mess fees, bus fees, tuition, and peer-to-peer student transfers. This project uses Python, Dash, SQL, HTML, and CSS, with Excel files serving as the data storage solution.

Features

Excel Integration: All data is stored and managed using Excel files.
Interactive Interface: Developed using Dash to provide a user-friendly interface.

Tech Stack

Python: Used for the backend logic and functionality.
Dash: A Python framework for building web applications.
HTML/CSS: Used to design the frontend of the dashboard for a clean and responsive user experience.
Excel: Used for data storage instead of MySQL, allowing data to be manipulated in a tabular format.

Setup Instructions

Clone the repository:

git clone https://github.com/abhiramsakaray/Centurion-Prepaid-Card-Dashboaord.git

Install the required libraries: Ensure you have Python installed. 

Then install necessary libraries:

pip install dash pandas openpyxl

Running the Dashboard: To start the dashboard, run the following command:

python app.py
This will start a local development server that you can access via your browser at http://127.0.0.1:8050.

Data Handling: The project relies on Excel files to manage data. Ensure that the correct Excel files (e.g., users.xlsx, transactions.xlsx) are available in the project directory.

Project Structure

/Centurion_Prepaid_Card_Dashboard
│
├── app.py               # Main Python file for the Dash app
├── assets/              # Folder containing static files like images, CSS
├── data/                # Folder containing Excel files for data storage
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation

Author Information
Name: Abhiram Sakaray
ERP No: 241801390012
Email: 241801390012@cutmap.ac.in
Course: First Semester DAVP (Python) Project
This project serves as part of the Python programming course, designed to enhance practical experience with data handling, web development, and dashboard creation.

