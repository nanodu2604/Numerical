from Input_Proccessing import Expression
class Bisection:
    _a=None
    _b=None
    _tol=None
    _status=None

    def __init__(self,expression,a,b,tol):
        self._expression_obj=Expression(expression=expression)
        self._a=a
        self._b=b
        self._tol=tol
    
    def f(self,*args):
        return self._expression_obj.f(*args)

    def bisect(self):
        i=1
        max_iter=100
        while self._tol<=((self._b-self._a)/2):
            p=(self._a+self._b)/2
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