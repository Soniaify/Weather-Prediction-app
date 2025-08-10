from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

model = joblib.load('temp_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        humidity = float(request.form.get("humidity"))
        pressure = float(request.form.get("pressure"))
        windspeed = float(request.form.get("windspeed"))
        rainfall = float(request.form.get("rainfall"))
        sunlight = float(request.form.get("sunlight"))
        
        test_data = np.array([humidity, pressure, windspeed, rainfall, sunlight]).reshape(-1,5)
        prediction = model.predict(test_data)
        return jsonify({'prediction': round(float(prediction[0]), 2)})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)