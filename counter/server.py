from xml.etree.ElementInclude import include
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "counter"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.pop('count')
    return redirect('/')

@app.route('/addTwo')
def addTwo():
    session['count'] += 2
    return render_template('index.html')

# @app.route('/addMore')
# def addMore():
#     print(request.form)
#     # if 'increments' not in session:
#     #     session['increments'] = 
#     # else:
#     #     session.pop('increments')
#     # session['count'] += increments
#     return redirect('/')









if __name__=="__main__":   
    app.run(debug=True)    