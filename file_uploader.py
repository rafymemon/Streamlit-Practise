import streamlit as st
import pandas as pd

st.title("File Uploader Example")

file = st.file_uploader("Upload a CSV file", type =['CSV'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
    
if file:
    st.subheader("Statistical Summary")
    st.write(df.describe())
    
if file:
    outlook = df['outlook'].unique()
    selected_outlook = st.selectbox("Select Outlook", outlook)
    filtered_data = df[df['outlook'] == selected_outlook]
    st.dataframe(filtered_data)