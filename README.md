# **Food Commodity Prices Analysis and Forecasting in Kenya**

**By:** Charles Kagwanja   **|**   Kevin Kagia  |   Lucy Njambi  |
 Mwenda Mugambi

---

## **Introduction and Project Overview**
This project analyzes and predicts basic food commodity prices in Kenya. By delving into historical data, the initiative seeks to uncover trends and influencing factors, developing predictive models for informed decision-making. Focused on addressing poverty and food security challenges, the project holds potential for significant contributions to agricultural planning, budgeting, and policy formulation. Its success could play a pivotal role in poverty alleviation, improved nutrition, and progress towards the UN Sustainable Development Goal of zero hunger in Kenya. The project aims to Contribute to effective agricultural planning and policy formulation by identifying historical trends, regional variations, and forecasting future prices, ultimately supporting progress towards poverty alleviation and achieving zero hunger in Kenya.

## **Business Understanding**
The prices of agricultural products are subject to frequent and unpredictable fluctuations.These price movements have significant impacts on the livelihoods of farmers, the profitability of wholesalers and retailers, the affordability and accessibility of food for consumers, and the stability and security of the food system.

There is a need for a reliable and timely forecasting model that can predict the future prices of agricultural products based on historical data and current market conditions. Such a model will help the stakeholders to plan, budget, and optimize their production, consumption, and distribution strategies, as well as to anticipate and mitigate the risks and uncertainties associated with the price fluctuations.

In Kenya, where 35.6% live below the international poverty line, challenges include 29% of rural children experiencing stunted growth. With a total population of 48.5 million, securing nutritious food remains a struggle for many. Addressing a third of the population's difficulty in accessing quality food is crucial, aligning with the global goal of zero hunger.

This project responds to these challenges, aiming to provide actionable insights into food commodity price trends and future predictions in Kenya. By employing data science and time series forecasting, the initiative seeks to contribute to more stable and predictable food markets in the country. Further, the project aims to provide valuable insights and recommendations for improving the efficiency and effectiveness of the food system.


## **Project Objectives:**

- **Forecasting Future Prices**: Develop models to predict future commodity prices, enhancing the capacity for informed decision-making.
- **Analyzing Price Trends and Seasonality**: Identify historical patterns in commodity prices across different markets in Kenya.

.**Regional variations analysis:** Examine regional variations in food prices across diverse areas of Kenya, providing insights into market dynamics that impact consumers, retailers, and farmers.


### Primary Stakeholders

- Government Ministries e.g. Ministry of Agriculture, Ministry For Planning and National Development
- Farmers' Associations and Agricultural Cooperatives
- Retailers and Market Analysts
- Donors, Humanitarian and Relief Organizations, Non-Governmental Organizations and International Bodies
- The General Public especially low income earners

### Why This Project Matters
1. **Economic Impact on Farmers and Producers**: Empowering farmers with the knowledge of future price trends, which can guide their crop production and marketing strategies.

2. **Consumer Protection and Budgeting**: Assisting consumers, especially in lower-income groups, to better plan their food budgets.

3. **Policy Making and Food Security**: Enabling policymakers to formulate strategies that can stabilize food markets and ensure food security.

4. **Retail and Distribution Management**: Helping retailers and distributors in optimizing their inventory and pricing strategies.

5. **Aid and Intervention Planning**: Assisting NGOs and international organizations in planning and distributing aid more effectively.

6. **Market Stability and Investment**: Attracting investment in the agricultural sector by providing a clearer understanding of market dynamics.

7. **Research and Development**: Contributing to academic and practical research in market dynamics and agricultural economics.


## **Data Understanding**

### Data Source
The dataset for this project was obtained from the Humanitarian Data Exchange (HDX), specifically from the World Food Programme's food price database for Kenya. The dataset can be accessed [here](https://data.humdata.org/dataset/wfp-food-prices-for-kenya).

This dataset is particularly suitable for our analysis due to the following reasons:
1. **Comprehensiveness**: It covers a wide range of food commodities and spans multiple regions within Kenya.
2. **Relevance**: The data directly relates to the prices of food commodities, which is the central focus of our project.
3. **Timeliness**: The dataset includes recent data, which is crucial for accurate forecasting.


## DATA LIMITATIONS

a) **Data Quality:** The accuracy and reliability of the analysis heavily depend on the quality of the available data. Inaccuracies or missing data points for some market  could impact the validity and accuracy of our timeseries forecasting.

b) **External Factors:** Unforeseen external factors, such as extreme weather events or economic shocks, may not be fully captured in the dataset but can significantly influence commodity prices.

c) **Model Limitations:** The forecasting models used (auto_ARIMA and Prophet) may have inherent limitations and assumptions. Continuous validation and adjustment may be necessary as market dynamics evolve.

