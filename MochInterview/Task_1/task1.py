from collections import deque
from typing import List
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
    def __init__(self, buffer_size: int = 10):
        self.series: deque[TimeSeries] = deque(maxlen=buffer_size)
        self.moving_average: float = 0
        self.buffer = buffer_size

    def ingest(self, data: dict) -> bool:
        try:
            ts = TimeSeries(**data)
            self.series.append(ts)
            self.compute_moving_average()
            return True
        except:
          return False

    def compute_moving_average(self) -> None:
        total = 0
        for v in self.series:
            total += (v.accel_x + v.accel_y + v.accel_z) / 3
        self.moving_average = total / self.series.count()

    def get_series(self) -> List[TimeSeries]:
        return list(self.series)
    