from connection import Connection
from analysis import DataAnalysis

RUN_TIME = 10
connection = Connection("COM3")


class GiveData:
    def give(self):
        if connection.open():
            data_list = connection.read_data(RUN_TIME)
            print(f"Data list: {data_list}")
            connection.close()
            analysis = DataAnalysis(data_list)
            reps = int(analysis.count_reps())
            kilograms = int(analysis.count_kilograms())
            return kilograms, reps
