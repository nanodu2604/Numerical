import tkinter as tk

# The multi-line template string
template = """Hello World
This is my name"""

def add_text_area():
    # Create a new Text widget
    new_text = tk.Text(root, width=30, height=5)
    new_text.pack(pady=5)
    
    # Insert the template text into the Text widget
    new_text.insert("1.0", template)

# Create the main application window
root = tk.Tk()
root.title("Dynamic Text with Template")
root.geometry("300x300")

# Add the button
button = tk.Button(root, text="Add Text Area", command=add_text_area)
button.pack(pady=10)

# Start the main event loop
root.mainloop()
