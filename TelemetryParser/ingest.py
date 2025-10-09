import asyncio
import json 
import pandas as pd

from arteficialtimer import ArteficialTimer
from ringbuffer import RingBuffer

class Ingest:
    def __init__(self, file: str):
        self.file = file
        if not self.validate_file():
            return
        self.timer = ArteficialTimer()
        self.data = self.parse_telemetry()

        # Ensure timestamp is float, sorted
        self.data["timestamp"] = pd.to_numeric(self.data["timestamp"], errors="coerce")
        self.data = self.data.sort_values("timestamp", kind="mergesort").reset_index(drop=True)
        self.ringbuffer = RingBuffer(self.data)
        self.running = True
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
    
    async def run_simulation(self):
        timer_task = asyncio.create_task(self.timer.timer())
        current_time = object()
        try:
            while self.running:
                await asyncio.sleep(0)
                if self.timer.time != current_time:
                    current_time = self.timer.time
                    current_data = self.ringbuffer.get_data(current_time)
                    print(current_data)
        except KeyboardInterrupt:
            pass
        finally:
            self.timer.turn_off()
            timer_task.cancel()
            print("Simulation ended.")