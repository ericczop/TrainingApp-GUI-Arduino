import matplotlib.pyplot as plt
import numpy as np


class DataAnalysis:
    def __init__(self, data):
        self.data = data
        self.distance = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
        self.kilograms = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

    def count_reps(self):
        reps = 0
        switch = False

        for i in range(len(self.data) - 1):
            if self.data[i] + 2 < self.data[i + 1] and not switch:
                reps += 1
                switch = True
            if self.data[i] > self.data[i + 1] and switch:
                switch = False
        return reps

    def count_kilograms(self):
        actual_height = round(self.data[0], 1)

        if actual_height in self.distance:
            actual_kilograms = self.kilograms[self.distance.index(actual_height)]
        else:
            closest_distance = min(self.distance, key=lambda x: abs(x - actual_height))
            actual_kilograms = self.kilograms[self.distance.index(closest_distance)]

        return actual_kilograms

    def plot_data(self):
        x_points = np.arange(start=0, stop=len(self.data), step=1)
        y_points = np.array(self.data)

        plt.plot(x_points, y_points)
        plt.xlabel("Czas (s)")
        plt.ylabel("Odległość (cm)")

        plt.text(x_points[-1], y_points[-1], f"Kilograms assumed: {self.count_kilograms()} kg", fontsize=10, ha='right')

        plt.show()

