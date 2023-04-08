from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import uuid
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from random import randint
import uuid
import cv2
import numpy as np
import pandas as pd
#import TensorFlow
#from TensorFlow import keras
from sklearn.ensemble import ExtraTreesRegressor
#import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from pydantic import BaseModel
import pickle

#pickled_model1 = pickle.load(open('model_regressor.pkl', 'rb'))
#pickled_model2 = pickle.load(open('model_regressor_gpu.pkl', 'rb'))

pickled_model3 = pickle.load(open('vit_model.pkl', 'rb'))

from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    value1: int
    value2: int
    value3: int
    value4: int

class Item2(BaseModel):
    year: int
    month: int

@app.post("/predict_cpu")
async def predict_cpu(info : Item):
    a = info.value1
    b = info.value3

    X = np.array([[a, b]])

    predictions = pickled_model1.predict(X)
    predictions = list(predictions)
    predictions = predictions[0]

    print(predictions)

    return {"CPUWatt" : round(predictions,5)}


@app.post("/predict_gpu")
async def predict_cpu(info : Item):
    a = info.value2
    b = info.value4

    X = np.array([[a, b]])

    predictions = pickled_model2.predict(X)
    predictions = list(predictions)
    predictions = predictions[0]

    print(predictions)

    return {"GPU_Power" : round(predictions,5)}


@app.post("/ebunits")
async def predict_ebunits(info : Item2):
    a = info.year
    b = info.month

    X = np.array([[a, b]])

    predictions = pickled_model3.predict(X)
    predictions = list(predictions)
    predictions = predictions[0]

    print(predictions)

    return {"ebunits" : round(predictions,5)}



