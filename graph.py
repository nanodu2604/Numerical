import matplotlib.pyplot as plt
import numpy as np
#graph
class Bis_Graph(plt):
    def __init__(self,a,b,res,f):
        plt.__init__(self,figsize=(5,5))
        self._x=np.linspace(a,b,600)
        self._y=f(self._x)
        self._sol=res
        self._fsol=f(res)
        
    def plot(self):
        plt.scatter(self._sol,self._fsol,color="red")
        plt.plot(self._x,self._y)
        plt.show()

