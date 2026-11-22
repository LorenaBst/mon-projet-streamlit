import pandas as pd
import streamlit as st

@st.cache_data
def get_dataset():
    flights = pd.read_csv("flights.csv")
    return flights
flights = get_dataset()

st.title("Voici des données sur les vols")


st.subheader("Aperçu selon les dates")

annee_mini = int(flights["year"].min())
annee_maxi = int(flights["year"].max())

plage_annees = st.slider(
    "Sélectionnez une plage d'années",
    min_value = annee_mini, 
    max_value = annee_maxi,
    value = (annee_mini, annee_maxi)
    )
flights_filtres= flights[(flights["year"]>=plage_annees[0]) & (flights["year"]<= plage_annees[1])]

liste_mois = ["Tous"] + list(flights["month"].unique())
choix_mois = st.selectbox("Choisissez le mois", options=liste_mois)
if choix_mois != "Tous" : 
    flights_filtres = flights_filtres[flights_filtres["month"] == choix_mois]

nb_passagers = flights_filtres["passengers"].sum()
st.metric(label = "Nombre de passagers sur la période", value =nb_passagers)

flights_filtres["Date complete"] = pd.to_datetime(flights_filtres["year"].astype(str) + " " + flights_filtres["month"].astype(str) + " 1")

st.line_chart(data= flights_filtres, x="Date complete", y = "passengers")

import matplotlib.pyplot as plt
import seaborn as sns

afficher_heatmap = st.checkbox("Afficher la Heatmap")

if afficher_heatmap : 
    donnees_pivot = flights_filtres.pivot(index="month", columns="year", values="passengers") #on fzit un tableau croisé acec les year month et passengers
    fig, ax = plt.subplots(figsize = (8,4))
    sns.heatmap(donnees_pivot, annot = True, cmap= "pink_r", fmt = ".0f", ax = ax)
    ax.set(title= "Répartition des passagers")
    plt.show()
    st.pyplot(fig)




