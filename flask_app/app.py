#import a library
from flask import Flask,render_template, request
import joblib

#instance of an app
app = Flask(__name__)

#Load the model 
model = joblib.load("diabetic_79.pkl")

@app.route('/')
def hello():
    return render_template('landing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/data', methods = ["POST"])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
   
    if output[0] == 0:
        output = "Not Diabetic"
    else:
        output = "Diabetic"

    return render_template("result.html", result = output)



if __name__ == '__main__':
    app.run(debug = True)