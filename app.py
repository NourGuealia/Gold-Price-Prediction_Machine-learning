import streamlit as st 
import pickle
import pandas as pd
import numpy as np
# import the model :
model = pickle.load(open('./savedModel/model.sav', 'rb'))

st.title("🪙 Gold price Prediction ")
st.subheader("Gold price Prediction using :blue[Machine Learning] model")

with st.container():
    st.header("Fields explanation")
    st.text("CSMP : the capitalization for 500 companies ( stock publicaly trated ) ")
    st.text("USO : United state Oil price ")
    st.text("Silver price : The silver price ($)")
    st.text("EUR/USD : currency pair of european euro and united state dollar ")

with st.container():
    st.header("Predict gold price ")
    placeholder = st.empty()

    col1 , col2 = st.columns(2)

    with col1 : 
        spx = st.number_input('SPX / CSMP index  : ')
        expanderSPX = st.expander("See explanation")
    with col2 : 
        uso = st.number_input('USO : ')


    with col1 : 
        slv = st.number_input('Silver price : ')
    with col2 : 
        eurToUsd = st.number_input('EUR/USD')

with st.container():
    
    if st.button('Get the price') : 
          data = pd.DataFrame(np.array([spx ,uso , slv , eurToUsd]).reshape(1 , -1), columns=['SPX' , 'USO' , 'SLV' ,'EUR/USD'])
          prediction = model.predict(data)
          placeholder.success( "the price predicted is : " +  str(prediction[0]) +" $")
         
