from sympy import *
#from math import *
# 1. insert math. before sin cos log pow sqrt ...
# 2. find a way using sympy to calculate it
x, m = symbols('x m')
Y = 1 / (1 + sin(x) ** 2 + m ** 2)
print(type(Y))
print(diff(Y, x))

y = eval("1+x",{"x":1})


a = symbols("b")
print(diff(cos(a), a))
print(diff(eval("cos(a)"), a))

print("type",type(eval("cos(a)")))
class err_progation(object):

    def __init__(self,Name,args,func,errs):
        self.rank = len(args)
        self.k = list(args.keys())
        self.sk = [symbols(n) for n in self.k]
        self.v = list(args.values())
        self.p = [diff(func,n) for n in self.k]
        self.pnum = [diff(func,n).evalf(subs = args) for n in self.k]
        self.platex = [latex(diff(func,n)) for n in self.k]
        self.unc = [self.pnum[n]*list(errs.values())[n] for n in range(self.rank)]
        self.uncall = sum([n**2 for n in self.unc])**0.5
        #print(self.p,self.pnum,self.platex)
        print(self.unc,self.uncall)
        '''
        print(self.sk)
        print(self.k)
        print(diff(eval(func),self.sk[0]))
        print(diff(func,self.k[0]))
        print(latex(diff(func,self.k[0])))

        print(diff(func,self.k[0]).evalf(subs = args))
print("\n")
        for n in range(len(args)):
            print("%s : %s = %f\n %s"%(self.k[n],str(diff(eval(func),self.sk[n])),eval(str(diff(eval(func),self.sk[n])),args),latex(diff(func,self.k[0]))))'''
        for n in range(len(args)):
            #print("%s : %s = %f\n %s"%(self.k[n],str(diff(func,self.k[n])),diff(func,self.k[n]).evalf(subs = args),latex(diff(func,self.k[n]))))
            print("%s : \n%s = %f\n latex : %s\n uncertainty caused by %s:%f"%(self.k[n],str(self.p[n]),self.pnum[n],str(self.platex[n]),self.k[n],self.unc[n]))
            """ print("\n")
            print("\n")
            
            pprint(diff(func,self.k[n])) """

        print("The uncertainty is ",self.uncall)
        print("latex:\n\sigma_{%s} = \sqrt{"%(Name))
        for n in range(len(args)):
            print('\left( %s \sigma_{%s} \\right)^2'%(self.platex[n],self.k[n]))
            if n!=self.rank-1:
                print("+")
        print("}")
        #args.keys() 
err_progation("f",{"x":1,"m":2},"1 / (1 + sin(x) ** 2 + m ** 2)",{"x":0.01,"m":0.01})
