import requests
import json 
import pandas as pd
#Data source: 
# --------------    --------------------   -------------------

# Load data from API into DataFrame for further processing
def load_data():
    try:   
        response = requests.get("https://api.example.com/data")
        response.raise_for_status()  # Check if the request was successful
        loaded_data = response.json()
        if loaded_data is None:
            raise ValueError("No data found in the response")
    except requests.exceptions.RequestException as e:
        print(f"Data unseccessfully loaded: {e}")
        loaded_data = None

    for item in loaded_data:
        print(item)
    #---------------     --------------------   -------------------
    # Convert loaded data to DataFrame for further processing
    try:
        df = pd.DataFrame(loaded_data)
        if df.empty:
            raise ValueError("DataFrame is empty after conversion")
    except Exception as e:
        print(f"Error converting loaded data to DataFrame: {e}")
        df = pd.DataFrame()

#---------------     --------------------   -------------------