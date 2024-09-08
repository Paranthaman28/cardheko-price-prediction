import streamlit as st # web development
from streamlit_option_menu import option_menu
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor

df=pd.read_csv(r"C:\Users\Paranthaman\OneDrive\Desktop\project 3\concat_project3")
df1=pd.read_csv(r"C:\Users\Paranthaman\OneDrive\Desktop\project 3\my_final_concat")
st.set_page_config(
    page_title='CarDheko price pridection',
    layout='wide'
)
#dasboard title
st.title('CarDheko Price Prediction')
select=option_menu("main menu",options=['Home','Create the Model','prediction'],
                   icons=['house','pencil-square','phone'],
                   styles={'container':{'padding':'10!important','width':'100'},"icon": {"color": "black", "font-size": "20px"}}
)

if select=='Create the Model':
        col1,col2=st.columns(2)
        
        with col1:
            Fuel_type=st.selectbox('Select the fuel type',df['fuel_type'].unique())
            df_1=df[df['fuel_type']==Fuel_type]
            body_type=st.selectbox('Select the body type',df['body_type'].unique())
            df_1=df[df['body_type']==body_type]
            owner_type=st.selectbox('Select the owner type',df['owner_type'].unique())
            df_1=df[df['owner_type']==owner_type]
            transmission_type=st.selectbox('Select the transmission type',df['transmission_type'].unique())
            df_1=df[df['body_type']==transmission_type]
            manufacture_year=st.selectbox('Select the manufacture year',df['manufacture'].unique())
            df_1=df[df['manufacture']==manufacture_year]
            kilometer=st.selectbox('Select the kilometer in log',df1['kilometers_log'].unique())
            df_1=df1[df1['kilometers_log']==kilometer]
        with col2:
              seat=st.selectbox('Select the seat type',df['seat'].unique())
              df_1=df[df['seat']==seat]
              car_model=st.selectbox('Select the number of owner',df['oem'].unique())
              df_1=df[df['oem']==car_model]
              Mileage=st.selectbox('Select the Mileage',df['mileage'].unique())
              df_2=df[df['mileage']==Mileage]
              Engine_Capacity=st.selectbox('Select the Engine Capacity',df['engine_capacity'].unique())
              df1=df[df['engine_capacity']==Engine_Capacity]
              city=st.selectbox('Select the city',df['city'].unique())
              df_2=df[df['city']==city]

if select=='prediction':
    input_data=df.drop(columns=['price'])
    output_data=df['price']

    x_train,x_test,y_train,y_test=train_test_split(input_data,output_data,test_size=0.2)

    def RandomForest(df1):
        input_data=df1.drop(columns=['price'])
        output_data=df1['price']
        X_train,X_test,y_train,y_test=train_test_split(input_data,output_data,test_size=0.2)
        model=RandomForestRegressor().fit(X_train,y_train)
        y_pred= model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)

        return mse
    
    st.write("## [**The Selling Price of the you choosed Feature car is:**]",RandomForest(df1))
    