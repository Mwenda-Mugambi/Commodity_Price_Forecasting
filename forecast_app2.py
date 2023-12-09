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
    # progress_placeholder = st.empty()
    # progress_placeholder.text("Model in Progress...")
    
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

    # # Plotting the original series and forecasted values
    # plt.figure(figsize=(10, 6))
    # plt.plot(df['date'], df['value'], label='Original Series')
    # plt.plot(forecast_dates, forecast, label='Forecast', color='red')
    # plt.fill_between(forecast_dates, conf_int[:, 0], conf_int[:, 1], color='red', alpha=0.3)
    # plt.title(f'ARIMA price Forecast for {ref["commodity"].iloc[0]}')
    # plt.xlabel('Date')
    # plt.ylabel('Value')
    # plt.legend()
    # st.pyplot(plt)

    # Get the predicted price
    p_price = forecast_df[forecast_df["date"] == date_r]["forecast"].values[0]
    return p_price, forecast_df

# Streamlit UI
def main():
    # Custom CSS styles
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .header {
        color: #ff6347;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007bff;  /* Blue color */
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        margin: 10px 0;
    }
    div.stButton > button:hover {
        background-color: #0056b3;  /* Darker blue color on hover */
    }
    </style>
    """, unsafe_allow_html=True)

    # Define commodities and their units
    commodities_per_kg = ['Wheat', 'Sorghum', 'Maize', 'Potatoes', 'Beans', ]
    commodities_per_liter = ['Oil (vegetable)', 'Milk']


    st.title('ARIMA Modeling')


    # Image banner
    banner_image_path = 'Design_Assets/Header_image.jpg'  
    st.image(banner_image_path, use_column_width=True)

    st.markdown('We aim to launch a comprehensive project to analyze and predict ' 
                'the dynamics of food commodity prices in Nairobi, Kenya. The project '
                 'utilizes time series analysis to understand trends, fluctuations,' 
                 ' and seasonality in prices across various markets.', unsafe_allow_html=True)

    # Input selection in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        pricetype_selected = st.selectbox("**Select Price Type**", options=list(nairobi_dict.keys()))
    with col2:
        district_selected = st.selectbox('**Select District**', options=list(nairobi_dict[pricetype_selected].keys()))
    with col3:
        commodity_selected = st.selectbox('**Select Commodity**', options=list(nairobi_dict[pricetype_selected][district_selected].keys()))
    
    date_input = st.date_input('**Enter desired date for prediction:**', min_value=datetime.today())
    
    if st.button('Predict Price'):
        with st.spinner('Model in Progress...'):
            ref = nairobi_dict[pricetype_selected][district_selected][commodity_selected]
            predicted_price, forecast_df = arima_model(ref, date_input)

        st.success("Modeling complete ✔")
        price_message = f'The price forecast for {commodity_selected} on {date_input.strftime("%Y-%m-%d")} is estimated to be KES {round(predicted_price,2)}'

        # Determine the unit based on the selected commodity
        if commodity_selected in commodities_per_kg:
            price_message += " per KG"
        elif commodity_selected in commodities_per_liter:
            price_message += " per Liter"

        st.write(price_message)

if __name__ == "__main__":
    main()

