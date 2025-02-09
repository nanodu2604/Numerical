import tkinter as tk
from tkinter import ttk
from Methods import Bisection
from graph import Bis_Graph
class BisectionGui(tk.Frame):
    namepage="BisectionGui"
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=ttk.Label(self,text="Bisection method")
        label.grid(row = 0, column = 40, padx = 10, pady = 10)

        #navigation
        button1=ttk.Button(self,text="Main",command=lambda: controller.showFrame("Main"))
        button1.grid(row = 1, padx = 10, pady = 10)

        #make the input field
        ilable=ttk.Label(self,text="Fill interval and f(x)")
        ilable.grid(row=1,column=2)

        #interval input
        interval_label=ttk.Label(self,text="Make the interval:")
        interval_label.grid(row=2,column=2)
        self._open_var=tk.BooleanVar()
        open_interval=ttk.Combobox(self,textvariable=self._open_var)
        open_interval["values"]=("[","(")
        open_interval.bind("<<ComboboxSellected>>",self._open_var.set(open_interval.get()=="("))
        open_interval.current(0)
        open_interval.grid(column=3,row=2)
        
        # lower and upper field
        self._a=tk.DoubleVar()
        lower=ttk.Entry(self,textvariable=self._a)
        lower.grid(row=2,column=4)
        self._b=tk.DoubleVar()
        upper=ttk.Entry(self,textvariable=self._b)
        upper.grid(column=5,row=2)
        self._close_var=tk.BooleanVar()
        close_interval=ttk.Combobox(self,textvariable=self._close_var)
        close_interval["values"]=("]",")")
        close_interval.bind("<<ComboboxSellected>>",self._close_var.set(close_interval.get()=="]"))
        close_interval.current(0)
        close_interval.grid(column=6,row=2)
        
        #expression input
        expression_label=ttk.Label(self,text="f(x)=")
        expression_label.grid(row=3,column=2)
        self._expression=tk.StringVar()
        expression_text=ttk.Entry(self,textvariable=self._expression)
        expression_text.grid(row=3,column=3)

        #Tolenrant field
        self._tolerent_var=tk.DoubleVar()
        tolerent_label=ttk.Label(self,text="Enter the tolerent: ")
        tolerent_label.grid(row=4,column=2)
        tolerent_text_box=ttk.Entry(self,textvariable=self._tolerent_var)
        tolerent_text_box.grid(row=4,column=3)

        #Calculate buttom
        cal_but=ttk.Button(self,text="Calculate")
        cal_but.bind("<Button-1>",self.show_output)
        cal_but.grid(row=5,column=3)

        #Out put frame set up
        self.out_frame=tk.Frame(self)
        self.out_frame.grid(row=7,column=3)
        self.out_frame.grid_remove()

        #create a label attached to the out_frame
        self.out_label=tk.Label(self.out_frame)
        self.out_label.grid(row=0,column=0)

        #Graph button
        graph_but=ttk.Button(self.out_frame,text="Graph")
        graph_but.bind("<Button-1>",self.show_graph)

    #show the output
    def show_output(self,event):
        try:
            #get input and calculate the bisection
            expression=self._expression.get().strip()
            a=self._a.get()
            b=self._b.get()
            tol=self._tolerent_var.get()
            if not expression:
                raise ValueError("The Expression is empty, try again later")
            self._res_obj=Bisection(expression=expression,a=a,b=b,tol=tol)
            self._res=self._res_obj.bisect(open=self._open_var.get(),close=self._close_var.get())
            template=f"""Result: \n
            {self._res}
            """
            #configure the out_label
            self.out_label.config(text=template)

            #raise the out_frame
            self.out_frame.grid()
            self.out_frame.lift()
            
        except ValueError as v:
            self.out_label.config(text=f"Error: {v}, please try again")
        except Exception as e:
            print("Error: ",e)
    
    def show_graph(self,event):
        graph=Bis_Graph(a=self._a.get(),b=self._b.get(),res=self._res,f=self._res_obj.f(self._res),f_string=self._expression.get(),master=self.out_frame)
        graph.plot()

