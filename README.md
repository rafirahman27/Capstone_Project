# MarketMaster: Predicting your Car's Sales Price
---
## Problem Statement
---
In the complex and ever-evolving used car market, determining the fair market value of a used vehicle can be a daunting task for individuals, with most often relying on online guides or dealer estimates. These methods often lack the ability to comprehensively assess the unique features and market conditions that influence a car's worth, leading to potential financial losses for sellers who underestimate their vehicle's true value.

To address this challenge, the objective to this project will be to develop a machine learning model that utilizes vehicle catalogs from multiple sources, to reduce bias and capture a wider range of market variations and provide precise price predictions to the user.

---
## Background Research
---
In 2021 the UK 2nd hand car market was recorded to be worth $117.69 Billion with it expected to reach $226.16 Billion by 2027. Now just like any other market, it has its own fluctuations, like the Covid-19 outbreak where sales dropped by 15%, then the silion shortage which led to reduced new vehicle production, increasing sales within the 2nd hand car market.

Accurately predicting the price of a used car is a complex task that involves considering a multitude of factors, including the vehicle's make, model, year, mileage, condition, location, and market trends. Traditionally, car sellers have relied on subjective methods such as online guides, dealer estimates, or personal experience to determine their vehicle's value. However, these methods often lack the accuracy and comprehensiveness needed to make informed pricing decisions.

Various studies have demonstrated the potential of utilizing machine learning for car price prediction. For instance, Samruddhi and Kumar (2020) proposed a supervised machine learning model using K-Nearest Neighbors to predict used car prices. Their model achieved an accuracy of up to 85% when trained on a dataset of over 10,000 used cars. Similarly, Pudaruth (2014) explored the use of decision tree, K-nearest neighbors, multiple regression, and naïve Bayes algorithms to predict used car prices in Mauritius. Their results showed that machine learning algorithms can outperform traditional methods in terms of accuracy.

A key challenge with this problem is the potential for bias within the data. If the training data is not representative of the entire population of used cars, the ML model may produce biased predictions leading to unfair pricing outcomes for certain owners. This can be overcome by collecting and utilizing more diverse and representative data sets by obtaining data from multiple different sources to reduce the bias and ensure fair pricing for all car sellers.

---
## Data Dictionary
---
The data used within this project has been webscrapped from Cazoo, BuyaCar and Motorpoint, this information has then be put into the following format.

|Feature|Type|Dataset|Description|
|---|---|---|---|
|Model|*String*|Audi|Vehicle Manufacturers|
|Model|*String*|A3|Model of the vehicle|
|Trim|*String*|TFSI Black Edition|Signifies the variation of the model|
|engine_size|*float*|2.0|Engine size for the vehicle|
|num_doors|*int*|3|The number of doors the vehicle has|
|mileage|*int*|27204|Miles that the vehicle has travelled|
|reg_year|*int*|2019|The year the vehicle was registered on the road|
|fuel_type|*string*|Petrol|The type of fuel that vehicle uses|
|transmission_type|*string*|Manual|The type of gearbox the vehicle has|
|price|*int*|9400|The sales price of the vehicle|

---
## Executive Summary
---

By leveraging this diverse data that we was able to webscrape, our model is able to provide precise price predictions, empowering car sellers to make informed decisions, navigate the car market with confidence, and maximize their returns.

Our model demonstrated high accuracy in predicting car prices with a R2 Score of 99.21% with our test data, achieving an mean absolute error (MAE), which is the average difference between the predicted and actual prices of 136.8079.

---
## Methodology
---

The first step involved gathering data from various online second-hand vehicle sales platforms. To achieve this, we employed the BeautifulSoup library, an effective tool for web scraping. We carefully selected websites that provided open access to their data, ensuring ethical and compliant data acquisition.

Once the data was collected, we embarked on a rigorous data cleaning and preprocessing phase. This involved removing outliers, handling missing values, and transforming categorical data into numerical representations using techniques like CountVectorizer and OneHotEncoder. This process ensured data quality and consistency, preparing the data for subsequent analysis and modeling.

To determine the most suitable machine learning algorithm for our problem statement, we employed a model selection approach. We initially trained and evaluated two distinct model types: a Linear Regression model and a Tree-based model. By comparing their performance metrics, we can understand what type of model will perform the best for our problem statement, before proceeding with our model tuning process. 

---
## Conclusion & Recommendations
---
In conclusion, we developed a machine learning model for predicting the price of used cars using data gathered from multiple sources to reduce bias and capture a wider range of market variations. We employed an. ExtraTrees Model, a tree-based ensemble method as our final production model due to its superior performance compared to a Linear Regression model.

To further enhance the accessibility and usability of our model, we successfully implemented it into a Streamlit web application. This interface allows individuals to easily input their car's specifications and receive real-time price predictions.

Overall our ExtraTrees model achieved a mean absolute error (MAE) of 136.8079 and an R-squared score of 99.21% on the test data. These results indicated that our model can provide accurate car price predictions empowering individuals to make informed decisions when. selling their used cars.

To further this project you could explore:
1) Incorporating additional data sources to increase the number of vehicles that the model is trained on and to also capture more market treads. This could be done by exploring manufacturers approved websites or private listings.
2) Investigating more complex machine learning algoriths, such as deep learning models, could potentially improve the model's accuracy and improve the models performance, especially on rare or unique car models.
3) Creating a mobile applications that integrates the model would provide individuals with a convenient and on-the-go tool for car price predictions.

---
## Citations
---
1) Mordor Intelligence - Used Car Market in UK Size & Share Analysis - Growth Trends & Forecasts (2023 - 2028) Source: https://www.mordorintelligence.com/industry-reports/unitedkingdom-used-car-market
2) Pudaruth, S. (2014). A comparative study of machine learning algorithms in used car price prediction. Journal of Applied Mathematics, 2014, 1-11.
3) Samruddhi, M., & Kumar, A. (2020). Used Cars Price Prediction and Valuation using Data Mining Techniques. RIT Scholar Works, Rochester Institute of Technology.