import numpy as np

'''
@Author : Eduardo Medina
'''

class StatisticsHandler():

    def __init__(self) -> None:
        print("StatisticsHandler")
    
    def getMeasures(self, data):
        print("getMeasures")

        # numpy mean,  median standard deviation
        mean = np.mean(data)
        print("mean", mean)
        median = np.median(data)
        print("median", median)

        std = np.std(data)
        print("std", std)

        min = np.min(data)
        print("min", min)

        max = np.max(data)
        print("max", max)

        print("-----------------------------")


