
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model('et_api')

# Define predict function
@app.post('/predict')
def predict(T, TM, Tm, SLP, H, VV, V, VM):
    data = pd.DataFrame([[T, TM, Tm, SLP, H, VV, V, VM]])
    data.columns = ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM']
    predictions = predict_model(model, data=data) 
    return {'prediction': list(predictions['Label'])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)