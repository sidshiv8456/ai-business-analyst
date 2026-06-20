def calculate_kpis(df):

    total_revenue = df["Revenue"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order_ID"].nunique()

    total_customers = df["Customer_ID"].nunique()

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else 0
    )

    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue > 0
        else 0
    )

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "average_order_value": average_order_value,
        "profit_margin": profit_margin
    }