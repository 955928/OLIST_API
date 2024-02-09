import streamlit as st
import requests

# Setup title page
st.set_page_config(page_title="Training")
st.header("Prediction - Olist Dataset")
st.markdown("Train the model to make predictions for classification.")
st.sidebar.header("Train model")

launch_training = st.sidebar.button("Training")

if launch_training:
    url = f"http://localhost:8000/train_model"

    # Envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        response = response.json()["Response"]
        st.success(f"Model training message: {response}")
    else:
        st.error("Error in training request.")

else:
# Welcome message
# # print('Welcome message')
    url = f"http://127.0.0.1:8000/infos"

    # Envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        message = response.json()["message"]
        st.success(f"API welcome message: {message}")
    else:
        st.error("Error in welcome request.")