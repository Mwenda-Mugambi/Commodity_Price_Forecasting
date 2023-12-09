import streamlit as st
import pandas as pd
from pmdarima import auto_arima
import matplotlib.pyplot as plt
from datetime import datetime

# Assuming df_nairobi is provided and properly formatted
# df_nairobi should be a DataFrame with 'pricetype', 'district', 'commodity', 'date', and 'standardized_price' columns
df_nairobi = pd.read_csv("nairobi_df.csv")


# Create the nested dictionary from the df_nairobi DataFrame
nairobi_dict = {}
for pricetype_name in df_nairobi['pricetype'].unique():
    nairobi_dict[pricetype_name] = {}
    df_pricetype = df_nairobi[df_nairobi['pricetype'] == pricetype_name]

    for region_name in df_pricetype['district'].unique():
        nairobi_dict[pricetype_name][region_name] = {}
        df_region = df_pricetype[df_pricetype['district'] == region_name]

        for item_name in df_region['commodity'].unique():
            nairobi_dict[pricetype_name][region_name][item_name] = df_region[df_region['commodity'] == item_name]

# Function to perform ARIMA forecasting
def arima_model(ref, date_input):
    ref['date'] = pd.to_datetime(ref['date'])
    date_r = pd.to_datetime(date_input)
    n = (date_r - ref['date'].iloc[-1]).days  # Access the last date in 'ref'
    
    st.write("Model in Progress...")
    
    df = pd.DataFrame({
        'date': ref['date'],
        'value': ref['standardized_price']
    })

    # auto_arima model
    model = auto_arima(df['value'], trace=False, suppress_warnings=True, seasonal=False)
    
    # fitted model
    n_periods = int(n)
    forecast, conf_int = model.predict(n_periods=n_periods, return_conf_int=True)
    forecast_start_date = df['date'].iloc[-1] + pd.DateOffset(1)
    forecast_dates = pd.date_range(forecast_start_date, periods=n_periods, freq='D')

    # DataFrame for the forecast
    forecast_df = pd.DataFrame({
        'date': forecast_dates,
        'forecast': forecast,
        'lower_bound': conf_int[:, 0],
        'upper_bound': conf_int[:, 1]
    })

    # Plotting the original series and forecasted values
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['value'], label='Original Series')
    plt.plot(forecast_dates, forecast, label='Forecast', color='red')
    plt.fill_between(forecast_dates, conf_int[:, 0], conf_int[:, 1], color='red', alpha=0.3)
    plt.title(f'ARIMA price Forecast for {ref["commodity"].iloc[0]}')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    st.pyplot(plt)

    # Get the predicted price
    p_price = forecast_df[forecast_df["date"] == date_r]["forecast"].values[0]
    return p_price, forecast_df

# Streamlit UI
def main():
    st.title('Commodity Price Prediction with ARIMA')

    # Selection of price type, district, and commodity based on the nested dictionary
    pricetype_selected = st.selectbox('Select Price Type', options=list(nairobi_dict.keys()))
    district_selected = st.selectbox('Select District', options=list(nairobi_dict[pricetype_selected].keys()))
    commodity_selected = st.selectbox('Select Commodity', options=list(nairobi_dict[pricetype_selected][district_selected].keys()))
    
    # User Inputs
    date_input = st.date_input('Enter desired date for prediction (YYYY-MM-DD):', min_value=datetime.today())
    
    if st.button('Predict Price'):
        # Retrieve the reference dataframe for the selected commodity
        ref = nairobi_dict[pricetype_selected][district_selected][commodity_selected]
        predicted_price, forecast_df = arima_model(ref, date_input)
        st.write(f'The price forecast for {commodity_selected} on {date_input.strftime("%Y-%m-%d")} is estimated to be KES {predicted_price}')

if __name__ == "__main__":
    main()
