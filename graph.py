import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
#graph
class Bis_Graph():
    def __init__(self,a,b,res,f,master,f_string):
        self._master=master
        self._fig,self._ax=plt.subplots()
        self._canvas=FigureCanvasTkAgg(self._fig,self._master)
        self._x=np.linspace(a,b,600)
        self._y=f(self._x)
        self._sol=res
        self._fsol=f(res)
        self._f=f
        self._f_string=f_string
        
    def plot(self):
        self._ax.scatter(self._sol,self._fsol,color="red")
        self._ax.plot(self._x,self._y,label=f"f(x)={self._f_string}")
        self._ax.set_title("Bisection method")
        self._ax.set_xlabel("x")
        self._ax.set_ylabel("y")
        self._fig.legend()
        self._canvas.draw()
        toolbar = NavigationToolbar2Tk(self._canvas, self._master)
        toolbar.update()
        self._canvas.get_tk_widget().pack()

        