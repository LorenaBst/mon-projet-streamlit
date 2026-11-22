
import streamlit as st
import pandas as pd

st.title("Mon Premier Dashboard Streamlit 🚀")
st.write("Bienvenue sur cette application interactive dédiée à l'analyse de données.")

st.markdown("On peut utiliser le **gras**, l' *italique* et du :rainbow:[texte en couleur].")

afficher_details = st.checkbox("Afficher plus d'informations")
if afficher_details:
    st.info("Voici des détails supplémentaires affichés dynamiquement.")
