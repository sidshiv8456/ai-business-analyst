import streamlit as st
import pandas as pd

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

    df = pd.read_excel(
        uploaded_file,
        sheet_name="Sales_Data"
    )

    # KPI Calculations

    total_revenue = df["Revenue"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order_ID"].nunique()

    total_customers = df["Customer_ID"].nunique()

    average_order_value = total_revenue / total_orders

    average_profit_per_order = total_profit / total_orders

    # KPI Cards

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric(
            "💰 Revenue",
            f"₹ {total_revenue:,.0f}"
        )

    with col2:
        st.metric(
            "📈 Profit",
            f"₹ {total_profit:,.0f}"
        )

    with col3:
        st.metric(
            "📦 Orders",
            total_orders
        )

    with col4:
        st.metric(
            "👥 Customers",
            total_customers
        )

    with col5:
        st.metric(
        "🛒 Avg Order Value",
        f"₹ {average_order_value:,.0f}"
    )

    with col6:
        st.metric(
            "📈 Avg Profit Per Order",
            f"₹ {average_profit_per_order:,.0f}"
        )

    st.divider()

    st.subheader("Data Preview")

    st.dataframe(df.head())