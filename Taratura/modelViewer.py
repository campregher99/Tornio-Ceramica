import Function

data=Function.open_data()
print("m della retta: " + str(data[0].coef_)+" RPM/V")
print("q della retta: " + str(data[0].intercept_)+" RPM")
print("errore massimo al 99%: +- " + str(data[1]*3)+" RPM")