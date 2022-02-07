import statistics

import numpy

import Function
import matplotlib.pyplot as plt

list=Function.open_data()
Function.print_data_settings(list)
print("\nvalori già acquisiti")
point=Function.print_data(list)
plt.scatter(point[0][:],point[1][:])
plt.show()
if Function.digital_question("Do you want to delete the latest point?"):
    list=list[:len(list)-1]
    list[0]=list[0]-1
    Function.save_data(list[:len(list)-1])
if Function.digital_question("Do you want to make the linear regretion?"):
    x=[]
    y=[]
    for el in list[7:]:
        x.append(el[1])
        y.append(el[0]/6400*60)
    model=Function.linear_regression(x,y)
    print(model)
    x_t=numpy.linspace(0,5,1000)
    x_t=numpy.array(x)

    y_t=(model.coef_.mean()*x_t+model.intercept_)
    plt.plot(x_t,y_t)
    plt.scatter(x, y)
    plt.show()
    res=[]
    for el in list[7:]:
        res.append(abs(el[0]/6400*60-model.coef_.mean()*el[1]+model.intercept_))
    plt.figure()
    plt.plot([i for i in range(0,len(res))],res)
    plt.show()
    std=statistics.stdev(res)
    print(std)
    Function.save_data([model,std])