import streamlit as st
import pandas as pd


def apply_filters(df):

    st.sidebar.header("🔍 Filters")

    regions = sorted(
        df["Region"].unique()
    )

    selected_regions = st.sidebar.multiselect(
        "Region",
        regions,
        default=regions
    )

    categories = sorted(
        df["Product_Category"].unique()
    )

    selected_categories = st.sidebar.multiselect(
        "Product Category",
        categories,
        default=categories
    )

    min_date = df["Date"].min()
    max_date = df["Date"].max()

    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date)
    )

    filtered_df = df.copy()

    filtered_df = filtered_df[
        filtered_df["Region"].isin(
            selected_regions
        )
    ]

    filtered_df = filtered_df[
        filtered_df["Product_Category"].isin(
            selected_categories
        )
    ]

    if len(date_range) == 2:

        start_date, end_date = date_range

        filtered_df = filtered_df[
            (
                filtered_df["Date"]
                >= pd.to_datetime(start_date)
            )
            &
            (
                filtered_df["Date"]
                <= pd.to_datetime(end_date)
            )
        ]

    return filtered_df