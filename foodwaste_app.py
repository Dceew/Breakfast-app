#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[114]:


# foodwaste_app.py
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")


# In[105]:


# Load trained model
model = joblib.load('foodwaste_model.pkl')


# In[106]:


# Page title
st.title("Food Waste Prediction App")


# In[ ]:





# In[107]:


menu_options = [
    'Menu_Idaly Wada Sambhar',
    'Menu_Masala Upit',
    'Menu_Medu Vada Sambhar',
    'Menu_Onion Uttapa',
    'Menu_Poha',
    'Menu_Poori Bhaji and Bread Omlette',
    'Menu_Sabudana Khichdi',
    'Menu_Tomato Uttapam',
    'Menu_Upma'
]


# In[ ]:





# In[108]:


day_of_week = st.selectbox("Select Day of the Week", ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
food_ordered = st.number_input("Enter Food Ordered (in kg)", min_value=0.0, step=0.1)
Headcount = st.number_input("Enter Estimated Headcount", min_value=0, step=1)
selected_menu = st.selectbox("Select Menu Item", menu_options)
menu_one_hot = {menu: 0 for menu in menu_options}
menu_one_hot[selected_menu] = 1


# In[109]:


# Preprocess input
#day_of_week = pd.to_datetime(date_input).day_name()


# In[110]:


#Optional: map menu to number like in training
#menu_mapping = {'Menu_Idaly Wada Sambhar': 1, 'Menu_Masala Upit': 1, 'Menu_Medu Vada Sambhar': 1, 'Menu_Onion Uttapa':1, 'Menu_Poha':1,
          #     'Menu_Poori Bhaji and Bread Omlette':1,'Menu_Sabudana Khichdi':1,'Menu_Tomato Uttapam':1,'Menu_Upma':1}
#menu_code = menu_mapping[menu_type]


# In[111]:


# Day name to code
day_mapping = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
}

day_code = day_mapping[day_of_week]


# In[112]:


# Create input dataframe (must match training columns)
input_data = {
    'Days': day_code,
    'Headcount': Headcount,
    'FoodOrdered': food_ordered,
    **menu_one_hot
}

input_df = pd.DataFrame([input_data])


# In[ ]:





# In[113]:


# Prediction button
if st.button("Predict Food Waste"):
    prediction = model.predict(input_df)[0]
    print("Prediction:", prediction)
    print("Type:", type(prediction))
    st.success(f"Estimated Unused Food Waste: {prediction[0]:.2f} units")


# In[ ]:




