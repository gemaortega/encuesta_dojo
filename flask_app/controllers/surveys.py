from flask import render_template, redirect, request, session
from flask_app import app
from flask import Flask

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/process', methods=["POST"])
def checkout():
    print(request.form)

    session['name'] = request.form ['name']
    session['city'] = request.form ['city']
    session['language'] = request.form ['language']
    session['comment'] = request.form ['comment']
    
    return redirect('/results')

@app.route('/results')
def data():
    print(session)
    return render_template( 'results.html', name=session['name'], city=session['city'], language=session['language'], comments=session['comment'])

