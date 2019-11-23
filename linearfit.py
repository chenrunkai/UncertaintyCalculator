import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy
 
 
def f_1(x, A, B):
 return A * x + B
 
plt.figure()
# 拟合点
x0 = [75, 70, 65, 60, 55,50,45,40,35,30]
y0 = [22.44, 22.17, 21.74, 21.37, 20.92,20.67,20.32,20.05,19.84,19.59]
 
x1 = [1,2,3]
y1 = [1,2  ,3]
print(dir(scipy))
print(scipy.stats.linregress( x1,y1))

# 绘制散点
plt.scatter(x0[:], y0[:], 3, "red")
 
# 直线拟合与绘制
A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
print( optimize.curve_fit(f_1, x1, y1))

x1 = np.arange(30, 75, 0.01)#30和75要对应x0的两个端点，0.01为步长
y1 = A1 * x1 + B1
plt.plot(x1, y1, "blue")
print(A1)
print(B1)
plt.title(" ")
plt.xlabel('t')
 
plt.ylabel('Mt/g')
#plt.show()