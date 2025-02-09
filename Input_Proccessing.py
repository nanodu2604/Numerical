from sympy.utilities.lambdify import lambdify
from sympy import parse_expr


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


    
