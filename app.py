# Importing essential libraries
from flask import Flask, render_template, request
import joblib,pickle
import numpy as np

app = Flask(__name__)
# Load the regression model
classifier = joblib.load('car_msp.ml')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    name = (request.form['name'])
    year = (request.form['year'])
    km_driven = (request.form['km_driven'])
    fuel = (request.form['fuel'])
    seller_type = (request.form['seller_type'])
    transmission = (request.form['transmission'])
    owner = (request.form['owner'])
    mileage = float(request.form['mileage'])
    max_power = (request.form['max_power'])
    seats = (request.form['seats'])

    data = [[name, year, km_driven, fuel, seller_type, transmission,owner, mileage, max_power, seats]]

    if (name == 0 and year ==0 and km_driven == 0):
        my_prediction = [0]
    else:
        my_prediction = classifier.predict(data)

    return render_template('index.html', prediction_text='The Maximum Selling Price of the Car will be $ {}'.format(round(my_prediction[0],2)))



if __name__ == "__main__":
    app.run(debug=True)