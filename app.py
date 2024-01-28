from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        car_name = request.form.get('Name')
        age_of_the_car = request.form['age_of_the_car']
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type = request.form['Fuel_Type']
        Transmission = request.form['Transmission']

        prediction = model.predict([[Present_Price, Kms_Driven, Fuel_Type, Transmission, age_of_the_car]])
        output = round(prediction[0], 2)
        prediction_text = 'Resale Value of your ' + car_name + ' is Rs. ' + str(output) + ' Lakhs.'
        return render_template('index.html', prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(debug=True)
