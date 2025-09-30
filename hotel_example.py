import streamlit as st
import datetime

# App Title
st.title("🏨 Welcome to the Hotel")

# Section: Customer Information
st.header("👤 Customer Information")
name = st.text_input("Enter your name:")

# Section: Menu Selection
st.header("🍽️ Menu")
dishes = ["Pizza", "Burger", "Biryani", "Pasta", "Salad"]
dish = st.selectbox("Select a dish:", dishes)

# Section: Dish Type (variation)
dish_types = {
    "Pizza": ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"],
    "Burger": ["Beef", "Chicken", "Veggie", "Cheese"],
    "Biryani": ["Chicken", "Beef", "Mutton", "Vegetable"],
    "Pasta": ["Alfredo", "Marinara", "Carbonara", "Pesto"],
    "Salad": ["Greek", "Caesar", "Garden Fresh", "Fruit"]
}
dish_type = st.radio(f"Choose type for {dish}:", dish_types[dish])

# Section: Quantity
quantity = st.number_input("Number of servings:", min_value=1, max_value=10, value=1, step=1)

# Section: Extra Add-ons
st.header("➕ Add-ons")
addons = st.multiselect("Select extras:", ["Cheese", "Fries", "Cold Drink", "Ketchup", "Sauce"])

# Prices
prices = {
    "Pizza": 800,
    "Burger": 500,
    "Biryani": 600,
    "Pasta": 700,
    "Salad": 400
}

addon_prices = {
    "Cheese": 100,
    "Fries": 150,
    "Cold Drink": 120,
    "Ketchup": 50,
    "Sauce": 70
}

# Section: Payment Options
st.header("💳 Payment")
payment = st.radio("Select payment method:", ["Cash", "Credit Card", "Debit Card", "Mobile Wallet"])

# Section: Generate Slip
if st.button("🧾 Generate Bill Slip"):
    if not name:
        st.error("Please enter your name to proceed!")
    else:
        # Get current date & time
        order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Calculate bill
        dish_total = prices[dish] * quantity
        addons_total = sum([addon_prices[a] for a in addons]) * quantity
        total_bill = dish_total + addons_total

        # Display slip
        st.success("✅ Order Confirmed! Your slip is generated below.")
        st.subheader("🧾 Customer Slip")
        st.write(f"**Customer Name:** {name}")
        st.write(f"**Dish Ordered:** {dish} ({dish_type})")
        st.write(f"**Quantity:** {quantity}")

        if addons:
            st.write(f"**Add-ons:** {', '.join(addons)}")
        else:
            st.write("**Add-ons:** None")

        st.write(f"**Payment Method:** {payment}")
        st.write(f"**Order Time:** {order_time}")

        st.markdown("---")
        st.subheader("💰 Bill Summary")
        st.write(f"Dish Price: Rs. {prices[dish]} × {quantity} = Rs. {dish_total}")
        if addons:
            st.write(f"Add-ons Price: Rs. {addons_total}")
        st.write(f"**Total Bill: Rs. {total_bill}**")

        st.markdown("---")
        st.info("🍴 Thank you for dining with Streamlit Hotel! We hope you enjoy your meal.")
