from fastapi import FastAPI
import numpy as np
from train_model import make_model_save
from make_pred import make_prediction
import pandas as pd
import sqlite3

app = FastAPI()

@app.get("/infos")
def read_root():
    return {"message": "Hello, welcome on my dashboard!"}


@app.get("/train_model")
def train_model():
    make_model_save()
    print('Training in progress')
    return {"Response": "Training completed."}


@app.get("/{t_l}/{r_l}")
def get_pred(x1: float, x2: float):
    p1 = [x1, x2]
    x = np.array([p1])

    # Entêtes de colonnes
    col_headers = ['temps_livraison', 'retard_livraison']

        # Création du DataFrame
    x_df = pd.DataFrame(x, columns=col_headers)

        # print('x', x_df)

    prediction = make_prediction(x_df)

    # print(prediction)

    return {"prediction": prediction}

