# Commodity_Price_Forecasting.
**By:** Charles Kagwanja   **|**   Kevin Kagia  |   Lucy Njambi  |
 Mwenda Mugambi
 
---

This project aimed to analyze and predict wholesale prices in Nairobi, Kenya, harnessing historical data to develop predictive models. It focuses on identifying trends and factors influencing these prices, thereby facilitating informed decision-making in agricultural planning, budgeting, and policy formulation. The project's overarching goal is to contribute to poverty alleviation, improved nutrition, and the realization of the UN Sustainable Development Goal of zero hunger in Kenya.

[Test the deployed model here](https://beanpricepredictions.streamlit.app/)

## Business Context
Focused on Nairobi County's volatile food market, this project addresses the challenge of price unpredictability that affects various sectors. By leveraging data analytics and Time series modeling, the goal is to enhance decision-making processes for entities involved in the supply chain, aligning with efforts to combat poverty and ensure food security in Kenya.

## Business Challenge
The main challenge was developing a reliable forecasting model capable of accurately predicting prices, crucial for effective planning and strategizing. This involved analyzing complex market dynamics and data patterns to anticipate future trends.

**Stakeholders**
* **Nairobi County Government:** Plays a pivotal role in local governance, including agricultural market oversight and support within Nairobi. 
* **Kenyan Ministry of Agriculture:** Responsible for agricultural policies and market regulation.
* **Retailers and Distributors:** Key players in the supply chain, managing distribution and sales of beans.

## Data Source
The dataset for this project was obtained from the Humanitarian Data Exchange (HDX), specifically from the World Food Programme's food price database for Kenya. The dataset can be accessed [here](https://data.humdata.org/dataset/wfp-food-prices-for-kenya).

This dataset was particularly suitable for our analysis due to the following reasons:
1. **Comprehensiveness**: It covers a wide range of food commodities and spans multiple regions within Kenya.
2. **Relevance**: The data directly relates to the prices of food commodities, which is the central focus of our project.
3. **Timeliness**: The dataset includes recent data, which is crucial for accurate forecasting.

## Methods Applied
* Exploratory data analysis
* Data Preprocessing 
  
## Modeling and Evaluation
Our modeling journey began with a baseline model using a simple ARIMA. This helped set a performance benchmark. We then explored a more complex model (SARIMA) to improve upon the baseline.
### Baseline ARIMA Model
- **RMSE**: 13.8997
- ![image](https://github.com/Mwenda-Mugambi/Commodity_Price_Forecasting/assets/132069152/9ad99f7b-9d65-4100-80d9-30c7748ddd70)


### SARIMA Model 1
- **RMSE**: 11.66
- ![image](https://github.com/Mwenda-Mugambi/Commodity_Price_Forecasting/assets/132069152/b9fc517c-66bf-441e-9a4f-f2229cb74943)


### SARIMA Model 2
- **RMSE**: 11.60
- ![image](https://github.com/Mwenda-Mugambi/Commodity_Price_Forecasting/assets/132069152/5d5e44af-a9ab-4a13-a91e-724683af7ada)


### SARIMA Model 3
- **RMSE**: 11.58
- ![image](https://github.com/Mwenda-Mugambi/Commodity_Price_Forecasting/assets/132069152/66f438a3-3508-494d-ae6e-994e2020d63f)
- SARIMA Model 3 achieved the lowest RMSE among the models we tested, indicating the highest forecasting accuracy. The slight improvement over SARIMA Model 2 suggested that the additional complexity or changes in the model parameters were capturing the underlying seasonal patterns just a bit more closely.

## Conclusion
Throughout our analysis, we observed the impact of incorporating seasonality into our time series models. The improvement in RMSE from the Baseline ARIMA model to the SARIMA models validated our hypothesis that seasonality is a significant component of our dataset.

The Baseline ARIMA model, without accounting for seasonality, had the highest RMSE, indicating a less accurate model. Each subsequent SARIMA model, which incorporated seasonal elements, showed a decrease in RMSE, underscoring the importance of capturing seasonal patterns.

Despite the progressive enhancements, the RMSE differences between the SARIMA models were relatively minor. SARIMA Model 3, while yielding the lowest RMSE, offered only a slight improvement over SARIMA Model 2. This marginal gain needs to be considered in the context of model complexity and operational efficiency.

The model diagnostics have confirmed that the residuals of all models exhibit no significant autocorrelations and are well approximated by a normal distribution, indicating that the models are well-specified and the underlying assumptions are reasonable.

## Reccomendations
#### Nairobi County Government:
* **Market Regulation and Support:** Implement regulatory measures to prevent market manipulation and ensure fair pricing for both farmers and consumers.
* **Infrastructure Development:** Invest in infrastructure improvements, like better storage facilities and transportation networks, based on predicted high-demand areas and times.
* **Community Support Programs:** Develop programs to support low-income communities during periods when bean prices are forecasted to rise, ensuring food security.

#### Retailers and Distributors:
* **Inventory Management:** Adjust purchasing and stocking strategies based on price trend forecasts to maximize profits and reduce waste.
* **Dynamic Pricing Strategies:** Implement dynamic pricing models that reflect the predicted fluctuations in bean prices, enhancing profitability.
* **Supply Chain Optimization:** Use insights to streamline the supply chain, improving logistics and reducing costs during predicted low-demand periods.

#### Kenyan Ministry of Agriculture:
* **Policy Formulation:** Utilize the predictive model's insights to develop policies that stabilize bean prices and support farmers during low-profit periods.
* **Subsidy Allocation:** Allocate subsidies and resources more effectively, targeting areas and times when the market predicts a downturn.
* **Agricultural Training Programs:** Implement training programs for farmers based on identified trends, focusing on crop diversification and modern farming techniques to mitigate risks.
