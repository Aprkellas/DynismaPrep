import json 
import pandas as pd

def parse_telemetry(file: str):
    with open(file, 'r') as f:
        data = [json.loads(line) for line in f]
    
    df = pd.json_normalize(data)
    return df

# extend with other parsing functions as needed