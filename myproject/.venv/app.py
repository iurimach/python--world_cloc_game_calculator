from flask import Flask, render_template
from datetime import datetime, timedelta


# from flask_wtf import FlaskForm
# from wtforms import StringField, FormField, FieldList, IntegerField, Form
# from wtforms.validators import Optional
# from collections import namedtuple

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    # Fetching 10 dummy items for demonstration purposes
    items = [
        {'name': 'Laptop', 'image': 'laptop.jpg'},
        {'name': 'Mobile', 'image': 'mobile.jpg'},
        # Add more items as needed
    ]
    return render_template('gallery.html', items=items)

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/about')
def about():
    # Information about you
    about_me_info = {
        'address': 'New York',
        'phone': 'xxxx',
        'email': 'your_email@example.com',
        # Add more information as needed
    }
    return render_template('about.html', about_me_info=about_me_info)

if __name__ == '__main__':
    app.run(debug=True)
