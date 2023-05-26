
import json
import pandas as pd

import uvicorn

import fastapi
from fastapi import FastAPI
app_lstm = FastAPI()

#import mangum
#from mangum import Mangum
#handler = Mangum(app_lstm)

# The EndPoint is by default http://127.0.0.1:8000/
@app_lstm.get("/")  # The INDEX (main) page of the EndPoint will return the JSON file below (no INPUT needed)
def index():
    return {"message": "Hello, stranger"}

@app_lstm.get("/{name}")  # The "name" page of the EndPoint will return the JSON file below (direct url input typed)
def get_name(name: str):
    return {"message": f"Hello, {name}"}



with open("load_model_keras_lstm.py") as f:
    exec(f.read())


# Declare the prediction EndPoint (Here it is http://127.0.0.1:8000/predict).
# It is accessed via JSON POST request ( response = requests.post(url, headers=headers, params=params) ).
@app_lstm.post("/predict")

# The function below tells the Endpoint how to calculate predictions from the JSON input received (here a tweet features in format for LSTM)
def predict_sentiments_probability(data_as_json):
    # Make the input JSON into a dictionary
    data = json.loads(data_as_json)

    # Make the dictionary into a dataframe
    df = pd.DataFrame.from_dict(data)

    # Model's probability prediction
    probability = model_keras_lstm.predict(df)
    
    return {"probability": probability[0][0].item()}



# Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app_lstm, host="127.0.0.1", port=8000)