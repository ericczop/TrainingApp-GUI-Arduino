import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

    def find_minima(self):
        inverted_data = -self.smooth_data()
        self.mins = find_peaks(inverted_data, prominence=2, distance=500)
        print(self.mins[0])
        return len(self.mins[0])

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

        plt.text(x_points[-1], y_points[-1], f"Kilograms assumed: {self.count_kilograms()} kg", fontsize=10, ha='right')

        if self.peaks is not None:
            [plt.axvline(p, c='red', linewidth=1) for p in self.peaks[0]]
        if self.mins is not None:
            [plt.axvline(p, c='blue', linewidth=1) for p in self.mins[0]]

        plt.axvline(x_points[0], c='black', linewidth=1)
        plt.axvline(x_points[-1], c='black', linewidth=1)
        plt.show()


def start_analysis(connection):
    if connection.open():
        data_list = connection.read_data()
        print(f"Data List: {data_list}")
        connection.close()
        analysis = DataAnalysis(data_list)
        reps = int(analysis.count_reps())
        kilograms = int(analysis.count_kilograms())
        data_analysed = [kilograms, reps]
        return data_analysed


def calculate_statistics(filename='FILES/training_data.csv'):
    try:
        df = pd.read_csv(filename)
        if not df.empty:
            statistics_data = {}
            for exercise_name, group in df.groupby('ExerciseName'):
                max_kg = float(group['Kilograms'].max())
                max_reps = group[group['Kilograms'] == max_kg]['Repetitions'].max()
                mean_kg = f"{round(group['Kilograms'].mean(), 2)}kg"
                mean_reps = int(group['Repetitions'].mean())
                total_kgs = f"{float(group['Kilograms'].sum() * group['Repetitions'].sum())}kg"
                total_reps = group['Repetitions'].sum()
                mean_time = f"{round(group['Time'].mean(), 2)}s"
                count = len(group)
                statistics_data[exercise_name] = {
                    "Max Kilograms": max_kg,
                    "Max Repetitions": max_reps,
                    "Mean Kilograms": mean_kg,
                    "Mean Repetitions": mean_reps,
                    "Total Repetitions": total_reps,
                    "Total Kilograms Lifted": total_kgs,
                    "Mean Time": mean_time,
                    "Total Entries": count,
                }
            return statistics_data
    except FileNotFoundError:
        return None

