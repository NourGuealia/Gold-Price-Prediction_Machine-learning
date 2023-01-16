# Gold-Price-Prediction_ML
A Gold Price Prediction model using Machine learning

## Screenshots
![Screenshot 2023-01-16 at 15-46-05 app · Streamlit](https://user-images.githubusercontent.com/120994590/212705412-818bac08-d2e8-4245-9fb6-d04f7ee7e9d5.png)

## Data set
- Link : https://www.kaggle.com/datasets/altruistdelhite04/gold-price-data
  
- Description : 
  - The dataset used provides information (4 parameters) that affects the change in the price of gold
- Attributes :
  - SPX : Called CSMP index, the capitalization for 500 companies ( stock publicaly trated )
  - USO : United state Oil price 
  - SLV : The silver price ($)
  - EUR/USD : currency pair of european euro and united states dollar ( 1 Euro = ? Dollar )
- Target variable :
  - GLD : Gold price 

## Project Overview : 
This project is devided into two parts  : 
- Creation and Training model : 
    - /data/gld_price_data.csv : Dataset CSV File
    - /code/ModelTraining.ipynb : Model source code file 
    - /savedModel/model.sav : Model saved 
- Ui : using Streamlit tool
    - /app.py : Main file of the ui

## Getting started

1. Clone the repository
2. install required python packages if previously not installed
3. Switch to the project directory
4. Run the ModelTraining.ipynb step by step (This will retrain the model)
5. Run `streamlit run app.py` to run the web UI




