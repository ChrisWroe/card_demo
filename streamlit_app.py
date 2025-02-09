import streamlit as st
import pandas as pd

st.title("🎈 My Tarrot app")
st.write(
    "Tarrot"
)

def load_data():
    data = pd.read_csv("data/cards.csv")
    return data

data=load_data()

st.subheader('Raw data')
st.write(data)