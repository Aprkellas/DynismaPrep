from time import sleep
import pandas as pd


class SimTimer:
    def __init__(self, df: pd.DataFrame, playback_rate=1.0):
        self.df = df
        self.playback_rate = playback_rate
        self.running = False
        self.index = 0

    async def start(self):
        """Stream each row at real-time intervals"""
        self.running = True
        while self.running:
            row = self.df.iloc[self.index]
            print(row)
            self.index += 1
            sleep(self.playback_rate)


    def stop(self):
        self.running = False
