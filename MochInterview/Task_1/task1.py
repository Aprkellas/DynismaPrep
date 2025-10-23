

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
        self.series: dict[datetime, TimeSeries] = []
        self.moving_averages: dict[datetime, float] = []
        self.buffer = buffer

    def ingest(self, data: dict) -> bool:
        series = TimeSeries(
            timestamp=data["timestamp"],
            accel_x=data["accel_x"],
            accel_y=data["accel_y"],
            accel_z=data["accel_z"],
            gyro_x=data["gyro_x"],
            gyro_y=data["gyro_y"],
            gyro_z=data["gyro_z"],
        ) 
        if(self.add_series(series)):
            if (self.compute_moving_average(series.timestamp)):
                return True
        return False
    
    def add_series(self, series: TimeSeries) -> bool:
        try:
            self.series[series.timestamp] = series
            if len(self.series) > self.buffer:
                self.series.pop(next(iter(self.series)))
            return True
        except:
            return False

    def compute_moving_average(self, key: datetime) -> bool:
        val = self.series[key]
        if val is None:
            return False
        
        total = (val.accel_x + val.accel_y + val.accel_z)
        if (total == 0):
            return False
        
        self.moving_averages[key] = total / 3
        return True

    def get_series(self) -> List[TimeSeries]:
        return self.series
    