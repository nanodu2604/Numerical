import tkinter as tk
from tkinter import ttk
from Bisectiongui import BisectionGui
from Fixpointgui import FixpointGui
from tkinter import font

#set up the window
class Master(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #set up the window
        #self.state("zoomed")
        self.title("Numerical analyis")
        
        #container set up
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(index=0,weight=1)
        container.grid_columnconfigure(index=0, weight=1)
        
        #make frames dictionary, initial frames
        self.frames={}
        #loop through the pages to add to the frames
        for F in (Main,BisectionGui,FixpointGui):
            frame=F(container,self)
            self.frames[F.namepage]=frame

            #sketch the frame
            frame.grid(row=0,column=0,sticky="nsew")

        # show the main frame first 
        self.showFrame("Main")


    #show the frame
    def showFrame(self,page):
        frame=self.frames[page]
        frame.tkraise()

class Main(tk.Frame):
    namepage="Main"
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=ttk.Label(self,text="Numerical Analysis App",font=font.Font(family="Edwardian Script ITC",size=20))
        label.grid(row = 0, column = 40, padx = 10, pady = 10) 
        button1 = ttk.Button(self, text ="Bisection",command = lambda : controller.showFrame("BisectionGui"))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Fixpoint",command = lambda : controller.showFrame("FixpointGui"))
        button2.grid(row=2,column=1,padx=10,pady=10)





master=Master()
master.mainloop()
