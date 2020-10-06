import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.57, 1.34, 2.58, -.23, -6.35, -3.97])
p = np.polyfit(x, y, 1)
yFit = p[0] * x + p[1]
plt.plot(x, y, 'rd', x, yFit, 'b--')


from math import sqrt
n = len(x)
r = (n*sum(x*y) - sum(x)*sum(y))/(sqrt(n*sum(x**2)-sum(x)**2)*sqrt(n*sum(y**2)-sum(y)**2))
r2 = r**2


t = np.arange(0, 61, 5)
Activity = np.array([5017, 4257, 3496, 3003, 2511, 2117, 1778, 1560, 1289, 1060, 902, 773, 653])
# transform using natural log
logActivity = np.log(Activity)
# perform linear regression using polyfit
# p[0] is slope
# p[1] is intercept
p = np.polyfit(t, logActivity, 1)
# back-transform parameters
b = np.exp(p[1])
m = p[0]

x = np.array([Index for Index in range(2, 13)])
y = np.array([3.19, 2.23, -1.97, -2.13, -3.43, -2.18, -3.89, -1.67, 0.55, 3.40, 6.74])
p = np.polyfit(x, y, 2)  # it’s 2 for a quadratic!
yFit = p[0] * x ** 2 + p[1] * x + p[2]
import matplotlib.pyplot as plt
plt.plot(x, y, 'rp', x, yFit, 'b--')




x = np.array([Index for Index in range(2, 13)])
y = np.array([3.19, 2.23, -1.97, -2.13, -3.43, -2.18, -3.89, -1.67, 0.55, 3.40, 6.74])
p = np.polyfit(x, y, 2)
# yFit = p(1)*x**2 + p(2)*x + p(3);
yFit = np.polyval(p, x)  # using polyval instead of writing out the polynomial
import matplotlib.pyplot as Plt
Plt.plot(x, y, 'rp', x, yFit, 'b--')



x = np.array([Index for Index in range(2, 13)])
y = np.array([3.19, 2.23, -1.97, -2.13, -3.43, -2.18, -3.89, -1.67, 0.55, 3.40, 6.74])
p = np.polyfit(x, y, 2)
yFit = np.polyval(p, x)
e = y - yFit
from statistics import mean
MSE = mean(e ** 2)
import matplotlib.pyplot as plt
plt.plot(x, y, 'rp', x, yFit, 'b--')
print('The MSE of this quadratic regression is ', MSE)


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
    data = np.array([row])  # creates a 2-D array; notice the use of square brackets
    row = file.readline()
    while row != '':
        row = row.split()
        row = [float(i) for i in row]
        data = np.append(data, [row], axis=0)  # concatenates the 2-D array; notice the use of square brackets
        row = file.readline()
    return data
    file.close()


data1 = OpenFile("data1.txt")
data2 = OpenFile("data2.txt")

