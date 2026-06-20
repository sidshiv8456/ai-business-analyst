import streamlit as st
import pandas as pd


def show_target_analysis(sales_df, uploaded_file):

    try:

        targets_df = pd.read_excel(
            uploaded_file,
            sheet_name="Targets"
        )

        # Clean column names
        targets_df.columns = (
            targets_df.columns
            .str.strip()
            .str.replace(" ", "_")
        )

        # Force second column to Revenue_Target
        if len(targets_df.columns) >= 2:

            targets_df = targets_df.rename(
                columns={
                    targets_df.columns[1]:
                    "Revenue_Target"
                }
            )

        actual_revenue = (
            sales_df.groupby("Region")["Revenue"]
            .sum()
            .reset_index()
        )

        comparison = actual_revenue.merge(
            targets_df,
            on="Region"
        )

        comparison["Variance"] = (
            comparison["Revenue"]
            - comparison["Revenue_Target"]
        )

        comparison["Variance_Percent"] = (
            comparison["Variance"]
            / comparison["Revenue_Target"]
        ) * 100

        st.subheader(
            "🎯 Target vs Actual Analysis"
        )

        st.dataframe(
            comparison,
            use_container_width=True
        )

        best_region = (
            comparison
            .sort_values(
                "Variance_Percent",
                ascending=False
            )
            .iloc[0]
        )

        worst_region = (
            comparison
            .sort_values(
                "Variance_Percent"
            )
            .iloc[0]
        )

        st.success(
            f"""
⭐ Best Performer

{best_region['Region']}

Exceeded target by
{best_region['Variance_Percent']:.1f}%
"""
        )

        st.error(
            f"""
🚨 Needs Attention

{worst_region['Region']}

Missed target by
{abs(worst_region['Variance_Percent']):.1f}%
"""
        )

    except Exception as e:

        st.error(
            f"Target Analysis Error: {e}"
        )