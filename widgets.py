import streamlit as st

st.title('Chai Maker App  || Streamlit Widgets Example')

if st.button('Make Chai'):
    st.success('Chai is ready! Enjoy your drink!')
    
add_sugar = st.checkbox('Add sugar')
if add_sugar:
    sugar_level = st.slider('Select sugar amount (in tsp):', 0, 5, 1)
    # st.write('Sugar added to your chai.')
    st.write(f'Sugar level set to {sugar_level} tsp.')
    
tea_types = st.radio('Choose your tea type:', [
    'Black', 'Green', 'Herbal'
    ])

st.write(f'You selected {tea_types} tea.')

flavour = st.selectbox('Select a flavour:', [
    'Cardamom', 'Ginger', 'Masala', 'Plain'
    ])
st.write(f'You selected {flavour} flavour.')



cups = st.number_input('How many number of cups? ', min_value=1, max_value=10, value=1, step=1)
if st.button('Get Chai'):
    st.success(f'You will get {cups} cup(s) of chai.')
    

name = st.text_input("Enter your name:")
if name: 
    st.write(f'Welcome, {name}! Your chai is on the way.')