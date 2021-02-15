"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import date

###
# Routing for your application.
###

@app.route('/profile')
def profile():
    "This shows the profile"
    date_joined = date(2021, 2, 8)
    return render_template('profile.html',date=format_date_joined(date_joined))


@app.route('/')
def home():
    """Render website's home page."""
@@ -24,6 +32,9 @@ def about():
    """Render the website's about page."""
    return render_template('about.html', name="Javier Stewart")

def format_date_joined(date):
    return "Joined "  + date.strftime("%B, %Y")


###
# The functions below should be applicable to all Flask apps.
@@ -54,5 +65,9 @@ def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")