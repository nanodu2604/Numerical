import tkinter as tk 
from tkinter import ttk 
  
# Creating tkinter window 
window = tk.Tk() 
window.geometry('350x250') 
# Label 
ttk.Label(window, text = "Select the Month :",  
        font = ("Times New Roman", 10)).grid(column = 0,  
        row = 15, padx = 10, pady = 25) 
  
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June',  
                          ' July',  
                          ' August',  
                          ' September',  
                          ' October',  
                          ' November',  
                          ' December') 
  
monthchoosen.grid(column = 1, row = 15) 
  
# Shows february as a default value 
monthchoosen.current(1)  
def get_value():
    print(n.get())
btn = tk.Button(window, text="Get Value", command=get_value)
btn.grid(column=1, row=16)
# Create a BooleanVar
bool_var = tk.BooleanVar(value=False)

# Create a Combobox
combo = ttk.Combobox(window, values=["Option 1", "Option 2"])
combo.grid(column=1,row=20)

# Function to handle the selection
def on_select(event):
    bool_var.set(combo.get() == "Option 1")
    print(bool_var.get())  # Print the value of the BooleanVar

# Bind the selection event
combo.bind("<<ComboboxSelected>>", on_select)

window.mainloop() 
