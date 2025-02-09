import tkinter as tk
from tkinter import font

def display_fonts():
    root = tk.Tk()
    root.title("Available Font Families")

    # Retrieve all font families
    font_families = font.families()

    # Create a scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a listbox to display font names
    listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, width=50, height=20)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    # Demonstrate fonts
    def show_font(event):
        selected_font = listbox.get(listbox.curselection())
        demo_label.config(text=f"This is {selected_font}", font=(selected_font, 16))

    listbox.bind("<<ListboxSelect>>", show_font)

    # Add fonts to the listbox
    for family in sorted(font_families):
        listbox.insert(tk.END, family)

    # Label to demonstrate the selected font
    demo_label = tk.Label(root, text="Select a font to see it here", font=("Arial", 16))
    demo_label.pack(pady=10)

    root.mainloop()

# Run the function
display_fonts()
