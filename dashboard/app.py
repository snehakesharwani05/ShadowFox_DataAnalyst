import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Food Delivery Analytics",
    page_icon="🍔",
    layout="wide"
)



# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(
    "data/cleaned/food_delivery_cleaned.csv"
)

df["Order Date"] = pd.to_datetime(df["Order Date"])


# -----------------------------
# SIDEBAR FILTERS
# -----------------------------

st.sidebar.header("🔎 Filters")

status_options = df["Order Status"].dropna().unique().tolist()

selected_status = st.sidebar.multiselect(
    "Order Status",
    options=status_options,
    default=status_options
)

payment_options = df["Payment Method"].dropna().unique().tolist()

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    options=payment_options,
    default=payment_options
)

city_options = sorted(
    df["city"].dropna().unique().tolist()
)

selected_city = st.sidebar.selectbox(
    "City",
    options=["All"] + city_options
)


# -----------------------------
# APPLY FILTERS
# -----------------------------

filtered_df = df[
    df["Order Status"].isin(selected_status) &
    df["Payment Method"].isin(selected_payment)
]

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["city"] == selected_city
    ]


# -----------------------------
# TITLE
# -----------------------------

st.title("🍔 Food Delivery Analytics Dashboard")

st.markdown(
    "Interactive analysis of food delivery orders, revenue, "
    "delivery performance and customer behaviour."
)


# -----------------------------
# KPI CALCULATIONS
# -----------------------------

total_orders = filtered_df["Order ID"].nunique()

total_revenue = filtered_df.loc[
    filtered_df["Order Status"] == "Delivered",
    "Order Amount (INR)"
].sum()

avg_order_value = filtered_df["Order Amount (INR)"].mean()

avg_delivery_time = filtered_df["Delivery Time (mins)"].mean()

avg_rating = filtered_df["Rating"].mean()

cancelled_orders = (
    filtered_df["Order Status"] == "Cancelled"
).sum()


# -----------------------------
# KPI CARDS
# -----------------------------

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col2.metric(
    "Total Revenue",
    f"₹{total_revenue:,.0f}"
)

col3.metric(
    "Avg Order Value",
    f"₹{avg_order_value:,.0f}"
)

col4.metric(
    "Avg Delivery Time",
    f"{avg_delivery_time:.1f} min"
)

col5.metric(
    "Avg Rating",
    f"{avg_rating:.2f}"
)

col6.metric(
    "Cancelled Orders",
    f"{cancelled_orders:,}"
)


st.divider()


# -----------------------------
# MONTHLY REVENUE
# -----------------------------

