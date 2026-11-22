import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Initialisation de la session
if "logged_in" not in st.session_state : 
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

@st.cache_data
def load_accounts():
    return pd.read_csv("accounts.csv")
def authenticate(username_input, password_input):
    accounts_df = load_accounts()
    user_match = accounts_df[(accounts_df["name"] == username_input) & (accounts_df["password"] == password_input)]
    return not user_match.empty

# PAGE DE CONNEXION (si l'utilisateur n'est pas connecté)
if not st.session_state["logged_in"]:
    st.title(" Connexion à l'Application Data")
    st.subheader("Veuillez vous identifier pour accéder au contenu")
    username_input = st.text_input("Nom d'utilisateur")
    password_input = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        if authenticate(username_input, password_input):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username_input
            st.success(f"Bienvenue {username_input} !")
            st.rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

# PARTIE SÉCURISÉE (Accessible UNIQUEMENT une fois connecté)
else:
    with st.sidebar:
        st.write(f" Bienvenue, **{st.session_state['username']}**!")
        if st.button("Se déconnecter"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.rerun()
        st.divider()
        selected_page = option_menu(
            menu_title="Menu principal",
            options=["Accueil", "Galerie Photos"],
            icons=["house", "images"],
            default_index=0
        )

    if selected_page == "Accueil":
        st.title(" Page d'Accueil Réservée")
    elif selected_page == "Galerie Photos":
        st.title("Album Photos")
        cols = st.columns(3)
        sample_images = [
            "images/tigre1.jpg",
            "images/tigre2.jpg",
            "images/tigre3.jpg"
            ]
        for idx, img_url in enumerate(sample_images):
            with cols[idx % 3]:
                st.image(img_url, width="stretch")

