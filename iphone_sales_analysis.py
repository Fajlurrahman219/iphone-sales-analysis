# iphone_sales_analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.title("📱 iPhone Sales Analysis Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("apple_products.csv")
    return df

df = load_data()

# Show the dataset
st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

# Basic stats
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Price vs Rating plot
st.subheader("💸 Price vs Rating")
fig1 = px.scatter(df, x="price", y="rating", color="category", hover_data=["product_name"])
st.plotly_chart(fig1)

# Top Rated iPhones
st.subheader("🌟 Top Rated iPhones")
top_rated = df.sort_values(by="rating", ascending=False).drop_duplicates('product_name').head(5)
st.dataframe(top_rated[['product_name', 'price', 'rating', 'category']])

# Average rating by category
st.subheader("📈 Average Rating by Category")
avg_rating = df.groupby("category")["rating"].mean().reset_index().sort_values(by="rating", ascending=False)
fig2 = px.bar(avg_rating, x="category", y="rating", text_auto=True)
st.plotly_chart(fig2)

# Footer
st.markdown("---")
st.caption("Built with Streamlit | Data: apple_products.csv")
