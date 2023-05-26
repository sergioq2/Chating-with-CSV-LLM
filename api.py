from fastapi import FastAPI
from cognitive import principal
from mangum import Mangum
import uvicorn
from preprocessing import preprocesamiento
import pandas as pd


def generate_string(user):
    string = ''
    for key, value in user.items():
        if value is not None and not pd.isna(value):
            string += str(value) + ' '
    return string

app = FastAPI(title="Recomendation job system Hunty", 
              description="API to find the best job match", 
              version="1.0.1")

handler = Mangum(app)

@app.get("/")
def home():
    return {"message": "Welcome to Hunty API"}

@app.get("/top")
def estimation(user:str):
    resultado = principal(user)
    return resultado

@app.post("/vacantes")
def update_vacantes():
    _, _, users= preprocesamiento()
    users = users.sample(3)
    dict_result = {}
    for id in users['id_user']:
        user = users.loc[users['id_user'] == id].to_dict('records')[0]
        string = generate_string(user)
        resultado = principal(string)
        users.loc[users['id_user'] == id, 'top_vacantes'] = resultado
        dict_result[id] = resultado
    return dict_result