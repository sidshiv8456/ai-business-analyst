import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Business Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Analyst")

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

# --------------------------------------------------
# MAIN APP
# --------------------------------------------------

if uploaded_file:

    # Load Data
    filtered_df = pd.read_excel(
        uploaded_file,
        sheet_name="Sales_Data"
    )

    filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])
    # --------------------------------------------------
    # SIDEBAR FILTERS
    # --------------------------------------------------

    st.sidebar.header("🔍 Filters")

    regions = sorted(filtered_df["Region"].unique())

    selected_regions = st.sidebar.multiselect(
        "Select Region",
        options=regions,
        default=regions
    )


    categories = sorted(
    filtered_df["Product_Category"].unique()
    )

    selected_categories = st.sidebar.multiselect(
        "Select Product Category",
        options=categories,
        default=categories
    )


    min_date = filtered_df["Date"].min()
    max_date = filtered_df["Date"].max()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date)
    )


    filtered_filtered_df = filtered_df.copy()

    filtered_filtered_df = filtered_filtered_df[
    filtered_filtered_df["Region"].isin(
        selected_regions
    )
    ]

    filtered_filtered_df = filtered_filtered_df[
    filtered_filtered_df["Product_Category"].isin(
        selected_categories
    )
    ]

    if len(date_range) == 2:

         start_date, end_date = date_range

    filtered_filtered_df = filtered_filtered_df[
        (
            filtered_filtered_df["Date"]
            >= pd.to_datetime(start_date)
        )
        &
        (
            filtered_filtered_df["Date"]
            <= pd.to_datetime(end_date)
        )
    ]

    st.info(
    f"Showing {len(filtered_filtered_df):,} records "
    f"out of {len(filtered_df):,}"
    )


    if filtered_df.empty:

     st.warning(
        "No data available for selected filters."
    )

    st.stop()
    # --------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------

    total_revenue = filtered_filtered_df["Revenue"].sum()

    total_profit = filtered_df["Profit"].sum()

    total_orders = filtered_filtered_df["Order_ID"].nunique()

    total_customers = filtered_filtered_df["Customer_ID"].nunique()

    average_order_value = total_revenue / total_orders

    average_profit_per_order = total_profit / total_orders

    profit_margin = (
        total_profit / total_revenue
    ) * 100

    # --------------------------------------------------
    # KPI DASHBOARD
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
    # REVENUE TREND
    # --------------------------------------------------

    st.subheader("📈 Monthly Revenue Trend")

    monthly_revenue = (
        filtered_filtered_df.groupby(
            filtered_filtered_df["Date"].dt.to_period("M")
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

    st.divider()

    # --------------------------------------------------
    # REGION PERFORMANCE
    # --------------------------------------------------

    st.subheader("🌍 Region Performance")

    region_sales = (
        filtered_df.groupby("Region")["Revenue"]
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

    st.divider()

    # --------------------------------------------------
    # TOP CUSTOMERS
    # --------------------------------------------------

    st.subheader("🏆 Top 10 Customers")

    top_customers = (
        filtered_df.groupby("Customer_Name")["Revenue"]
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

    st.divider()

    # --------------------------------------------------
    # PRODUCT CATEGORY ANALYSIS
    # --------------------------------------------------

    st.subheader("📦 Revenue by Product Category")

    category_sales = (
        filtered_df.groupby("Product_Category")["Revenue"]
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

    st.divider()

    # --------------------------------------------------
    # AI BUSINESS ANALYST
    # --------------------------------------------------

    st.subheader("🤖 AI Business Analyst")

    question = st.text_input(
        "Ask a business question"
    )

    if question:

        question = question.lower()

        customer_sales = (
            filtered_df.groupby("Customer_Name")["Revenue"]
            .sum()
            .reset_index()
        )

        if "underperforming" in question or "region" in question:

            worst_region = (
                region_sales
                .sort_values("Revenue")
                .iloc[0]
            )

            st.success(
                f"""
Underperforming Region: {worst_region['Region']}

Revenue: ₹{worst_region['Revenue']:,.0f}
"""
            )

        elif "top customer" in question:

            best_customer = (
                customer_sales
                .sort_values(
                    by="Revenue",
                    ascending=False
                )
                .iloc[0]
            )

            st.success(
                f"""
Top Customer: {best_customer['Customer_Name']}

Revenue: ₹{best_customer['Revenue']:,.0f}
"""
            )

        elif "summary" in question or "summarize" in question:

            st.success(
                f"""
Revenue: ₹{total_revenue:,.0f}

Profit: ₹{total_profit:,.0f}

Orders: {total_orders:,}

Customers: {total_customers:,}

Profit Margin: {profit_margin:.2f}%
"""
            )

        else:

            st.warning(
                """
Try asking:

• Which region is underperforming?

• Show top customer

• Summarize business
"""
            )

    st.divider()

    # --------------------------------------------------
    # DATA PREVIEW
    # --------------------------------------------------

    st.subheader("📄 Data Preview")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.write(
        f"Total Records: {len(filtered_df):,}"
    )

else:

    st.info(
        "👆 Upload the AI Business Analyst dataset to begin."
    )