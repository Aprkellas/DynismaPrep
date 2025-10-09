import numpy as np

class RingBuffer:
    def __init__(self, data):
        self.data = data
        self.sample_size = 5  # Number of previous samples to include

    def get_data(self, time):
        df = self.data
        ts = df['timestamp'].to_numpy()

        idx = int(np.searchsorted(ts, time, side="right") - 1)

        if idx < 0:
            return df.iloc[:1].reset_index(drop=True)
        
        start_idx = max(0, idx - self.sample_size)

        return df.iloc[start_idx:idx + 1].reset_index(drop=True)

