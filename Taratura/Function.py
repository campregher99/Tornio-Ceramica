import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from math import *
import pickle
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def remove_time(list,time):
    indexes = []
    for i, element in enumerate(list):
        if element > time:
            indexes.append(i)
    return indexes

def normalize_list(list_to_norm,ref_list):
    mul = int(len(ref_list) / len(list_to_norm))
    normalized = []
    for el in list_to_norm:
        for i in range(mul):
            normalized.append(el)
    return normalized

def read_date(date):
    date
    return datetime.strptime(date, '%d/%m/%Y  %H:%M:%S,%f')

def remove_outliers(list):
    isFinished=False
    copy=list.copy()
    indexes=[]
    while not isFinished:
        mean=np.mean(copy)
        std=np.std(copy)*2
        isFinished=True
        for (i,el) in enumerate(list):
            if (el>mean+std or el<mean-std) and el in copy:
                copy.remove(el)
                indexes.append(i)
                isFinished=False
    return indexes

def remove_under(list,limit):
    indexes = []
    for i,element in enumerate(list):
        if element < limit:
            indexes.append(i)
    return indexes

def read_names_url_txt(url):
    names = []
    for element in urllib.request.urlopen(url):
        names.append(element.decode('utf-8').strip('\n'))
    return names

def open_data():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = open(file_path, "rb")
    return pickle.load(file)

def linear_regression(x,y):
    x_array=np.array(x).reshape((-1,1))
    y_array=np.array(y)
    model=LinearRegression()
    model.fit(x_array,y_array)
    return model

def digital_question(question):
    while True:
        print(question + "(y/n)")
        ans = str(input())
        if len(ans) == 1 and ("y" in ans or "n" in ans):
            break
    if ans == "y":
        return True
    else:
        return False

def integer_question(question):
    while True:
        print(question)
        isExept = False
        try:
            number = int(input())
        except:
            isExept = True
        if not isExept:
            return number

def float_question(question):
    while True:
        print(question)
        isExept=False
        try:
            number = float(input())
        except:
            isExept=True
        if not isExept:
            return number

def plot_data(data_x,data_y,label_x="x",label_y="y"):
    plt.scatter(data_x, data_y)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.show()

def save_data(data):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename()
    file = open(file_path, "wb")
    pickle.dump(data,file)

def mobile_mean(list,step):
    max_i=len(list)-step
    meaned=[]
    for i in range(max_i):
        meaned.append(np.mean(list[i:i+step]))
    return meaned

def prepare_arrays(masses_X, masses_value_y, std_dev='0'):

    masses_X = [[masses_X[i]] for i in range(len(masses_X))]

    masses_X = np.array(masses_X)
    #masses_value_Y_ = [[masses_value_y[i]] for i in range(len(masses_value_y))]
    #masses_value_Y_ = np.array(masses_value_Y_)
    masses_value_y = np.array(masses_value_y)

    '''
    # Split the data into training/testing sets
    masses_X_train = masses_X[:-20]
    masses_X_test = masses_X[-20:]

    # Split the targets into training/testing sets
    means_y_train = means_y[:-20]
    means_y_test = means_y[-20:]
    '''

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(masses_X, masses_value_y)

    # Make predictions using the testing set
    means_y_pred = regr.predict(masses_X)

    reg_coeff = regr.coef_
    mean_squared_er = round(mean_squared_error(masses_value_y, means_y_pred), 20)
    dev_std = sqrt(mean_squared_er)
    det_coeff = round(r2_score(masses_value_y, means_y_pred), 20)

    # The coefficients
    print("Coefficients: \n", reg_coeff)
    # The mean squared error
    print(f"Mean squared error: {mean_squared_er}")
    print(f"stddev: {dev_std}")
    # The coefficient of determination: 1 is perfect prediction
    print(f"Coefficient of determination: {det_coeff}")

    # Plot outputs
    plt.scatter(masses_X, masses_value_y, color="black")
    plt.plot(masses_X, means_y_pred, color="blue", linewidth=3)


    plt.xlabel('mass [g]')
    plt.ylabel('signal [V]')
    plt.title('Taratura Statica')
    plt.show()

def print_data_settings(data):
    print("acquisizioni già fatte:\t" + str(data[0]))
    print("velocità minima impostata:\t" + str(data[1]))
    print("velocità massima impostata:\t" + str(data[2]))
    print("riduzione attuata:\t" + str(data[3]))
    print("numero di parti in cui viene diviso il range di velocità:\t" + str(data[4]))
    print("numero di ripetizioni della rampa di acquisizioni:\t" + str(data[5]))
    print("il valore che viene mostrato della velocità è in Hz:\t" + str(data[6]))
    print("rilevazioni totali:\t" + str(data[5] * data[4] * 2))
    print("rilevazioni rimanenti:\t" + str(data[5] * data[4] * 2 - data[0]))

def print_data(data):
    print("vel \tvolt")
    X=[]
    Y=[]
    for el in data[7:]:
        print(str(el[0])+"\t"+str(el[1]))
        Y.append(el[0])
        X.append(el[1])
    return [X,Y]