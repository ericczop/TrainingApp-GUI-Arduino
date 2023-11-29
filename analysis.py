import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


class DataAnalysis:
    def __init__(self, data):
        self.data = data
        self.distance = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
        self.kilograms = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        self.peaks = None
        self.mins = None

    def smooth_data(self, window_size=300):
        smoothed_data = np.convolve(self.data, np.ones(window_size) / window_size, mode='valid')
        return smoothed_data

    def count_reps(self):
        self.peaks = find_peaks(self.smooth_data(), prominence=2, distance=500)
        print(self.peaks[0])
        return len(self.peaks[0])

    def count_kilograms(self):
        actual_height = round(self.data[0], 1)

        if actual_height in self.distance:
            actual_kilograms = self.kilograms[self.distance.index(actual_height)]
        else:
            closest_distance = min(self.distance, key=lambda x: abs(x - actual_height))
            actual_kilograms = self.kilograms[self.distance.index(closest_distance)]

        return actual_kilograms

    def plot_data(self):
        x_points = np.arange(start=0, stop=len(self.smooth_data()), step=1)
        y_points = self.smooth_data()

        plt.plot(x_points, y_points)
        plt.xlabel("Samples quantity")
        plt.ylabel("Distance (cm)")

        plt.text(x_points[-1], y_points[-1], f"Kilograms: {self.count_kilograms()} kg", fontsize=10, ha='right')

        if self.peaks is not None:
            [plt.axvline(p, c='red', linewidth=1) for p in self.peaks[0]]
        if self.mins is not None:
            [plt.axvline(p, c='blue', linewidth=1) for p in self.mins[0]]

        plt.axvline(x_points[0], c='black', linewidth=1)
        plt.axvline(x_points[-1], c='black', linewidth=1)
        plt.show()
