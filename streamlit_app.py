import streamlit as st
import pandas as pd

# Sample DataFrame (Replace this with your own DataFrame)


df = pd.read_csv('CVS.csv')

# Display the first 5 records in a table
st.write("First 5 Records of the DataFrame:")
st.table(df.head(5))
