import streamlit as st
import numpy as np
from make_pred import make_prediction
import json
import pandas as pd
import plotly.express as px
import requests
import sqlite3


#order_delivered_customer_date,order_delivered_carrier_date,
# order_estimated_delivery_date,temps_livraison,retard_livraison,
#review_id,order_id,review_score,review_comment_title
# review_comment_message,review_creation_date,
# review_answer_timestamp,customer_id,order_status,order_purchase_timestamp,
# order_approved_at,order_delivered_carrier_date,order_delivered_customer_date,
# order_estimated_delivery_date,score,temps_livraison,retard_livraison,produit_recu



query = 'SELECT * FROM TrainingDataset'

# Setup data
with sqlite3.connect('olist.db') as conn:
    df = pd.read_sql_query(query, conn)

df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
# Setup title page
st.set_page_config(page_title="Prediction")
st.header("Prediction - Iris Dataset")
st.markdown("Utilize the RandomForestClassifier to make predictions for the classification of review score."
            "The predictions will be displayed on the graphs below to intuitively understand how they were made.")
st.sidebar.header("Make PredictionM")

t_l = st.sidebar.text_input("temps_livraison")
r_l = st.sidebar.text_input("retard_livraison")
make_pred_API = st.sidebar.button("Predict")

# # Affichage de scatterplot
df1 = df.loc[df['order_delivered_customer_date'] < df['order_estimated_delivery_date']]
plot1 = px.scatter(
    df,
    x="temps_livraison",
    y="retard_livraison",
    title="Orders delivered later than initial Estimated Delivery Time",
    color='score',
    color_continuous_scale='Viridis',
    size_max=10)

df2 = df.loc[df['order_delivered_customer_date'] >= df['order_estimated_delivery_date']]
plot2 = px.scatter(
    df,
    x="temps_livraison",
    y="retard_livraison",
    title="Orders delivered later than initial Estimated Delivery Time",
    color='score',
    color_continuous_scale='Viridis',
    size_max=10)


score_pred = None

# Launch prediction with API
if make_pred_API:
#     # Construire l'URL avec les paramètres
    url = f"http://localhost:8000/{(t_l)}/{(r_l)}"

#     # Envoyer la requête à FastAPI
    response = requests.get(url)

#     # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        score_pred = response.json().get("prediction", "Default Value")
        st.success(f"Prediction result: {score_pred} ")
    else:
        st.error("Error in prediction request.")

#     # Transformer mes x1/x2/x3/x4 en df
    p1 = [float(t_l), float(r_l)]
    x = np.array([p1])
    row = {"temps_livraison": [float(t_l)],
           "retard_livraison": [float(r_l)]
           }


    p1_df = pd.DataFrame(row)

    plot1.add_scatter(x=p1_df["temps_livraison"], 
                      y=p1_df["retard_livraison"],
                      mode='markers',  
                      name=score_pred,  
                      marker=dict(
                            color='red',  # Couleur des points
                            size=10,  # Taille des points
                            symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
                            line=dict(
                                color='white',  # Couleur de la bordure des points
                                width=2  # Largeur de la bordure des points
                            )
                      ))
    

    
st.plotly_chart(plot1)


























# Managing input data
# p1 = ["", "", "", ""]

# plot1 = px.scatter(
#     df,
#     x="petal_length",
#     y="petal_width",
#     title="Petal Length vs Petal Width",
#     color="species")

# plot2 = px.scatter(
#     df,
#     x="sepal_length",
#     y="petal_length",
#     title="Sepal Length vs Petal Length",
#     color="species")

# # Launch prediction with API
# if make_pred_API:
#     # Construire l'URL avec les paramètres
#     url = f"http://localhost:8000/{float(sep_len)}/{float(sep_wid)}/{float(pet_len)}/{float(pet_wid)}"

#     # Envoyer la requête à FastAPI
#     response = requests.get(url)

#     # Vérifier si la requête a réussi (statut 200)
#     if response.status_code == 200:
#         species_pred = response.json()["prediction"]
#         st.success(f"Prediction result: {species_pred}")
#     else:
#         st.error("Error in prediction request.")

#     p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
#     row = {"sepal_length": [float(sep_len)],
#            "sepal_width": [float(sep_wid)],
#            "petal_length": [float(pet_len)],
#            "petal_width": [float(pet_wid)]}
#     p1_df = pd.DataFrame(row)

#     st.subheader(f"Predicted Species: {species_pred}")
#     plot1.add_scatter(x=p1_df["petal_length"], 
#                       y=p1_df["petal_width"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#                       ))
#     plot2.add_scatter(x=p1_df["sepal_length"], 
#                       y=p1_df["petal_length"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#     ))

# # Making a prediction and displaying data
# if make_pred:
#     p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
#     x = np.array([p1])
#     row = {"sepal_length": [float(sep_len)],
#            "sepal_width": [float(sep_wid)],
#            "petal_length": [float(pet_len)],
#            "petal_width": [float(pet_wid)]}

#     p1_df = pd.DataFrame(row)
#     species_pred = make_prediction(x)

#     st.subheader(f"Predicted Species: {species_pred}")
#     plot1.add_scatter(x=p1_df["petal_length"], 
#                       y=p1_df["petal_width"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#                       ))
#     plot2.add_scatter(x=p1_df["sepal_length"], 
#                       y=p1_df["petal_length"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#     ))

# st.plotly_chart(plot1)
# st.plotly_chart(plot2)

# print('toto4')

# #5.2/2.7/3.9/1.4