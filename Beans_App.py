import streamlit as st
import pandas as pd
import joblib
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
from dateutil.relativedelta import relativedelta

# Load your trained SARIMA model
model_fit_full = joblib.load('sarima_beans_model3.pkl')

# Assuming you have a CSV with the latest data, including the 'standardized_price' column
latest_data = pd.read_csv('beans_wholesale_prices.csv')
latest_data['date'] = pd.to_datetime(latest_data['date'])
latest_data.set_index('date', inplace=True)
latest_data.sort_index(inplace=True)

st.title('Bean Price Prediction App')

def predict_price(model_fit, steps, initial_value):
    # Forecast future prices
    forecast = model_fit.get_forecast(steps=steps)
    forecast_mean = forecast.predicted_mean
    
    # Undo the differencing
    forecast_prices = initial_value + forecast_mean.cumsum()
    return forecast_prices.iloc[-1]

def main():
    # User inputs
    commodity = st.selectbox('Select Commodity', ['Beans'])
    prediction_month = st.selectbox('Prediction Month', range(1, 13))
    prediction_year = st.selectbox('Prediction Year', range(2021, 2030))

    if st.button('Predict Price'):
        # Get the last known price and its date
        last_known_price = latest_data['standardized_price'].iloc[-1]
        last_known_date = latest_data.index[-1]

        # Calculate the number of steps to forecast
        target_date = pd.Timestamp(year=prediction_year, month=prediction_month, day=1)
        steps = (target_date.year - last_known_date.year) * 12 + target_date.month - last_known_date.month
        
        # Make sure we are predicting for a future date
        if steps <= 0:
            st.error('Please select a future date for prediction.')
            return
        
        # Call the prediction function
        predicted_price = predict_price(model_fit_full, steps, last_known_price)
        st.write(f"The predicted average price for {commodity} in {prediction_month}/{prediction_year} is: KES {predicted_price:.2f} per KG")

if __name__ == '__main__':
    main()