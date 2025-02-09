import tkinter as tk

def check_empty():
    # Check if the entry is empty and restore placeholder text if needed
    if not entry.get():
        entry.delete(0, tk.END)
        entry.insert(0, placeholder_text)
        entry.config(fg="gray")
    else:
        # Continue checking after a short delay
        root.after(100, check_empty)

def on_focus_in(event):
    # Remove placeholder text when the user focuses on the Entry field
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")  # Change text color to black

def on_focus_out(event):
    # Restore placeholder text if the field is empty
    if not entry.get():
        entry.insert(0, placeholder_text)
        entry.config(fg="gray")  # Change text color to gray

# Initialize tkinter
root = tk.Tk()
root.title("Entry with Placeholder")

# Placeholder text
placeholder_text = "The input field is empty, please enter a valid expression"

# Entry field
entry = tk.Entry(root, fg="gray")  # Initial text color is gray
entry.insert(0, placeholder_text)  # Insert placeholder text
entry.pack(padx=10, pady=10)

# Bind events to handle placeholder behavior
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

# Start checking if the field is empty every 100 ms
root.after(100, check_empty)

# Run tkinter main loop
root.mainloop()
