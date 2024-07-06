import streamlit as st
import pandas as pd
df = pd.read_csv("orders.csv")

st.title("Production and Transportation Scheduling")

option = st.selectbox(
   "Select order_ID:",options = [" "]+list(df["Order_ID"])
)

if st.button("Submit"):
    st.image('graph.jpeg', caption='Network of Plants and Ports')
    a,b,c,d = df.loc[df['Order_ID'] == option]["decision"].values[0].split(',')
    st.write(f'Minimum cost for the order: {a[1:]}')
    st.write(f'Best plant for processing the order: {b}')
    st.write(f'Best port to sent the order from: {d[:-1]}')
    st.write(f'Best port price: {c}')
