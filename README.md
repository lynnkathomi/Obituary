# Obituary Platform

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Setup](#setup)
6. [Database Creation](#database-creation)
7. [Development Process](#development-process)
8. [Usage](#usage)
9. [Database Management](#database-management)
10. [Customization](#customization)
11. [Troubleshooting](#troubleshooting)
12. [Contributing](#contributing)

## Introduction

The Obituary Platform is a Flask-based web application for managing and sharing obituaries. Users can submit new obituaries through a web form and view a list of all submitted obituaries. The application also includes features for sharing obituaries on social media platforms like Facebook and Twitter.

## Features

- Submit new obituaries through a web form.
- View a list of submitted obituaries.
- Share obituaries on Facebook and Twitter.

## Project Structure

OM/
├── venv/ # Virtual environment for the project
├── app.py # Main application file
├── static/
│ ├── style.css # CSS file for styling
│ └── script.js # JavaScript file for user functionality
└── templates/
├── obituary_form.html # HTML template for obituary submission form
├── view_obituaries.html# HTML template for viewing submitted obituaries
└── other_templates.html# Other HTML templates (if any)



## Prerequisites

- Python 3.8+
- Flask
- python-slugify
- pip (Python package manager)
- virtualenv (recommended but optional)

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/obituary-management.git
   cd obituary-management
Create a virtual environment and activate it:

sh
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
Install the required dependencies:

git bash

pip install -r requirements.txt
(Create the requirements.txt file if it does not exist using pip freeze > requirements.txt.)

Run the application:

git bash

python app.py
Open your browser and navigate to http://127.0.0.1:5000 to access the application.

Database Creation
Test Area: Create a Database to Store Obituary Data
Steps:
Open your database management tool.
Create a new database named obituary_platform.
Create a table named obituaries with the following columns:
id (INT, Primary Key, Auto Increment)
name (VARCHAR(100))
date_of_birth (DATE)
date_of_death (DATE)
content (TEXT)
author (VARCHAR(100))
submission_date (DATETIME, default to current timestamp)
slug (VARCHAR(255), Unique)
Development Process
Set up the Flask project structure.
Design and implement the database model for obituaries.
Create views for submitting and viewing obituaries.
Develop templates for the user interface.
Implement pagination for efficient browsing.

Optimize for SEO.
Implement responsive design for various screen sizes.
Usage
To submit a new obituary, navigate to the home page and fill out the form.
To view the list of submitted obituaries, navigate to the "View Obituaries" page.
To share an obituary, use the provided links for Facebook and Twitter.
Database Management
Viewing or Modifying the Database
To interact with the database directly, follow these steps:


Customization
Modify the CSS in static/style.css to change the appearance.
Update templates in templates/ to alter the HTML structure.
Adjust the model in models.py for different obituary fields.
Troubleshooting
If you encounter database permission issues, ensure your PostgreSQL user has the correct privileges.
For static file issues, run python manage.py collectstatic.
Clear your browser cache if you don't see CSS changes.
Contributing
Feel free to fork this repository and make your own changes. Pull requests are welcome!
