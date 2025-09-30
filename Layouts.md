# Streamlit Layouts

Streamlit provides multiple ways to arrange and organize widgets and components on your app. Layouts help create visually appealing and interactive dashboards.

---

## 1. Sidebar

The **sidebar** is a special area on the left side of the app where you can place widgets for navigation, filters, or inputs.

```python
import streamlit as st

# Sidebar widgets
st.sidebar.title("Sidebar Example")
st.sidebar.text_input("Enter your name")
st.sidebar.slider("Select Age", 1, 100, 25)

st.write("Main content area remains here.")
```

---

## 2. Columns

Columns help you place widgets or text side by side.

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")
    st.button("Click Me")

with col2:
    st.write("Column 2")
    st.radio("Pick one:", ["A", "B", "C"])
```

---

## 3. Tabs

Tabs let you organize content into multiple views.

```python
tab1, tab2 = st.tabs(["Home", "Settings"])

with tab1:
    st.write("This is the Home tab")

with tab2:
    st.write("This is the Settings tab")
```

---

## 4. Expander

An expander allows you to hide/show content interactively.

```python
with st.expander("See more details"):
    st.write("Here is some hidden content that expands when clicked.")
```

---

## 5. Containers

Containers group together widgets or elements.

```python
with st.container():
    st.write("This content is inside a container")
    st.checkbox("Check me")
```

---

## Example: Combining Layouts with Sidebar

```python
import streamlit as st

# Sidebar filter
st.sidebar.title("Controls")
discount = st.sidebar.slider("Select Discount (%)", 0, 50, 10)

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.header("Product A")
    price_a = 200
    final_a = price_a - (price_a * discount / 100)
    st.write(f"Price after discount: ${final_a}")

with col2:
    st.header("Product B")
    price_b = 350
    final_b = price_b - (price_b * discount / 100)
    st.write(f"Price after discount: ${final_b}")

st.success("Bill generated successfully!")
```

---

## Layouts Overview Table

| Layout Type   | Purpose                                            | Example                     |
| ------------- | -------------------------------------------------- | --------------------------- |
| **Sidebar**   | Place filters, navigation, inputs on the left side | `st.sidebar.slider()`       |
| **Columns**   | Arrange widgets side by side                       | `st.columns(2)`             |
| **Tabs**      | Create multiple views in one page                  | `st.tabs(["Tab1", "Tab2"])` |
| **Expander**  | Hide/Show details interactively                    | `st.expander("See more")`   |
| **Container** | Group widgets together                             | `st.container()`            |
