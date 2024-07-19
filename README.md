Obituary Platform
Table of Contents
Introduction
Features
Project Structure
Prerequisites
Setup
Database Creation
Development Process
Usage
Database Management
Customization
Troubleshooting
Contributing
Introduction
The Obituary Platform is a Flask-based web application for managing and sharing obituaries. Users can submit new obituaries through a web form and view a list of all submitted obituaries. The application also includes features for sharing obituaries on social media platforms like Facebook and Twitter.

Features
Submit new obituaries through a web form.
View a list of submitted obituaries.
Share obituaries on Facebook and Twitter.
Project Structure
graphql
Copy code
OM/
├── venv/                 # Virtual environment for the project
├── app.py                # Main application file
├── static/
│   ├── style.css         # CSS file for styling
│   └── script.js         # JavaScript file for user functionality
└── templates/
    ├── obituary_form.html # HTML template for obituary submission form
    ├── view_obituaries.html # HTML template for viewing submitted obituaries
    └── other_templates.html # Other HTML templates (if any)
Prerequisites
Python 3.8+
Flask
python-slugify
pip (Python package manager)
virtualenv (recommended but optional)
Setup
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/obituary-management.git
cd obituary-management
Create a virtual environment and activate it:

sh
Copy code
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
(Create the requirements.txt file if it does not exist using pip freeze > requirements.txt.)

Run the application:

sh
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000 to access the application.

Database Creation
Create a database to store obituary data:

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
Submit a new obituary: Navigate to the home page and fill out the form.
View the list of submitted obituaries: Navigate to the "View Obituaries" page.
Share an obituary: Use the provided links for Facebook and Twitter.
Database Management
Viewing or Modifying the Database:
Interact with the database directly using your database management tool.
Customization
Modify the CSS in static/style.css to change the appearance.
Update templates in templates/ to alter the HTML structure.
Adjust the model in models.py for different obituary fields.
Troubleshooting
Database permission issues: Ensure your PostgreSQL user has the correct privileges.
Static file issues: Run python manage.py collectstatic.
CSS changes not visible: Clear your browser cache.
Contributing
Feel free to fork this repository and make your own changes. Pull requests are welcome!
