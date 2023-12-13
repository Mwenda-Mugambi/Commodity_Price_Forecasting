import streamlit as st
import pandas as pd
from datetime import datetime
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
import pmdarima as pm
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import joblib

# Load your trained SARIMA models
models = {
    'Maize': joblib.load('sarima_model_fit2.pkl'),
#     'Potatoes': joblib.load('sarima_potatoes_model.pkl'),
#     'Beans': joblib.load('sarima_beans_model.pkl'),
#     'Sorghum': joblib.load('sarima_sorghum_model.pkl')
 }

# Load your historical data
historical_data = pd.read_csv('nairobi_df.csv')
historical_data['date'] = pd.to_datetime(historical_data['date'])

st.title('Commodity Price Forecast App')

def main():
    # User inputs
    selected_commodity = st.selectbox('Select Commodity', ['Maize', 'Potatoes', 'Beans', 'Sorghum'])
    selected_pricetype = st.selectbox('Select Price Type', ['Wholesale', 'Retail'])
    selected_date = st.date_input('Select expected date')

    # Function to calculate n_periods
    def calculate_periods(selected_date, latest_date):
        selected_date = pd.to_datetime(selected_date)
        delta = selected_date - latest_date
        return delta.days // 30  # Rough approximation of months

    if st.button('Predict Price'):
        # Ensure the price type is Wholesale
        if selected_pricetype == 'Wholesale':
            # Calculate the number of periods to forecast
            latest_date = historical_data['date'].max()
            n_periods = calculate_periods(selected_date, latest_date)

            if n_periods > 0:
                # Get the appropriate model
                model = models[selected_commodity]
                
                # Generate forecast
                try:
                    forecast_future = model.get_forecast(steps=n_periods)
                    forecast_mean = forecast_future.predicted_mean
                    forecast_price = forecast_mean.iloc[-1]  # Safe retrieval of the last forecast
                    st.write(f'The forecasted price for {selected_commodity} on {selected_date} is: {forecast_price:.2f}')
                except Exception as e:
                    st.error(f'An error occurred: {e}')
            else:
                st.error('Selected date is before the latest available data.')
        else:
            st.error('Currently, the model only supports forecasting for Wholesale prices.')

# Run the app
if __name__ == '__main__':
    main()