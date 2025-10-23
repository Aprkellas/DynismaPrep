

from ast import List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TimeSeries:
    timestamp: datetime
    accel_x: float
    accel_y: float
    accel_z: float
    gyro_x: float
    gyro_y: float
    gyro_z: float

class Ingest:
    def __init__(self, buffer: int = 10):
        self.series: List[TimeSeries] = []
        self.buffer = buffer

    def ingest(self, data: dict) -> TimeSeries:
        series = TimeSeries(
            timestamp=data["timestamp"],
            accel_x=data["accel_x"],
            accel_y=data["accel_y"],
            accel_z=data["accel_z"],
            gyro_x=data["gyro_x"],
            gyro_y=data["gyro_y"],
            gyro_z=data["gyro_z"],
        ) 
        self.add_series(series)
        return series
    
    def add_series(self, series: TimeSeries) -> None:
        self.series.append(series)
        if len(self.series) > self.buffer:
            self.series.pop(0)

    def get_series(self) -> List[TimeSeries]:
        return self.series
    