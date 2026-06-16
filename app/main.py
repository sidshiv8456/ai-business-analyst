import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Business Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analyst")

# --------------------------------------------------
# File Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

# --------------------------------------------------
# Main App
# --------------------------------------------------

if uploaded_file:

    # Read Excel File
    df = pd.read_excel(
        uploaded_file,
        sheet_name="Sales_Data"
    )

    # Convert Date Column
    df["Date"] = pd.to_datetime(df["Date"])

    # --------------------------------------------------
    # KPI Calculations
    # --------------------------------------------------

    total_revenue = df["Revenue"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order_ID"].nunique()

    total_customers = df["Customer_ID"].nunique()

    average_order_value = total_revenue / total_orders

    average_profit_per_order = total_profit / total_orders

    profit_margin = (total_profit / total_revenue) * 100

    # --------------------------------------------------
    # KPI Dashboard
    # --------------------------------------------------

    st.subheader("📌 Business KPIs")

    row1 = st.columns(3)

    with row1[0]:
        st.metric(
            "💰 Revenue",
            f"₹ {total_revenue:,.0f}"
        )

    with row1[1]:
        st.metric(
            "📈 Profit",
            f"₹ {total_profit:,.0f}"
        )

    with row1[2]:
        st.metric(
            "📦 Orders",
            f"{total_orders:,}"
        )

    row2 = st.columns(3)

    with row2[0]:
        st.metric(
            "👥 Customers",
            f"{total_customers:,}"
        )

    with row2[1]:
        st.metric(
            "🛒 Avg Order Value",
            f"₹ {average_order_value:,.0f}"
        )

    with row2[2]:
        st.metric(
            "🎯 Profit Margin",
            f"{profit_margin:.2f}%"
        )

    st.divider()

    # --------------------------------------------------
    # Revenue Trend
    # --------------------------------------------------

    st.subheader("📈 Monthly Revenue Trend")

    monthly_revenue = (
        df.groupby(
            df["Date"].dt.to_period("M")
        )["Revenue"]
        .sum()
        .reset_index()
    )

    monthly_revenue["Date"] = monthly_revenue["Date"].astype(str)

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

    st.divider()

    # --------------------------------------------------
    # Region Performance
    # --------------------------------------------------

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
        title="Revenue by Region",
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # Top Customers
    # --------------------------------------------------

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
        title="Top 10 Customers by Revenue",
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # Product Category Analysis
    # --------------------------------------------------

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
        title="Revenue Contribution by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # Data Preview
    # --------------------------------------------------

    st.subheader("📄 Data Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.write(f"Total Records: {len(df):,}")

else:
    st.info("👆 Upload the AI Business Analyst Excel file to begin analysis.")