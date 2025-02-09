from sympy.utilities.lambdify import lambdify
from sympy import parse_expr
from sympy import Interval

#Evaluate expression in sympy library
class Expression:
    _variables=[]
    def __init__(self,expression:str):
        self._expression=parse_expr(expression,evaluate=False)
        self._variables=self._extract_variable()
        self._f=lambdify(self._variables,self._expression)

    #separate the variables from the expression
    def _extract_variable(self)->list: 
        return list(self._expression.free_symbols)
    
    def getfunction(self):
        return self._expression
    
    def f(self,*args)->float:
        return self._f(*args)
    
    def get_variables(self):
        return self._variables

class Interval_check:
    def __init__(self,a,b,open_interval,close_interval):
        self._a=a
        self._b=b
        self._interval=Interval(a,b,left_open=open_interval,right=close_interval)
    def compare(self,num):
        return self._interval.contains(num)
        
#class Dataset:
    

