from cmath import pi
from operator import le
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
    #generating training and test data sets (30 test, 70 train)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
    index_train = [x.index(i) for i in x_train]
    index_test = [x.index(i) for i in x_test]

    return [x, y, x_train, x_test, y_train, y_test, index_train, index_test, step_size_rad]

# Defining CMAC whose inputs are either discrete or continous
def CMAC(input):

    return e_train, e_test

# Initializing neccessary global variables
# Train and Test data for training the model
data = dataGenerator(np.sin)
x_data = data[0]
y_data = data[1]
train_x_data = data[2]
train_y_data = data[4]
train_index = data[6]
test_x_data = data[3]
test_y_data = data[5]
test_index = data[7]
step_size = data[8]
size_x_data = len(x_data)
size_train_data = len(train_x_data)
size_test_data = len(test_x_data)
# Length of input data 100
print("Length of generated input data: ", size_x_data)
print("Length of train data:",size_train_data)
print("Length of test data:",size_test_data)
CMAC_train_y = [0]
weights = [0 for i in range(0,size_x_data)]
