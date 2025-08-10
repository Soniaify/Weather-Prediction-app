# Weather Prediction App

A simple **Flask-based web application** that predicts **temperature** using a trained Machine Learning model.  
The model takes **humidity, pressure, windspeed, rainfall, and sunlight** as inputs and outputs the predicted temperature.

---

## Features
- User-friendly web interface.
- Accepts weather parameter inputs from users.
- Uses a trained ML model (`temp_model.pkl`) to predict temperature.
- REST API support for programmatic predictions.
- Built with **Flask**, **NumPy**, and **Joblib**.

---

## Project Structure
Weather_Prediction/
│── app.py                 
│── temp_model.pkl         
│── templates/
│   └── index.html         
│── linear_regressions.ipynb  
└── weather_500.csv            
