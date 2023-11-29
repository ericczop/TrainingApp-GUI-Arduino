from analysis import DataAnalysis
import time


class GiveData:
    def give(self):
        analysis = DataAnalysis([9, 6, 4, 7, 5, 6, 6, 5, 5, 5, 5, 5, 5, 6, 6, 7, 6, 9, 5, 5, 5, 6, 5, 6, 6, 6, 5, 5, 5, 6, 6, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 8, 8, 8, 8, 8, 8, 9, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 9, 10, 9, 9, 10, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10, 11, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 11, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 17, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 19, 18, 18, 19, 19, 18, 18, 19, 19, 18, 19, 18, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 23, 23, 24, 23, 23, 24, 24, 24, 24, 24, 24, 25, 24, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 26, 26, 27, 26, 26, 27, 27, 26, 27, 26, 26, 26, 26, 26, 26, 26, 27, 28, 27, 28, 28, 28, 28, 27, 27, 27, 27, 28, 27, 27, 28, 28, 28, 28, 28, 28, 27, 27, 27, 27, 27, 27, 27, 27, 27, 26, 26, 26, 26, 26, 26, 26, 25, 25, 25, 26, 25, 26, 25, 26, 26, 26, 25, 26, 26, 26, 26, 26, 26, 26, 26, 25, 26, 26, 25, 25, 26, 26, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 25, 24, 25, 24, 24, 24, 24, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 21, 21, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 21, 20, 21, 21, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 19, 19, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 15, 14, 14, 14, 15, 14, 14, 13, 13, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 12, 13, 13, 13, 12, 12, 12, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 9, 9, 9, 9, 8, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 7, 8, 7, 8, 8, 8, 8, 8, 8, 7, 7, 8, 7, 7, 7, 7, 7, 8, 7, 8, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 6, 6, 7, 7, 6, 6, 6, 6, 7, 6, 6, 7, 6, 7, 6, 7, 6, 7, 6, 6, 6, 7, 7, 6, 6, 6, 6, 6, 7, 7, 7, 6, 6, 6, 6, 6, 7, 7, 6, 7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 6, 6, 6, 6, 6, 7, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 6, 7, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 8, 7, 8, 8, 8, 8, 7, 8, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 8, 8, 8, 8, 9, 9, 9, 9, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 11, 12, 13, 12, 13, 13, 13, 12, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 16, 17, 17, 17, 17, 17, 17, 17, 18, 17, 18, 17, 17, 17, 18, 17, 16, 18, 17, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 19, 19, 2, 13, 20, 20, 20, 20, 2, 15, 20, 20, 20, 21, 5, 2, 17, 21, 21, 21, 21, 5, 2, 18, 21, 22, 21, 5, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 3, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 7, 6, 7, 7, 7, 7, 6, 7, 7, 6, 7, 7, 8, 8, 7, 7, 8, 7, 8, 7, 8, 8, 8, 9, 8, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 25, 26, 26, 25, 26, 26, 26, 26, 26, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 24, 25, 24, 24, 24, 24, 23, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 22, 22, 22, 21, 21, 21, 21, 21, 21, 21, 20, 21, 21, 21, 20, 21, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 19, 19, 20, 19, 19, 19, 18, 19, 18, 19, 18, 18, 18, 18, 18, 18, 17, 18, 18, 18, 18, 17, 18, 18, 17, 18, 17, 17, 17, 17, 18, 17, 17, 17, 17, 17, 16, 17, 16, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 12, 13, 13, 12, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 7, 7, 8, 8, 8, 8, 8, 8, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 6, 6, 7, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 6, 5, 6, 5, 5, 6, 5, 6, 5, 6, 5, 5, 5, 6, 6, 6, 5, 6, 6, 6, 6, 6, 5, 6, 6, 5, 6, 5, 5, 5, 5, 6, 5, 6, 6, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 7, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 6, 7, 6, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 9, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 12, 12, 13, 13, 13, 12, 13, 13, 13, 13, 13, 13, 13, 14, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 14, 14, 15, 15, 15, 15, 15, 16, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 18, 17, 18, 17, 18, 17, 18, 17, 18, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 18, 18, 18, 20, 19, 20, 18, 20, 19, 20, 19, 20, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 7, 22, 8, 22, 8, 23, 11, 23, 9, 6, 2, 2, 24, 9, 2, 3, 3, 3, 3, 3, 24, 10, 11, 11, 11, 11, 11, 12, 10, 12, 11, 13, 14, 13, 12, 11, 12, 13, 12, 14, 13, 12, 14, 13, 12, 13, 13, 13, 13, 14, 13, 14, 14, 13, 13, 13, 14, 14, 15, 15, 15, 14, 15, 15, 14, 14, 14, 15, 15, 15, 15, 16, 15, 16, 15, 15, 16, 16, 16, 15, 16, 16, 16, 16, 17, 16, 16, 16, 17, 16, 16, 16, 17, 18, 17, 17, 17, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 18, 17, 18, 17, 18, 18, 18, 18, 18, 18, 18, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 18, 19, 19, 19, 19, 20, 20, 21, 20, 21, 21, 22, 21, 27, 26, 27, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 26, 27, 26, 27, 26, 27, 26, 27, 27, 27, 26, 27, 26, 26, 26, 26, 26, 27, 26, 26, 27, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 26, 21, 26, 26, 22, 26, 26, 26, 22, 26, 26, 26, 26, 26, 26, 26, 26, 27, 26, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 26, 26, 25, 26, 26, 26, 25, 27, 25, 26, 25, 25, 26, 26, 26, 19, 17, 16, 17, 17, 16, 19, 17, 17, 16, 17, 16, 14, 16, 16, 15, 16, 15, 14, 14, 14, 13, 15, 13, 13, 15, 14, 13, 14, 14, 12, 13, 13, 13, 14, 12, 12, 12, 12, 11, 11, 11, 13, 10, 11, 9, 3, 3, 3, 24, 11, 10, 10, 24, 9, 4, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 22, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 18, 19, 18, 19, 18, 19, 18, 18, 18, 18, 18, 18, 18, 18, 17, 18, 18, 18, 17, 17, 18, 17, 18, 18, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 15, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 14, 14, 14, 14, 14, 14, 14, 13, 14, 13, 14, 13, 14, 13, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 13, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 12, 12, 12, 11, 11, 11, 11, 12, 11, 12, 12, 12, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 9, 10, 9, 9, 9, 9, 9, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 7, 8, 8, 7, 7, 8, 8, 7, 7, 8, 8, 8, 7, 8, 8, 7, 7, 8, 7, 7, 8, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 6, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 7, 7, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 7, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 9, 8, 8, 8, 9, 8, 9, 9, 8, 9, 8, 9, 9, 8, 9, 8, 8, 9, 8, 9, 9, 8, 10, 9, 8, 9, 9, 9, 9, 9, 9, 10, 10, 9, 10, 9, 9, 9, 10, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10, 10, 10, 10, 11, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 12, 13, 13, 13, 13, 13, 13, 13, 14, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 15, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 15, 16, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 17, 18, 17, 18, 17, 18, 17, 18, 17, 18, 17, 18, 17, 18, 16, 16, 16, 17, 17, 16, 16, 18, 19, 19, 18, 19, 19, 19, 19, 19, 20, 19, 20, 19, 20, 20, 20, 20, 20, 20, 20, 21, 20, 20, 20, 20, 21, 21, 21, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 21, 22, 22, 22, 22, 22, 23, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 23, 23, 23, 23, 11, 11, 24, 24, 24, 24, 24, 23, 24, 23, 24, 24, 23, 24, 24, 24, 23, 24, 24, 24, 12, 11, 11, 11, 11, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 24, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 24, 13, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 24, 25, 24, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 23, 24, 24, 24, 24, 24, 23, 23, 23, 23, 24, 23, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 23, 22, 22, 22, 23, 22, 22, 22, 22, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 21, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 20, 20, 20, 20, 20, 20, 20, 19, 20, 20, 19, 20, 19, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 18, 19, 19, 19, 18, 19, 18, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 18, 17, 18, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 17, 17, 17, 16, 16, 16, 17, 17, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 16, 15, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 13, 13, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 13, 13, 13, 12, 12, 12, 12, 12, 12, 13, 12, 12, 12, 12, 12, 12, 11, 12, 12, 12, 12, 12, 12, 11, 11, 11, 12, 11, 11, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 10, 10, 10, 10, 10, 10, 9, 9, 9, 10, 9, 9, 10, 9, 10, 10, 10, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 9, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 7, 8, 7, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 5, 5, 5, 5, 6, 6, 6, 6, 6, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 8, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 7, 8, 8, 7, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 9, 8, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 10, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 13, 14, 14, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 16, 17, 17, 16, 17, 16, 17, 17, 16, 17, 17, 17, 16, 17, 17, 18, 17, 18, 17, 18, 17, 18, 18, 18, 18, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19, 18, 19, 18, 19, 18, 19, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 20, 21, 20, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 24, 25, 25, 24, 25, 24, 24, 25, 25, 25, 24, 25, 25, 25, 24, 25, 24, 25, 24, 24, 24, 25, 24, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 24, 25, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 21, 21, 22, 22, 21, 22, 22, 22, 22, 21, 21, 21, 21, 22, 22, 21, 22, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 20, 21, 21, 21, 21, 21, 21, 20, 20, 20, 20, 20, 21, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 19, 20, 20, 19, 19, 19, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 17, 17, 16, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 14, 14, 15, 14, 15, 14, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 14, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 11, 11, 11, 10, 10, 10, 11, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 2, 9, 10, 10, 9, 10, 10, 10, 9, 8, 9, 9, 9, 8, 9, 8, 8, 8, 9, 9, 8, 8, 9, 9, 9, 8, 9, 9, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 8, 7, 7, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 8, 8, 7, 7, 7, 7, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 7, 7, 6, 7, 6, 6, 7, 6, 7, 7, 7, 6, 7, 7, 6, 7, 7, 6, 6, 6, 7, 6, 7, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 6, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 8, 8, 7, 7, 7, 7, 7, 8, 7, 8, 8, 8, 7, 7, 7, 7, 8, 7, 7, 8, 8, 7, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 9, 9, 9, 8, 8, 8, 9, 9, 8, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 12, 12, 12, 12, 11, 12, 11, 12, 13, 12, 12, 12, 12, 13, 12, 13, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 15, 14, 15, 15, 14, 15, 14, 15, 15, 15, 15, 15, 15, 16, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 15, 16, 16, 16, 16, 16, 16, 16, 16, 17, 16, 17, 16, 16, 16, 16, 17, 17, 17, 16, 16, 16, 16, 17, 17, 17, 17, 16, 17, 17, 17, 17, 17, 17, 17, 17, 18, 17, 18, 18, 17, 18, 18, 18, 18, 18, 19, 18, 18, 19, 18, 18, 19, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 19, 19, 20, 19, 20, 20, 20, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 23, 24, 23, 24, 24, 24, 24, 23, 23, 24, 24, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 24, 23, 24, 24, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 23, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 19, 20, 19, 19, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 18, 17, 17, 17, 18, 17, 18, 17, 18, 17, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 17, 16, 17, 17, 16, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 15, 14, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 14, 13, 13, 14, 13, 13, 13, 12, 13, 13, 13, 12, 13, 13, 13, 13, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 12, 11, 12, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 10, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 9, 9, 9, 10, 9, 10, 10, 10, 10, 10, 10, 10, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 8, 9, 9, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 8, 7, 8, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 7, 6, 6, 6, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 6, 7, 6, 7, 7, 6, 6, 6, 6, 7, 7, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 6, 6, 6, 6, 7, 6, 7, 7, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 7, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 6, 6, 8, 7, 6, 7, 7, 7, 6, 7, 8, 7, 7, 8, 8, 7, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 8, 7, 7, 8, 8, 7, 7, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 8, 9, 8, 8, 8, 8, 9, 8, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 10, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 16, 16, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 16, 17, 17, 16, 16, 16, 16, 16, 17, 17, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 17, 17, 18, 18, 17, 18, 16, 17, 18, 17, 18, 18, 17, 17, 17, 13, 15, 17, 17, 19, 18, 17, 19, 17, 19, 19, 18, 19, 19, 18, 19, 18, 18, 19, 18, 19, 20, 19, 19, 20, 18, 20, 20, 19, 20, 20, 19, 20, 20, 20, 20, 20, 20, 20, 19, 20, 20, 20, 20, 20, 20, 21, 20, 20, 20, 20, 20, 21, 21, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 21, 21, 22, 22, 22, 22, 22, 23, 23, 22, 22, 22, 22, 22, 23, 23, 22, 22, 22, 23, 22, 22, 22, 22, 22, 22, 23, 23, 22, 23, 22, 22, 23, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 23, 24, 24, 24, 24, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 24, 23, 23, 24, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 20, 20, 20, 20, 20, 20, 19, 19, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 18, 18, 19, 19, 19, 19, 19, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 18, 17, 17, 17, 17, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 17, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 14, 15, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 13, 13, 13, 13, 14, 13, 14, 14, 13, 13, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 11, 11, 11, 11, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 10, 9, 9, 9, 10, 9, 10, 9, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 8, 9, 9, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 8, 8, 8, 9, 9, 8, 8, 9, 9, 9, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 7, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 8, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 7, 8, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 7, 8, 7, 8, 8, 8, 8, 7, 8, 8, 8, 7, 8, 7, 8, 8, 7, 8, 8, 8, 8, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 7, 7, 8, 7, 8, 8, 7, 8, 7, 8, 8, 8, 7, 8, 7, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8, 7, 7, 8, 8, 8, 8, 7, 8, 8, 7, 8, 7, 8, 7, 8, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 6, 7, 6, 7, 6, 7, 7, 6, 7, 6, 7, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 7, 6, 7, 7, 7, 6, 7, 7, 8, 7, 7, 8, 7, 8, 7, 7, 7, 7, 8, 7, 7, 7, 7, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 8, 8, 7, 8, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 8, 7, 8, 8, 8, 7, 8, 7, 8, 7, 8, 7, 8, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 8, 7, 7, 8, 8, 7, 8, 8, 7])
        time.sleep(5)
        kilograms = int(analysis.count_kilograms())
        reps = int(analysis.count_reps())
        data_analysed = [kilograms, reps]
        return data_analysed
