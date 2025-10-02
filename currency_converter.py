# Web Requests and APIs

import streamlit as st
import requests

st.title("Live Currency Convertor")
amount = st.number_input('Enter the amount in pkr', min_value=1)
tagert_currency = st.selectbox('Select the target currency', ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'INR', 'AUD', 'CAD', 'CHF', 'NZD'])


if st.button('Convert'):
    url = "https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(url)
    
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][tagert_currency]
        converted_amount = amount * rate
        st.success(f"{amount} PKR is equal to {converted_amount:.2f} {tagert_currency}")
    else:
        st.error("Failed to fetch exchange rates. Please try again later.")