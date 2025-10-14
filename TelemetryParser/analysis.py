

class Analyser:
    @staticmethod
    def analyze(data):
        avg_acceleration_3d = data[['accel_x', 'accel_y', 'accel_z']].to_numpy().mean(axis=0)
        accel = avg_acceleration_3d.sum()
        return accel / avg_acceleration_3d.shape[0] if avg_acceleration_3d.shape[0] > 0 else 0
