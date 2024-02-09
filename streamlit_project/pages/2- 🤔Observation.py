import streamlit as st
import pandas as pd
import plotly.express as px
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


st.set_page_config(page_title="Olist Dataset")
st.header("Values - Olist Dataset")
st.markdown("Explore the relationship between each individual variable and each reviews "
            "We can intuit patterns within the individual values and gain an understanding of how the data is utilized for classification.")
st.sidebar.header("Individual Values")

# Setting graph to display
options = st.sidebar.radio("Select values",
                           options=["temps_livraison", "order_estimated_delivery_date","retard_livraison"])

show_df = df.filter(items=[options, "review_score"])

plot1 = px.histogram(
    show_df,
    x=show_df[options],
    title=f"{options} Histogram", 
    nbins=30,
    color="review_score")

st.plotly_chart(plot1)