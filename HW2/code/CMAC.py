from cmath import pi
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import math
import random
import time



# Preparing dataset using sin(x) function to train 1-D CMAC
# Creating and sampling my function at 100 evenly spaced points
def dataGenerator(input):
    max = 360 # In degrees
    min = 0
    data_points = 100
    # computing step size
    step_size = float((max - min)/ data_points)
    # computing in radians
    step_size_rad = float(step_size*(np.pi/180))
    x = [step_size_rad * (i + 1) for i in range(0, data_points)]
    y = [input(x[i]) for i in range(0, data_points)]
    print(x,y)
    #generating training and test data sets (30 test, 70 train)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
    index_train = [x.index(i) for i in x_train]
    index_test = [x.index(i) for i in x_test]

    return [x, y, x_train, x_test, y_train, y_test, index_train, index_test, step_size_rad]


dataset = dataGenerator(np.sin)