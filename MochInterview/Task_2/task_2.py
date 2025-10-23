from time import sleep
import pandas as pd
import asyncio


class SimTimer:
    def __init__(self, df: pd.DataFrame, playback_rate: float = 1.0, ts_col: str = "timestamp"):
        if ts_col not in df.columns:
            raise ValueError(f"Expected timestamp column '{ts_col}' in DataFrame.")
        self.df = df
        self.ts_col = ts_col
        self.playback_rate = playback_rate
        self.running = False
        self.index = 0
        self._n = len(df)

    async def start(self):
        """Stream each row at intervals based on timestamp deltas."""
        if self._n == 0:
            return

        self.running = True

        # Loop while there's a "next" row to time against
        while self.running and self.index < self._n - 1:
            curr = self.df.iloc[self.index]
            nxt  = self.df.iloc[self.index + 1]

            # Emit current row (replace with callback if you want)
            print(curr.to_dict())

            # Compute delta to next row (scaled)
            dt = float(nxt[self.ts_col]) - float(curr[self.ts_col])
            dt = max(dt / self.playback_rate, 0.0)

            # Non-blocking sleep
            await asyncio.sleep(dt)

            # Advance
            self.index += 1

        # Optionally emit the final row once more at the end
        if self.running and self.index == self._n - 1:
            print(self.df.iloc[self.index].to_dict())

        self.running = False
        # print("Simulation complete.")

    def stop(self):
        self.running = False
