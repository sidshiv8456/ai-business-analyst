import streamlit as st
import pandas as pd

st.title("AI Business Analyst")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.write(df.head())