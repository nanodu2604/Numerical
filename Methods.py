from Input_Proccessing import Expression, Interval_check
import numpy as np
class Bisection:
    _a=None
    _b=None
    _tol=None
    def __init__(self,expression,a,b,tol):
        self._expression_obj=Expression(expression=expression)
        self._a=a
        self._b=b
        self._tol=tol
    
    def f(self,*args):
        return self._expression_obj.f(*args)

    def bisect(self,open,close):
        interval=Interval_check(self._a,self._b,open,close)
        i=1
        max_iter=100
        while self._tol<=((self._b-self._a)/2):
            p=(self._a+self._b)/2
            if not interval.compare(p):
                raise ValueError(f"The solution is out of range in [{self._a},{self._b}]")
            if (self._expression_obj.f(self._a)*self._expression_obj.f(p)>0) and (self._expression_obj.f(self._b)*self._expression_obj.f(p)<0):
                self._a=p
            elif (self._expression_obj.f(p)*self._expression_obj.f(self._b)>0) and (self._expression_obj.f(self._a)*self._expression_obj.f(p)<0):
                self._b=p
            elif (self._expression_obj.f(p)*self._expression_obj.f(self._b)==0):
                return p
            i+=1
            if i>max_iter:
                raise ValueError(f"The iteration limit has been reached at iteration number: {i} and at value is {p} since the solution is out of range")
        return p,i

class Fixpoint:
    _a=None
    _b=None
    _tol=None
    
    def __init__(self,expression,a,b,tol):
        self._expression_obj=Expression(expression=expression)
        self._a=a
        self._b=b
        self._tol=tol

    def f(self,*args):
        return self._expression_obj.f(*args)
    
    def fixpoint(self, p0,open,close):
        i = 1
        interval=Interval_check(self._a,self._b,open,close)
        N=100 # max_iter
        while i <= N:
            p = self._expression_obj.f(p0)
            if interval.compare(p):
                raise ValueError(f"Method yield no root in [{self._a},{self._b}]")
            if abs(p - p0) < self._tol:
                return p  # return p instead of p0
            else:
                p0 = p
                i += 1
        return None

class Lagrange:
    def __init__(self,x:list,y:list):
        self._x=np.array(x)
        self._y=np.array(y)
        if len(self._x)!=len(self._y):
            raise ValueError("The length of the x and y must be equal")
    
    def interpolation_polynomial(self):
        np.vander(self._x,increasing=True)
        inverse_x = np.linalg.inv(self._x)
        return np.flip(inverse_x@self._y)
'''
class Derivative:
    def __init__(self,expression,x,h,):
'''