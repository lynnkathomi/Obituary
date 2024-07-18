from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from slugify import slugify
from datetime import datetime

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'obituary_platform',
}

# Route for displaying the obituary submission form
@app.route('/')
def obituary_form():
    return render_template('obituary_form.html')

# Route for handling form submission
@app.route('/submit_obituary', methods=['POST'])
def submit_obituary():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    date_of_death = request.form['date_of_death']
    content = request.form['content']
    author = request.form['author']
    submission_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    slug = slugify(name + '-' + submission_date)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author, submission_date, slug)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (name, date_of_birth, date_of_death, content, author, submission_date, slug))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('view_obituaries'))

# Route for displaying the list of obituaries
@app.route('/view_obituaries')
def view_obituaries():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM obituaries')
    obituaries = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('view_obituaries.html', obituaries=obituaries)

if __name__ == '__main__':
    app.run(debug=True)
