import streamlit as st
import pandas as pd

# Sample DataFrame (Replace this with your own DataFrame)
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'San Francisco']
}

df = pd.DataFrame(data)

# Display the first 5 records in a table
st.write("First 5 Records of the DataFrame:")
st.table(df.head(5))
