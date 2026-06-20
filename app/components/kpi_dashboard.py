import streamlit as st


def show_kpis(kpis):

    st.subheader("📌 Business KPIs")

    row1 = st.columns(3)

    with row1[0]:
        st.metric(
            "💰 Revenue",
            f"₹ {kpis['total_revenue']:,.0f}"
        )

    with row1[1]:
        st.metric(
            "📈 Profit",
            f"₹ {kpis['total_profit']:,.0f}"
        )

    with row1[2]:
        st.metric(
            "📦 Orders",
            f"{kpis['total_orders']:,}"
        )

    row2 = st.columns(3)

    with row2[0]:
        st.metric(
            "👥 Customers",
            f"{kpis['total_customers']:,}"
        )

    with row2[1]:
        st.metric(
            "🛒 Avg Order Value",
            f"₹ {kpis['average_order_value']:,.0f}"
        )

    with row2[2]:
        st.metric(
            "🎯 Profit Margin",
            f"{kpis['profit_margin']:.2f}%"
        )