d) **Socioeconomic Factors:** The analysis might not fully capture the impact of socioeconomic factors on market dynamics, which could affect the practicality of the recommendations given above.


# Checking the results
price_type_analysis
**Beans:** The majority of price records for beans are for wholesale prices, which are more than three times the records for retail prices. This suggests that beans are commonly traded in bulk, and wholesale prices are more frequently reported.

**Maize:** Wholesale prices for maize also have a higher count compared to retail, but the difference is not as pronounced as with beans. This indicates a significant presence of maize in both wholesale and retail markets.

**Milk:** All price records for milk are retail, indicating that the dataset might be capturing consumer prices rather than bulk trading prices.

**Oil (Vegetable):** Similar to milk, all records for vegetable oil are retail prices, suggesting the data reflects end-consumer pricing.

**Potatoes:** The count of wholesale price records is significantly higher than retail for potatoes, indicating a focus on bulk trade within the dataset for this commodity.

**Sorghum:** Wholesale price records outnumber retail ones.


1. Wholesale emerges as the predominant price type in the Nairobi district.
2. This prevalence may stem from a higher concentration of data collection in markets where small-scale traders procure goods for subsequent retail sales.
#Bar plot visualization of various commodities within the 'Nairobi' district markets


## Selecting the Nairobi District data for our modelling

We chose to work with the Nairobi district  markets data as a representative sample for the broader analysis due to various reasons such as :

a) **High Data Availability**: It has the highest number of entries hence suggesting data completeness and richness. This could lead into creation of a robust timesseries model.

b) **Diverse Commodity Distribution**:he frequency distribution of commodities within the Nairobi district is varied, indicating a diverse market with a broad range of goods or services. This diversity can contribute to a more comprehensive and representative time series analysis.

c) **Economic Significance**:Nairobi being a major economic hub in many regions often reflects trends and patterns that can be indicative of broader economic changes. Time series analysis in this district may provide insights into economic trends that have implications beyond the local context.

d) **Consumer Behavior**:The consumption patterns observed in Nairobi, especially for commonly consumed commodities like beans, maize, and potatoes, can offer insights into consumer behavior over time. This information is crucial for businesses and policymakers.

## CHOICE OF MODEL 

In this project, the use of auto ARIMA (AutoRegressive Integrated Moving Average) has been beneficial for forecasting future trends in commodity prices. By analyzing historical price data, the auto ARIMA model can identify patterns and seasonality in the data and make predictions for future prices.

The model helped  in several aspects such as market optimization, providing insights into forecasted trends which can be used to educate consumers on budgeting strategies based on forecasted food prices and attract investment in the agricultural sector by showcasing a clearer understanding of market dynamics.

However, it is important to highlight the limitations of the model, such as data quality, external, political and socioeconomic factors. The accuracy and reliability of the model heavily depend on the quality of the available data, and unforeseen external, political or socioeconomic factors may not be fully captured in the dataset. Continuous validation and adjustment of the model may be necessary as market dynamics evolve.

Overall, the use of auto ARIMA in this project can provided valuable insights and support decision-making processes related to commodity prices, helping various stakeholders make better-informed decisions.



## CONCLUSION
a) **Price Trends and Seasonality Analysis:** The identification of patterns, through reliance on historical data will aid in anticipating future price movements and aid in proper budgeting especially the low income consumers who are adversely affected by fluctuations in prices of basic commodities.

b) **Regional Variations:** Examination of price differences across regions provides valuable insights into the diverse dynamics of local markets. Variations may be attributed to factors such as geographical location, climate, and economic activities.

c) **Forecasting Future Prices:** The developed time series forecasting models offer a tool for predicting future commodity prices. This can be instrumental for stakeholders in making informed decisions related to agriculture, retail, and policy planning.

d) **Stakeholder Involvement:** Involvement of key stakeholders, including the Kenyan Ministry of Agriculture, farmers' associations, retailers, NGOs, and the general public, is crucial for implementing effective strategies based on the findings.


## RECOMMENDATIONS
a) **Market Optimization for Retailers:** Support retailers and market analysts in optimizing inventory and pricing strategies based on regional variations and forecasted trends.

b) **Consumer Education:** Develop campaigns to educate consumers, especially those in lower-income groups, on budgeting strategies considering the forecasted food prices.

c) **Farmers' Empowerment:** Provide targeted support and information to farmers through associations and cooperatives to enable them to make better-informed decisions about crop production and marketing.

d) **NGO and International Aid Planning:** NGOs and international bodies can use the insights to plan and distribute aid more effectively, targeting regions and periods of higher food insecurity.

e) **Investment Promotion:** Attract investment in the agricultural sector by showcasing a clearer understanding of market dynamics and future trends.
