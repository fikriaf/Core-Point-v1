import tkinter as tk
from tkinter import *

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollbar Example")

# Create a Canvas widget
canvas = Canvas(root)
canvas.place(x=10, y=10, width=380, height=200)

# Create a vertical scrollbar
vertical_scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
vertical_scrollbar.place(x=390, y=10, height=200)

# Configure the Canvas to use the scrollbar
canvas.configure(yscrollcommand=vertical_scrollbar.set)

# Create a frame inside the Canvas to hold the content
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add content to the frame
for i in range(1, 51):
    label = Label(frame, text=f"Item {i}")
    label.pack()

# Bind the Canvas to configure event
canvas.bind("<Configure>", on_canvas_configure)

root.mainloop()
