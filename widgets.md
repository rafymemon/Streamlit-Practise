# Streamlit Widgets Documentation

Widgets in **Streamlit** are interactive elements that let users input or control values in your app. Below is a quick reference table followed by detailed examples.

---

## 📌 Quick Reference Table

| Widget            | Function/Purpose                             |
| ----------------- | -------------------------------------------- |
| **Button**        | Trigger an action when clicked               |
| **Checkbox**      | Toggle between `True` / `False`              |
| **Radio**         | Select one option from a list                |
| **Selectbox**     | Dropdown to choose a single option           |
| **Multiselect**   | Choose multiple options from a list          |
| **Slider**        | Select a numeric value (or range) by sliding |
| **Text Input**    | Enter free text                              |
| **Number Input**  | Enter a numeric value with min/max/step      |
| **Date Input**    | Pick a date from a calendar                  |
| **File Uploader** | Upload files from local system               |

---

## 1. Button

```python
import streamlit as st

if st.button("Click Me"):
    st.write("Button was clicked!")
```

---

## 2. Checkbox

```python
agree = st.checkbox("I agree")
if agree:
    st.write("Thanks for agreeing!")
```

---

## 3. Radio Buttons

```python
choice = st.radio("Pick one:", ["Apple", "Banana", "Cherry"])
st.write("You selected:", choice)
```

---

## 4. Selectbox (Dropdown)

```python
option = st.selectbox("Choose a number", [1, 2, 3, 4, 5])
st.write("You chose:", option)
```

---

## 5. Multiselect

```python
options = st.multiselect("Pick multiple", ["Red", "Green", "Blue"])
st.write("You picked:", options)
```

---

## 6. Slider

```python
number = st.slider("Select a value", 0, 100, 25)
st.write("Your number is", number)
```

---

## 7. Text Input

```python
name = st.text_input("Enter your name")
st.write("Hello,", name)
```

---

## 8. Number Input

```python
age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
st.write("You are", age, "years old")
```

---

## 9. Date Input

```python
date = st.date_input("Pick a date")
st.write("Your date:", date)
```

---

## 10. File Uploader

```python
file = st.file_uploader("Upload a file")
if file:
    st.write("File uploaded:", file.name)
```

---

## Why Use Widgets?

* Make apps **interactive**
* Enable **data exploration**
* Allow **user input** (upload files, tune parameters, select models)

---
