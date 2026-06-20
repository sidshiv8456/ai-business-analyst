import streamlit as st


def show_ai_chat(df):

    st.subheader("🤖 AI Business Analyst")

    question = st.text_input(
        "Ask a business question"
    )

    if not question:
        return

    question = question.lower()

    region_sales = (
        df.groupby("Region")["Revenue"]
        .sum()
        .reset_index()
    )

    customer_sales = (
        df.groupby("Customer_Name")["Revenue"]
        .sum()
        .reset_index()
    )

    category_sales = (
        df.groupby("Product_Category")["Revenue"]
        .sum()
        .reset_index()
    )

    # ------------------------
    # Underperforming Region
    # ------------------------

    if (
        "underperforming" in question
        or "worst region" in question
    ):

        worst_region = (
            region_sales
            .sort_values("Revenue")
            .iloc[0]
        )

        st.success(
            f"""
Underperforming Region:
{worst_region['Region']}

Revenue:
₹{worst_region['Revenue']:,.0f}
"""
        )

    # ------------------------
    # Top Region
    # ------------------------

    elif (
        "best region" in question
        or "top region" in question
    ):

        best_region = (
            region_sales
            .sort_values(
                "Revenue",
                ascending=False
            )
            .iloc[0]
        )

        st.success(
            f"""
Best Region:
{best_region['Region']}

Revenue:
₹{best_region['Revenue']:,.0f}
"""
        )

    # ------------------------
    # Top Customer
    # ------------------------

    elif "top customer" in question:

        top_customer = (
            customer_sales
            .sort_values(
                "Revenue",
                ascending=False
            )
            .iloc[0]
        )

        st.success(
            f"""
Top Customer:
{top_customer['Customer_Name']}

Revenue:
₹{top_customer['Revenue']:,.0f}
"""
        )

    # ------------------------
    # Top Category
    # ------------------------

    elif "top category" in question:

        top_category = (
            category_sales
            .sort_values(
                "Revenue",
                ascending=False
            )
            .iloc[0]
        )

        st.success(
            f"""
Top Category:
{top_category['Product_Category']}

Revenue:
₹{top_category['Revenue']:,.0f}
"""
        )

    # ------------------------
    # Business Summary
    # ------------------------

    elif "summary" in question:

        revenue = df["Revenue"].sum()
        profit = df["Profit"].sum()

        st.success(
            f"""
Business Summary

Revenue:
₹{revenue:,.0f}

Profit:
₹{profit:,.0f}

Records:
{len(df)}
"""
        )

    else:

        st.warning(
            """
Try asking:

• Which region is underperforming?

• Which is the best region?

• Show top customer

• Show top category

• Give me summary
"""
        )