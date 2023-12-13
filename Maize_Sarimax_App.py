import streamlit as st
import pandas as pd
import joblib
from dateutil.relativedelta import relativedelta

# Load your trained SARIMA model
model = joblib.load('sarimax_model_monthly.pkl')

st.title('Wholesale Maize Price Forecast App')

def main():
    # User inputs
    st.header('Select Month and Year for Prediction')
    selected_month = st.selectbox('Month', range(1, 13))
    selected_year = st.selectbox('Year', range(2021, 2031))  # Change range as needed

    if st.button('Predict Price'):
        # Construct the target date for prediction (end of the selected month)
        target_date = pd.Timestamp(year=selected_year, month=selected_month, day=1)
        target_date = target_date + relativedelta(months=1) - relativedelta(days=1)

        # Generate forecast
        try:
            # Make the forecast for the next months including the target month
            steps_to_forecast = (target_date.year - 2020) * 12 + target_date.month  # Assuming the training data goes up to December 2020
            forecast_future = model.get_forecast(steps=steps_to_forecast)
            forecast_mean = forecast_future.predicted_mean
            forecast_price = forecast_mean[-1]  # Retrieve the forecasted price for the target month

            st.success(f'The forecasted average price for Maize in {target_date.strftime("%B %Y")} is: {forecast_price:.2f}')
        except Exception as e:
            st.error(f'An error occurred: {e}')

# Run the app
if __name__ == '__main__':
    main()