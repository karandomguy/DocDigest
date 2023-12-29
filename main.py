import dill
import os
import json
import requests

headers = {"Authorization": f"Bearer {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}"}
API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response
    
def load_and_predict(input_data):
    with open('DocDigest/DocDigest.pkl', 'rb') as file:
        your_model = dill.load(file)
    predictions = your_model.predict(input_data)
    audio_output = query({"text_inputs": predictions})

    return predictions, audio_output