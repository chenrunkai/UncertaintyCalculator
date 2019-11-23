from sympy import *

class err_progation(object):

    def __init__(self,Name,args,func,errs,pp = 0):
        self.rank = len(args)
        self.k = list(args.keys())
        self.sk = [symbols(n) for n in self.k]
        self.v = list(args.values())
        self.p = [diff(func,n) for n in self.k]
        self.pnum = [diff(func,n).evalf(subs = args) for n in self.k]
        self.platex = [latex(diff(func,n)) for n in self.k]
        self.unc = [self.pnum[n]*list(errs.values())[n] for n in range(self.rank)]
        self.uncall = sum([n**2 for n in self.unc])**0.5
        
        for n in range(len(args)):
            #print("%s : %s = %f\n %s"%(self.k[n],str(diff(func,self.k[n])),diff(func,self.k[n]).evalf(subs = args),latex(diff(func,self.k[n]))))
            print("the derivative of %s with respect to %s : \n%s = %f\nlatex : %s\nuncertainty caused by %s:%f"%(Name,self.k[n],str(self.p[n]),self.pnum[n],str(self.platex[n]),self.k[n],self.unc[n]))
            if pp:
                print("")
                print("pprint:")
                pprint(self.p[n])
                print("")

        print("The uncertainty is ",self.uncall)
        print("latex:\n\sigma_{%s} = \sqrt{"%(Name))
        for n in range(len(args)):
            print('\left( %s \sigma_{%s} \\right)^2'%(self.platex[n],self.k[n]))
            if n!=self.rank-1:
                print("+")
        print("}")
 
tobec = input("please input name of variable to be calculated:\nexample : G\n")

print("please input variables , values and uncertainties ended with # # #")
print("example : \ng 9.8 0.01 \nm 1 0.001 \n# # #\n")
v = dict()
e = dict()
var,val,unc = input().split()
val,unc = float(val) ,float(unc) 
v[var] = val
e[val] = unc
while(var != '#'):
    var,val,unc = input().split()
    if var =='#':
        break
    val,unc = float(val) ,float(unc) 
    v[var] = val
    e[val] = unc
formula = input("please input formula:\nexample : m*g\n")

pp = input("pprint?0 or 1")
#print(tobec,v,formula,e,pp)
err_progation(tobec,v,formula,e,pp)

#err_progation("f",{"x":1,"m":2},"1 / (1 + sin(x) ** 2 + m ** 2)",{"x":0.01,"m":0.01},1)
