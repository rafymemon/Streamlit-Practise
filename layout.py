import streamlit as st

st.title("Streamlit Layouts Example")

col1, col2 = st.columns(2)

with col1:
    st.header("Adrak Chai")
    st.image("https://images.unsplash.com/photo-1625033405953-f20401c7d848?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2hhaXxlbnwwfHwwfHx8MA%3D%3D", use_container_width=True)
    vote1 = st.button("Vote for Adrak Chai")
    
with col2: 
    st.header('Green tea')
    st.image("https://plus.unsplash.com/premium_photo-1694540110881-84add98c0a75?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Z3JlZW4lMjB0ZWF8ZW58MHx8MHx8fDA%3D", use_container_width=True)
    vote2 = st.button("Vote for Green Tea")
    
if vote1:
    st.success("You voted for Adrak Chai")
elif vote2:
    st.success("You voted for Green Tea")
    
    
    
    
    
name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("Select your tea:", ["Adrak Chai", "Green Tea", "Black Tea", "Masala Chai"])

st.write(f"Hello, {name}! Your {tea} will be served to you shortly.")


with st.expander("Chai Instructions"):
    st.write("""
             1. Boil water.
             2. Add tea leaves and spices.
             3. Add milk and sugar.
             4. Simmer for a few minutes.
             5. Strain and serve hot.
             6. Enjoy your chai!
             """)
    
    
    
st.markdown('### Wekcome to the Tea Shop')
st.markdown('> Blackquote')