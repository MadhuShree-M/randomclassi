import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Random classifier", layout="centered")

# Title
st.title("🚀 Random Classifier")
st.write("This is a basic Streamlit application example.")

# Sidebar
st.sidebar.header("User Input")

name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=1, max_value=120)
salary = st.sidebar.number_input("Enter your monthly salary", min_value=0)

# Main content
if st.button("Submit"):
    st.success("Data submitted successfully!")

    st.write("### User Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Salary:** ₹{salary}")

    # Simple calculation
    yearly_salary = salary * 12
    st.info(f"💰 Estimated Yearly Salary: ₹{yearly_salary}")

# Sample DataFrame
st.write("### Sample Data")
data = {
    "Values": np.random.randint(10, 100, 5)
}
df = pd.DataFrame(data)
st.dataframe(df)

# Chart
st.write("### Sample Chart")
st.bar_chart(df)