monthly = (
    filtered_df
    .groupby(
        filtered_df["Order Date"].dt.to_period("M")
    )
    .agg(
        Revenue=("Order Amount (INR)", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

monthly["Order Date"] = monthly["Order Date"].astype(str)


fig_monthly = px.line(
    monthly,
    x="Order Date",
    y="Revenue",
    markers=True,
    title="Monthly Revenue"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)


# -----------------------------
# ORDER STATUS
# -----------------------------

status = (
    filtered_df["Order Status"]
    .value_counts()
    .reset_index()
)

status.columns = [
    "Order Status",
    "Orders"
]


fig_status = px.pie(
    status,
    names="Order Status",
    values="Orders",
    title="Order Status Distribution"
)

st.plotly_chart(
    fig_status,
    use_container_width=True
)

# -----------------------------
# DELIVERY PERFORMANCE
# -----------------------------

st.subheader("🚚 Delivery Performance")

delivery_analysis = (
    filtered_df.groupby("city")
    .agg(
        Avg_Delivery_Time=("Delivery Time (mins)", "mean"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

delivery_analysis["Avg_Delivery_Time"] = (
    delivery_analysis["Avg_Delivery_Time"].round(1)
)

fig_delivery = px.bar(
    delivery_analysis.sort_values(
        "Avg_Delivery_Time",
        ascending=False
    ),
    x="city",
    y="Avg_Delivery_Time",
    title="Average Delivery Time by City",
    labels={
        "city": "City",
        "Avg_Delivery_Time": "Average Delivery Time (mins)"
    }
)

st.plotly_chart(
    fig_delivery,
    use_container_width=True
)

# -----------------------------
# PAYMENT METHOD ANALYSIS
# -----------------------------

st.subheader("💳 Revenue by Payment Method")

payment_analysis = (
    filtered_df.groupby("Payment Method")
    .agg(
        Revenue=("Order Amount (INR)", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

fig_payment = px.bar(
    payment_analysis.sort_values(
        "Revenue",
        ascending=False
    ),
    x="Payment Method",
    y="Revenue",
    title="Revenue by Payment Method",
    labels={
        "Payment Method": "Payment Method",
        "Revenue": "Revenue (INR)"
    },
    text_auto=".2s"
)

st.plotly_chart(
    fig_payment,
    use_container_width=True
)

# -----------------------------
# RESTAURANT PERFORMANCE
# -----------------------------

st.subheader("🍽️ Top Restaurants")

restaurant_analysis = (
    filtered_df.groupby("name")
    .agg(
        Revenue=("Order Amount (INR)", "sum"),
        Orders=("Order ID", "nunique"),
        Avg_Order_Value=("Order Amount (INR)", "mean")
    )
    .reset_index()
)

restaurant_analysis["Avg_Order_Value"] = (
    restaurant_analysis["Avg_Order_Value"].round(0)
)

top_restaurants = (
    restaurant_analysis
    .sort_values("Revenue", ascending=False)
    .head(10)
)

fig_restaurants = px.bar(
    top_restaurants,
    x="Revenue",
    y="name",
    orientation="h",
    title="Top 10 Restaurants by Revenue",
    labels={
        "name": "Restaurant",
        "Revenue": "Revenue (INR)"
    },
    text_auto=".2s"
)

fig_restaurants.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig_restaurants,
    use_container_width=True
)

# -----------------------------
# ORDER BEHAVIOUR ANALYSIS
# -----------------------------

st.subheader("🛒 Order Behaviour")

order_behavior = (
    filtered_df.groupby("Number of Items")
    .agg(
        Orders=("Order ID", "nunique"),
        Avg_Order_Value=("Order Amount (INR)", "mean"),
        Avg_Rating=("Rating", "mean")
    )
    .reset_index()
)

fig_order_behavior = px.bar(
    order_behavior,
    x="Number of Items",
    y="Avg_Order_Value",
    title="Average Order Value by Number of Items",
    labels={
        "Number of Items": "Number of Items",
        "Avg_Order_Value": "Average Order Value (INR)"
    },
    text_auto=".0f"
)

st.plotly_chart(
    fig_order_behavior,
    use_container_width=True
)

# -----------------------------
# ORDER VALUE DISTRIBUTION
# -----------------------------

fig_order_value = px.histogram(
    filtered_df,
    x="Order Amount (INR)",
    nbins=30,
    title="Order Value Distribution",
    labels={
        "Order Amount (INR)": "Order Amount (INR)"
    }
)

st.plotly_chart(
    fig_order_value,
    use_container_width=True
)

# -----------------------------
# CANCELLATION & RISK ANALYSIS
# -----------------------------

st.subheader("❌ Cancellation & Delivery Risk")


# Create delivery-time groups
risk_df = filtered_df.copy()

risk_df["Delivery_Time_Group"] = pd.cut(
    risk_df["Delivery Time (mins)"],
    bins=[0, 30, 45, 60, 90, float("inf")],
    labels=[
        "Under 30 mins",
        "30–45 mins",
        "45–60 mins",
        "60–90 mins",
        "90+ mins"
    ]
)


# Calculate cancellation rate
risk_analysis = (
    risk_df.assign(
        Cancelled=risk_df["Order Status"].eq("Cancelled").astype(int)
    )
    .groupby("Delivery_Time_Group", observed=False)
    .agg(
        Total_Orders=("Order ID", "nunique"),
        Cancelled_Orders=("Cancelled", "sum")
    )
    .reset_index()
)

risk_analysis["Cancellation_Rate"] = (
    risk_analysis["Cancelled_Orders"]
    / risk_analysis["Total_Orders"]
    * 100
)


# Cancellation rate chart
fig_risk = px.bar(
    risk_analysis,
    x="Delivery_Time_Group",
    y="Cancellation_Rate",
    title="Cancellation Rate by Delivery Time",
    labels={
        "Delivery_Time_Group": "Delivery Time",
        "Cancellation_Rate": "Cancellation Rate (%)"
    },
    text_auto=".1f"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)

# -----------------------------
# CITY CANCELLATION ANALYSIS
# -----------------------------

city_risk = (
    filtered_df.assign(
        Cancelled=filtered_df["Order Status"].eq("Cancelled").astype(int)
    )
    .groupby("city")
    .agg(
        Total_Orders=("Order ID", "nunique"),
        Cancelled_Orders=("Cancelled", "sum")
    )
    .reset_index()
)

city_risk["Cancellation_Rate"] = (
    city_risk["Cancelled_Orders"]
    / city_risk["Total_Orders"]
    * 100
)


# Only show cities with at least 50 orders
city_risk = city_risk[
    city_risk["Total_Orders"] >= 50
].sort_values(
    "Cancellation_Rate",
    ascending=False
).head(10)


fig_city_risk = px.bar(
    city_risk,
    x="Cancellation_Rate",
    y="city",
    orientation="h",
    title="Top Cities by Cancellation Rate",
    labels={
        "city": "City",
        "Cancellation_Rate": "Cancellation Rate (%)"
    },
    text_auto=".1f"
)

fig_city_risk.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig_city_risk,
    use_container_width=True
)

# -----------------------------
# PROMOTION ANALYSIS
# -----------------------------

st.subheader("🎟️ Promotion & Free Delivery Analysis")

promo_analysis = (
    filtered_df.groupby("Promo Code Applied")
    .agg(
        Orders=("Order ID", "nunique"),
        Revenue=("Order Amount (INR)", "sum"),
        Avg_Order_Value=("Order Amount (INR)", "mean"),
        Avg_Items=("Number of Items", "mean")
    )
    .reset_index()
)

fig_promo = px.bar(
    promo_analysis,
    x="Promo Code Applied",
    y="Avg_Order_Value",
    title="Average Order Value: Promo vs Non-Promo",
    labels={
        "Promo Code Applied": "Promo Code Applied",
        "Avg_Order_Value": "Average Order Value (INR)"
    },
    text_auto=".0f"
)

st.plotly_chart(
    fig_promo,
    use_container_width=True
)

# -----------------------------
# FREE DELIVERY ANALYSIS
# -----------------------------

free_delivery_analysis = (
    filtered_df.groupby("Has Free Delivery")
    .agg(
        Orders=("Order ID", "nunique"),
        Revenue=("Order Amount (INR)", "sum"),
        Avg_Order_Value=("Order Amount (INR)", "mean"),
        Avg_Items=("Number of Items", "mean")
    )
    .reset_index()
)

fig_free_delivery = px.bar(
    free_delivery_analysis,
    x="Has Free Delivery",
    y="Avg_Order_Value",
    title="Average Order Value: Free Delivery vs Paid Delivery",
    labels={
        "Has Free Delivery": "Free Delivery",
        "Avg_Order_Value": "Average Order Value (INR)"
    },
    text_auto=".0f"
)

st.plotly_chart(
    fig_free_delivery,
    use_container_width=True
)

# -----------------------------
# PROMOTION CANCELLATION RATE
# -----------------------------

promo_cancellation = (
    filtered_df.assign(
        Cancelled=filtered_df["Order Status"].eq("Cancelled").astype(int)
    )
    .groupby("Promo Code Applied")
    .agg(
        Total_Orders=("Order ID", "nunique"),
        Cancelled_Orders=("Cancelled", "sum")
    )
    .reset_index()
)

promo_cancellation["Cancellation_Rate"] = (
    promo_cancellation["Cancelled_Orders"]
    / promo_cancellation["Total_Orders"]
    * 100
)

fig_promo_cancel = px.bar(
    promo_cancellation,
    x="Promo Code Applied",
    y="Cancellation_Rate",
    title="Cancellation Rate: Promo vs Non-Promo",
    labels={
        "Promo Code Applied": "Promo Code Applied",
        "Cancellation_Rate": "Cancellation Rate (%)"
    },
    text_auto=".1f"
)

st.plotly_chart(
    fig_promo_cancel,
    use_container_width=True
)

# -----------------------------
# EXECUTIVE SUMMARY
# -----------------------------

st.subheader("📌 Executive Summary")

if len(filtered_df) > 0:

    # Basic metrics
    delivered_orders = (
        filtered_df["Order Status"] == "Delivered"
    ).sum()

    cancelled_orders_count = (
        filtered_df["Order Status"] == "Cancelled"
    ).sum()

    cancellation_rate = (
        cancelled_orders_count
        / len(filtered_df)
        * 100
    )

    avg_delivery = filtered_df[
        "Delivery Time (mins)"
    ].mean()

    avg_order = filtered_df[
        "Order Amount (INR)"
    ].mean()

    # Best performing restaurant
    top_restaurant = (
        filtered_df.groupby("name")["Order Amount (INR)"]
        .sum()
        .idxmax()
    )

    # Best payment method
    top_payment = (
        filtered_df.groupby("Payment Method")[
            "Order Amount (INR)"
        ]
        .sum()
        .idxmax()
    )

    # Highest revenue city
    top_city = (
        filtered_df.groupby("city")[
            "Order Amount (INR)"
        ]
        .sum()
        .idxmax()
    )

    # Display insights
    st.markdown(
        f"""
        ### 🔎 Key Business Insights

        - **Total orders analysed:** {len(filtered_df):,}

        - **Average order value:** ₹{avg_order:,.0f}

        - **Average delivery time:** {avg_delivery:.1f} minutes

        - **Cancellation rate:** {cancellation_rate:.1f}%

        - **Top revenue-generating restaurant:** 
          **{top_restaurant}**

        - **Top revenue-generating city:** 
          **{top_city}**

        - **Highest revenue payment method:** 
          **{top_payment}**
        """
    )

else:

    st.warning(
        "No orders match the selected filters."
    )

# -----------------------------
# BUSINESS RECOMMENDATIONS
# -----------------------------

st.subheader("💡 Business Recommendations")

recommendations = []

if cancellation_rate > 30:
    recommendations.append(
        "⚠️ Cancellation rate is relatively high. "
        "Investigate delivery delays, restaurant preparation "
        "time and order allocation."
    )

if avg_delivery > 45:
    recommendations.append(
        "🚚 Average delivery time is above 45 minutes. "
        "Consider improving route allocation and delivery "
        "agent availability during peak periods."
    )

if avg_order < 1000:
    recommendations.append(
        "🛒 Average order value is relatively low. "
        "Consider bundled meals, add-on recommendations "
        "and minimum-order incentives."
    )

if not recommendations:
    recommendations.append(
        "✅ Current performance indicators do not show "
        "a major issue based on the selected filters."
    )

for recommendation in recommendations:
    st.info(recommendation)