import streamlit as st
import pandas as pd
import plotly.express as px
import plotly
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

#order_delivered_customer_date,order_delivered_carrier_date,
# order_estimated_delivery_date,temps_livraison,retard_livraison,
#review_id,order_id,review_score,review_comment_title
# review_comment_message,review_creation_date,
# review_answer_timestamp,customer_id,order_status,order_purchase_timestamp,
# order_approved_at,order_delivered_carrier_date,order_delivered_customer_date,
# order_estimated_delivery_date,score,temps_livraison,retard_livraison,produit_recu


#Setup data by executing a SQL query
query = 'SELECT * FROM TrainingDataset'

#Connect to the SQLITE database
with sqlite3.connect('olist2.db') as conn:
    df = pd.read_sql_query(query, conn)

conn.close()

# Make page
st.set_page_config(page_title="Olist Dataset")
st.header("Comparison - Olist Dataset")
st.markdown("Explore these variables inorder to understand their relationships and how they correlate with the species. "
            "As patterns emerge, we can intuitively understand how the RandomForestClassifier makes decisions in classifying data.")
st.sidebar.header("Variable Comparison")


# Setting graph to display
options = st.sidebar.radio("Select comparison",
                           options=["The importance of the Customer Delivery Date on the Review Score",
                                    "The consequences of the Carrier Delivery Date on the Customer Delivery Date"
])

if options == "The importance of the Customer Delivery Date on the Review Score": 
    df1 = df.loc[df['order_delivered_customer_date'] < df['order_estimated_delivery_date']]
    # plot1 = px.scatter(
    #     df1.sample(frac=0.9),
    #     x="order_delivered_customer_date",
    #     y="order_estimated_delivery_date",
    #     title="Orders delivered less than initial Estimated Delivery Time",
    #     color='review_score',
    #     color_continuous_scale='Viridis',
    #     size_max=10)
    # # Personnalisation des axes
    # plot1.update_xaxes(title_text="Customer Order Delivery Date")
    # plot1.update_yaxes(title_text="Estimated Delivery Time")
    plot1 = px.histogram(
        df1,
        x="temps_livraison",
        y="retard_livraison",
        title="Orders delivered later than initial Estimated Delivery Time",
        color='score',
        #color_continuous_scale='viridis',     
        #size_max=10
        color_discrete_map={1: 'violet', 0: 'light blue'},
        nbins=38
        )
     # Personnalisation des axes
    plot1.update_xaxes(title_text="Delivery Date")
    plot1.update_yaxes(title_text="Late Delivery")
    
    df2 = df.loc[(df['order_delivered_customer_date'] >= df['order_estimated_delivery_date'])]
    plot2 = px.histogram(
        df2,
        x="temps_livraison",
        y="retard_livraison",
        title="Orders delivered later than initial Estimated Delivery Time",
        color='score',
        #color_continuous_scale='viridis',     
        #size_max=10
        color_discrete_map={1: 'violet', 0: 'light blue'},
        nbins=38
        )
    # Personnalisation des axes
    plot2.update_xaxes(title_text="Delivery Date")
    plot2.update_yaxes(title_text="Late Delivery")
    
    st.plotly_chart(plot1)
    st.plotly_chart(plot2)
   

else:
    
    df3 = df.loc[df['order_delivered_customer_date'] < df['order_estimated_delivery_date']]
    plot3 = px.histogram(
        df3,
        x="order_delivered_carrier_date",
        y="retard_livraison",
        title='Graphs showing the Carrier Delivery Date in function of on-time deliveries',
        color='review_score',
        color_discrete_map={1: 'violet', 0: 'light blue'},
        nbins=38
    )
     # Personnalisation des axes
    plot3.update_xaxes(title_text="Carrier Delivered Time")
    plot3.update_yaxes(title_text="Late Delivery")
    
    df4 = df.loc[df['order_delivered_customer_date'] > df['order_estimated_delivery_date']]
    plot4 = px.histogram(
        df4,
        x="order_delivered_carrier_date",
        y="retard_livraison",
        title='Graphs showing the Carrier Delivery Date prior to late deliveries',
        color='review_score',
        color_discrete_map={1: 'violet', 0: 'light blue'},
        nbins=38
    )
     # Personnalisation des axes
    plot4.update_xaxes(title_text="Carrier Delivered Time")
    plot4.update_yaxes(title_text="Late Delivery")
    
    
    st.plotly_chart(plot3) 
    st.plotly_chart(plot4)


