import streamlit as st
import pandas as pd
df = pd.read_csv("orders.csv")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.vecteezy.com/system/resources/previews/034/795/660/non_2x/global-logistics-network-connection-background-concept-with-big-data-visualization-cloud-computing-and-transportation-illustration-eps10-free-vector.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Production and Transportation Scheduling")

option = st.selectbox(
   "Select order_ID:",options = [" "]+list(df["Order_ID"])
)

if st.button("Submit"):
    st.image('graph.jpeg', caption='Network of Plants and Ports')
    a,b,c,d = df.loc[df['Order_ID'] == option]["decision"].values[0].split(',')
    st.write(f'Minimum cost for the order: {round(float(a[1:]), 3)}')
    st.write(f'Best plant for processing the order: {b}')
    st.write(f'Best port to sent the order from: {d[:-1]}')
    st.write(f'Best port price: {round(float(c), 3)}')
