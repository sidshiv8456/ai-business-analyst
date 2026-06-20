import streamlit as st

from utils.data_loader import load_data
from utils.calculations import calculate_kpis

from components.filters import apply_filters
from components.kpi_dashboard import show_kpis

from components.charts import (
    show_revenue_trend,
    show_region_performance,
    show_top_customers,
    show_category_analysis
)


st.set_page_config(
    page_title="AI Business Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analyst")

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    filtered_df = apply_filters(df)

    if filtered_df.empty:

        st.warning(
            "No data available."
        )

        st.stop()

    kpis = calculate_kpis(
        filtered_df
    )

    show_kpis(kpis)

    st.divider()

    show_revenue_trend(filtered_df)

    st.divider()

    show_region_performance(filtered_df)

    st.divider()

    show_top_customers(filtered_df)

    st.divider()

    show_category_analysis(filtered_df)

else:

    st.info(
        "Upload an Excel file to begin."
    )