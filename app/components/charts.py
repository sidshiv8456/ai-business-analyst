import streamlit as st
import plotly.express as px


def show_revenue_trend(df):

    st.subheader("📈 Monthly Revenue Trend")

    monthly_revenue = (
        df.groupby(
            df["Date"].dt.to_period("M")
        )["Revenue"]
        .sum()
        .reset_index()
    )

    monthly_revenue["Date"] = (
        monthly_revenue["Date"]
        .astype(str)
    )

    fig = px.line(
        monthly_revenue,
        x="Date",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_region_performance(df):

    st.subheader("🌍 Region Performance")

    region_sales = (
        df.groupby("Region")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(
            by="Revenue",
            ascending=False
        )
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Revenue",
        text_auto=True,
        title="Revenue by Region"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_top_customers(df):

    st.subheader("🏆 Top 10 Customers")

    top_customers = (
        df.groupby("Customer_Name")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(
            by="Revenue",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top_customers,
        x="Customer_Name",
        y="Revenue",
        text_auto=True,
        title="Top 10 Customers by Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_category_analysis(df):

    st.subheader("📦 Revenue by Product Category")

    category_sales = (
        df.groupby("Product_Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_sales,
        names="Product_Category",
        values="Revenue",
        title="Revenue Contribution by Product Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )