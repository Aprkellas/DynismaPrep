import json 
import pandas as pd

from arteficialtimer import ArteficialTimer

class Ingest:
    def __init__(self, file: str):
        self.file = file
        if not self.validate_file():
            return
        self.timer = ArteficialTimer()

    def validate_file(self):
        if not isinstance(self.file, str):
            raise ValueError("File path must be a string.")
        if not (self.file.endswith('.jsonl') or self.file.endswith('.csv')):
            raise ValueError("Unsupported file format. Only .jsonl and .csv are supported.")
        return True

    def parse_telemetry(self):
        with open(self.file, 'r') as f:
            if self.file.endswith('.jsonl'):
                data = [json.loads(line) for line in f]
                df = pd.json_normalize(data)
        return df
    

# extend with other parsing functions as needed