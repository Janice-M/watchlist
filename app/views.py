from flask import render_template
from app import app

#views
@app.route('/')
def index ():
    """ this is a view root page that returns the index page and its data """
    
    message = 'Flask is running bois - Grey'
    return render_template('index.html', message= message)