from analysis import DataAnalysis

class GiveData:
    def give(self, connection):
        if connection.open():
            data_list = connection.read_data()
            print(f"Data list: {data_list}")
            connection.close()
            analysis = DataAnalysis(data_list)
            reps = int(analysis.count_reps())
            kilograms = int(analysis.count_kilograms())
            data_analysed = [kilograms, reps]
            return data_analysed
