import  numpy as npy
import cmath

class linear_fit(object):

    def __init__(self , x , y ,allowance_err_x = 0 , allowance_err_y = 0):
        self.x = x
        self.y = y 
        self.n = len(x)
        self.x_bar=npy.mean(x)
        self.y_bar=npy.mean(y)
        self.SSR=0
        self.Varx=0
        self.Vary=0
        for i in range(0,len(x )):
            self.SSR+=(x [i]-self.x_bar)*(y [i]-self.y_bar)
            self.Varx+=(x [i]-self.x_bar)**2
            self.Vary+=(y [i]-self.y_bar)**2
            #not divided by n
        self.SST=(self.Varx*self.Vary)**0.5
        self.result={}
        self.coef=npy.polyfit(x ,y ,1)#算出各个回归系数
        self.polynomial=self.coef.tolist()
        #self.result["polynomial"]=self.coef.tolist()
        p=npy.poly1d(self.coef)#拟合一条线
        self.y_hat=p(x )
        self.r = self.SSR/self.SST
        self.result["r"]=self.SSR/self.SST
        self.a = self.polynomial[0]
        self.b = self.polynomial[1]
        self.result["a"] = self.a
        self.result["b"] = self.b
        self.uncertaity_of_a = self.a * ((1/self.r**2-1)/(len(x )-2))**0.5
        self.result["uncertainty_of_fit"]=self.uncertaity_of_a
        self.result["uncertainty_of_allowance_err"] = (allowance_err_x*self.a+allowance_err_y)/(3*self.Varx)**0.5
        self.result["uncertainty_of_all"]=(self.result["uncertainty_of_fit"]**2+self.result["uncertainty_of_allowance_err"]**2)**0.5
        self.Varx /= self.n 
        self.Vary /= self.n
    
    def p(self):
        for n in self.result.keys():
            print(n,self.result[n])

test_x = [float(n) for n in input("x_data(seperated by " "):").split()]
test_y = [float(n) for n in input("y_data(seperated by " "):").split()]
allowance_errer_x = float(input("allowance error of x (default 0):"))
allowance_errer_y= float(input("allowance error of y (default 0):"))

f  = linear_fit(test_x,test_y,allowance_err_x=allowance_errer_x,allowance_err_y=allowance_errer_y)
#print(f.result)
f.p()
#{'polynomial': [2.65677966101695, 5.322033898305075], 'r': 0.94031007654487, 'uncertaity_of_a_fit': 0.5551494334153915, 'uncertaity_of_a_allowance_err': 0.0030730325901789134, 'uncertaity_of_a_all': 0.5551579387442195}