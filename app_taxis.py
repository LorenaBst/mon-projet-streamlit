import pandas as pd
import streamlit as st 

taxis = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")

st.title("Dashboard Analyse Taxis - Loréna")

choix_quartier = st.selectbox("Choisissez le quartier de prise en charge", taxis["pickup_borough"].dropna().unique())
taxis_arr = taxis[taxis["pickup_borough"]== choix_quartier]

st.dataframe(taxis_arr.head(5))
st.metric(label ="Nombre total de courses dans cet arrondissement", value = len(taxis_arr))
