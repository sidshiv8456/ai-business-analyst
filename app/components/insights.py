import streamlit as st
import pandas as pd


def show_insights(df):

    st.subheader("🧠 Automated Business Insights")

    total_revenue = df["Revenue"].sum()

    # -------------------------------
    # Region Analysis
    # -------------------------------

    region_sales = (
        df.groupby("Region")["Revenue"]
        .sum()
        .reset_index()
    )

    best_region = (
        region_sales
        .sort_values(
            by="Revenue",
            ascending=False
        )
        .iloc[0]
    )

    worst_region = (
        region_sales
        .sort_values(
            by="Revenue"
        )
        .iloc[0]
    )

    st.success(
        f"""
⭐ Best Performing Region

{best_region['Region']}

Revenue: ₹{best_region['Revenue']:,.0f}
"""
    )

    st.warning(
        f"""
⚠ Lowest Performing Region

{worst_region['Region']}

Revenue: ₹{worst_region['Revenue']:,.0f}
"""
    )

    # -------------------------------
    # Category Analysis
    # -------------------------------

    category_sales = (
        df.groupby(
            "Product_Category"
        )["Revenue"]
        .sum()
        .reset_index()
    )

    top_category = (
        category_sales
        .sort_values(
            by="Revenue",
            ascending=False
        )
        .iloc[0]
    )

    st.info(
        f"""
📦 Top Product Category

{top_category['Product_Category']}

Revenue: ₹{top_category['Revenue']:,.0f}
"""
    )

    # -------------------------------
    # Customer Concentration Risk
    # -------------------------------

    customer_sales = (
        df.groupby(
            "Customer_Name"
        )["Revenue"]
        .sum()
        .reset_index()
        .sort_values(
            by="Revenue",
            ascending=False
        )
    )

    top_customer = customer_sales.iloc[0]

    customer_share = (
        top_customer["Revenue"]
        / total_revenue
    ) * 100

    if customer_share > 20:

        st.error(
            f"""
🚨 Revenue Dependency Risk

{top_customer['Customer_Name']}

Contributes {customer_share:.1f}%
of total revenue.
"""
        )

    # -------------------------------
    # Profitability Insight
    # -------------------------------

    total_profit = df["Profit"].sum()

    profit_margin = (
        total_profit
        / total_revenue
    ) * 100

    if profit_margin < 10:

        st.error(
            f"""
⚠ Low Profit Margin

Current Margin:
{profit_margin:.2f}%
"""
        )

    else:

        st.success(
            f"""
✅ Healthy Profit Margin

Current Margin:
{profit_margin:.2f}%
"""
        )