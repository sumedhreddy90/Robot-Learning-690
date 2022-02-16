from cmath import pi
from operator import index, le
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import math
import random
import time

from sqlalchemy import true



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

def CMAC_train():
    e =1000 
    for i in range(0, size_train_data):
       convergence = False
       t_index = train_index[i]
       err = 0
       iter = 0
       # generalization factor: offset value
       o_val = 0
       if i - n_index < 0:
           o_val = i - n_index
       if i + n_index >= size_train_data:
           o_val = size_train_data - (i + n_index)

        # iterate through untill convergence is obtained
       while convergence is False:
            c_out = 0
            for j in range(0, GF):
                total_n_index = t_index - (j - n_index)

                if total_n_index >=0 and total_n_index < size_x_data:
                    weights[total_n_index] = weights[total_n_index] + (err / (GF + o_val)) * learn_rate
                    c_out = c_out + x_data[total_n_index] * weights[total_n_index]
            err = train_y_data[i] - c_out
            iter = iter + 1
            if iter > 35:
                break
            # convergence threshold 0.001
            if abs(math.pow((train_y_data[i] - c_out),2)) <= 0.001:
               convergence = True 

def CMAC_test(d_type, c_type):
    c_error = 0 #cumulative error
    if d_type == 'train':
        i_data = train_x_data
        t_output = train_y_data
        t_indices = train_index
    else :
        i_data = test_x_data
        t_output = test_y_data
        t_indices = train_index
    c_out = [0 for i in range(0, len(i_data))]

    for i in range(0, len(i_data)):
        if d_type == 'train':
            dex = t_indices[i]
        else :
            dex = (np.abs(np.array(x_data)- i_data[i])).np.argmin()

        e_index = float((x_data[dex] - i_data[i])/ step_size)
        #slidding window to left,  overlapping partially 
        if e_index <0:
            max_offset =  0
            min_offset = -1
        #slidding window to right, overlapping partially
        elif e_index > 0:
            max_offset = 1
            min_offset = 0

        else: 
            max_offset = 0
            min_offset = 0 
        
        for j in range(min_offset, GF+ max_offset):
            total_n_index = dex - (j - n_index)
            if total_n_index >= 0 and n_index < size_x_data:
                if j is min_offset:
                    if c_type == 'Discrete':
                        w = weights[total_n_index]
                    if c_type == 'Continuous':
                        w = weights[total_n_index] * (1- abs(e_index))
                elif j is GF + max_offset:
                    if c_type  == 'Discrete':
                        w = 0
                    if c_type == 'Continuous':
                        w = weights[total_n_index] * abs(e_index)
                else:
                    w = weights[total_n_index]
                
                c_out[i] += x_data[total_n_index] * w

        c_error += abs(powerEval(t_output[i], c_out[i]))
        print('CMAC:', c_out)
    return c_out, c_error
        
def powerEval(a, b):
    reult_ev = math.pow((a - b),2)
    return reult_ev            


# Defining CMAC whose inputs are either discrete or continous
def CMAC(model_type):
    i = 0
    timer = time.time()
    while i < 20:
        # Training the CMAC model 
        CMAC_train()
        # Estimating error for train and test weights
        CMAC_train_y, train_c_error = CMAC_test('train', model_type)
        err_train = train_c_error / size_x_data
        CMAC_test_y, test_c_error = CMAC_test('test', model_type)
        err_test = test_c_error / size_test_data
        i = i+1
    timer = time.time() - timer
    #plotting train vs test CMAC output
        
    return err_train, err_test

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
# generalization factor
GF = 5
# neighbourhood index
n_index = int(math.floor(GF / 2))
learn_rate = 0.15



TrainErrorDiscrete, TestErrorDiscrete = CMAC('Discrete')