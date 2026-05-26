import streamlit as st
import pandas as pd
from query_engine import ask_database

st.set_page_config(page_title="AI Data Analyst", layout="wide")

df = pd.read_csv("data/Sample - Superstore.csv")
st.title("AI Data Analyst")
st.success("Ask business questions and export reports")

st.caption("Natural Language  ->  SQL  ->  Business Insights")

st.markdown("Analyse sales performance interactively")

total_sales = round(df["Sales"].sum())

total_orders = len(df)

total_profit = round(df["Profit"].sum())

col1, col2, col3 = st.columns(3)

col1.metric("Total sales", f"${total_sales}")

col2.metric("Orders", total_orders)

col3.metric("Profit", f"${total_profit}")


st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Choose category", ["ALL"] + list(df["Category"].unique())
)

if category != "ALL":
    filtered_df = df[df["Category"] == category]

else:
    filtered_df = df

st.subheader("Filtered Dataset")
st.dataframe(filtered_df)

st.subheader("Sales by Sub category")

sales = (filtered_df.groupby("Sub-Category")["Sales"].sum())


st.bar_chart(sales)

st.divider()

st.caption("Built using Python • Streamlit • SQLite")

st.header("AI Data Analyst")

question = st.text_input("Ask a business question:")

if st.button("Analyse"):
    answer = ask_database(question)

    st.write(answer)

    try:
        if hasattr(answer, "shape"):
            if answer.shape[1] > 1:
                st.bar_chart(answer.set_index(
                    answer.columns[0]
                ))

    except:
        pass

    
    if hasattr(answer, "to_csv"):
        csv = answer.to_csv(index=False)

        st.download_button("Download Report", csv, "report.csv", "text/csv")

