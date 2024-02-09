import streamlit as st
import pandas as pd
import sqlite3

#Setup data by executing a SQL query
query = 'SELECT * FROM TrainingDataset'

#Connect to the SQLITE database
with sqlite3.connect('olist.db') as conn:
    df = pd.read_sql_query(query, conn)
    
conn.close()

# background_image_style = """
#     <style>
#         body {
#             background-image: url('img.png');
#             background-size: cover;
#         }
#     </style>
# """



# Make page

st.set_page_config(page_title="Olist")
st.header("Olist Machine Learning Project")
st.markdown("Deployment of the Olist dataset machine learning model using RandomForestClassifier.")
st.markdown("Use this dashboard to understand the data provided on the Olist Dataframe and to make predictions.")
st.markdown("")
st.markdown("img.png")
