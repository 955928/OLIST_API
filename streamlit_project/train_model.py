import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
import csv
import json as js
import pickle as pk
import numpy as np
import sqlite3


def make_model_save():
    
    query = 'SELECT * FROM TrainingDataset'

    # Setup data
    with sqlite3.connect('olist2.db') as conn:
        df = pd.read_sql_query(query, conn)

    conn.close()

# #Process Data
#     label_encoder = LabelEncoder()
#     df['review_score_encoded'] = label_encoder.fit_transform(df['review_score'])

# #Save processed data to new file and json
#     df.to_csv('encoded_data_csv')
#     options_title = df['review_score'].unique()

    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])


#     # Separate Target and Features : x and y datas
#en mettant des doubles crochets, il ne se plus reconnu commes des listes mais plutôt un Dataframe
    y = df[['score']]
    x = df[["order_delivered_customer_date"]]

    # Separate TrainSet / TestSet
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

    # Train model
    model = RandomForestClassifier(max_depth=2, random_state=0)
    model.fit(x_train, y_train)

#     # Save model
    with open('main_model.pkl', 'wb') as fichier_modele:
        
        pk.dump(model, fichier_modele)
        

    
