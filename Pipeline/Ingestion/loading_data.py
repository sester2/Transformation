import json 
import urllib.request
import tarfile
import pandas as pd
from pathlib import Path

#Data source: 
# --------------    --------------------   -------------------

# Load data from API into DataFrame for further processing
def load_data():
    try:
        housing_path = Path("https://github.com/ageron/data/raw/main/housing.tgz")
        if not housing_path.is_file():
            urllib.request.urlretrieve(housing_path)
            with tarfile.open(housing_path) as housing_tarball:
                housing_tarball.extractall(path='datasets')
        
        df = pd.read_csv(Path("datasets/housing/housing.csv"))
        if df.empty:
            raise ValueError("DataFrame is empty after loading")
        else:   
            print("Data loaded successfully.")

    except Exception as e:
        print(f"Error loading data: {e}")
        df = pd.DataFrame()

    return df

#---------------     --------------------   -------------------
# Convert loaded data to DataFrame for further processing 

#---------------     --------------------   -------------------
