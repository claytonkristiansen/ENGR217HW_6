import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from statistics import mean

def OpenFile(file_name):
    file = open(file_name)

    # Check to see if the file is empty
    row = file.readline()  # read the first line that has column headers
    if row == '':
        quit('The file is empty.')
    else:
        header = row.split()  # creates a list of strings

    row = file.readline()  # read the first line that has data
    row = row.split()  # creates a list
    row = [float(i) for i in row]  # convert strings to floating point numbers
    data = []
    data.append(np.array([]))
    data.append(np.array([]))
    data[0] = np.append(data[0], row[0])
    data[1] = np.append(data[1], row[1])
    row = file.readline()
    while row != '':
        row = row.split()
        row = [float(i) for i in row]
        data[0] = np.append(data[0], row[0])
        data[1] = np.append(data[1], row[1])
        row = file.readline()
    return data
    file.close()


data1 = OpenFile("data1.txt")
data2 = OpenFile("data2.txt")

p0 = np.polyfit(data1[0], data1[1], 1)

y0 = p0[0] * data1[0] + p0[1]
plt.plot(data1[0], data1[1], 'rp', data1[0], y0, 'b--')
plt.show()
print('Slope is ' + str(p0[0]) + ", and intercept is " + str(p0[1]))

p1 = np.polyfit(data2[0], data2[1], 1)
p2 = np.polyfit(data2[0], data2[1], 2)
p3 = np.polyfit(data2[0], data2[1], 3)

y1 = p2[0] * data2[0] + p2[1]
y2 = np.polyval(p2, data2[0])
y3 = np.polyval(p3, data2[0])
e1 = data2[1] - y1
e2 = data2[1] - y2
e3 = data2[1] - y3
MSE1 = mean(e1 ** 2)
MSE2 = mean(e2 ** 2)
MSE3 = mean(e3 ** 2)
plt.plot(data2[0], data2[1], 'rp', data2[0], y1, 'b--', data2[0], y2, 'b--', data2[0], y3, 'b--')
print('The mean squared error is ' + str(MSE1) + ' for the linear model')
print('The mean squared error is ' + str(MSE2) + ' for the quadratic model')
print('The mean squared error is ' + str(MSE3) + ' for the cubic polynomial model')


plt.show()

p = np.array([0.6, 1, 1.4, 1.8, 2.2, 2.6, 3, 3.4, 3.8, 4.2, 4.6, 5, 5.4])
k = np.array([5.89, 4.68, 4.1, 3.45, 3.25, 2.69, 2.25, 1.92, 1.55, 1.45, 1.19, 0.99, 0.84])
logk = np.log(k)
p4 = np.polyfit(p, logk, 1)
B = p4[0]
A = np.exp(p4[1])
kFit = A * np.exp(B*p)
#kFitEst = np.polyval(p4, p)
e4 = kFit - k
MSE4 = mean(e4 ** 2)
print('MSE of log-transformed linear regression is ' + str(MSE4))
p5 = np.polyfit(p, k, 1)
kFit1 = np.polyval(p5,p)
e5 = kFit1 - k
MSE5 = mean(e5 ** 2)
print('order	MSE')
print('1        ' + str(MSE5))
i = 2
while(MSE5 >= MSE4):
    p5 = np.polyfit(p, k, i)
    kFit1 = np.polyval(p5,p)
    e5 = kFit1 - k
    MSE5 = mean(e5 ** 2)
    print(str(i) + '        ' + str(MSE5))
    i = i + 1
print('Polynomial regression of order ' + str(i - 1) + ' has a better MSE than log-transformed linear regression')
