import streamlit as st


# st.title('Hello, Streamlit!')
# st.subheader('This is a subheader')
# st.text('This is a simple text element.')
# st.markdown('This is a **markdown** element with _formatting_.')
# st.write('This is a write element that can display various data types.')

# select = st.selectbox('Choose your selection', [
#     'Option 1', 'Option 2', 'Option 3'
# ])
# st.write(f'You Choose {select}. Excellent Choice') 
# st.success(f'Your {select} is selected successfully!')


# Age Calculator App

import datetime as dt
from  dateutil.relativedelta import relativedelta

st.title("Age Calculate APP")
st.subheader("Automate Calculate Age")

date = st.date_input(
    "Please select your birthdate:",
    min_value=dt.date(1900, 1, 1),
    max_value=dt.date.today()
)
current_date = dt.date.today()

diff = relativedelta(current_date, date)
st.write(f"Your age is: {diff.years} years, {diff.months} months, and {diff.days} days.") 