from connection import Connection
from analysis import DataAnalysis

RUN_TIME = 10

connection = Connection("COM3")

if connection.open():
    data_list = connection.read_data(RUN_TIME)
    print(f"Data list: {data_list}")
    connection.close()
    analysis = DataAnalysis(data_list)
    reps = analysis.count_reps()
    print(f"Number of reps done: {reps}")
    kilograms = analysis.count_kilograms()
    print(f"Kilograms: {kilograms}")
    analysis.plot_data()
