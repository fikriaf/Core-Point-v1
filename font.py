import tkinter as tk
from tkinter import *
import time


def change_font(stop=None):
    n=0
    with open("font.txt", "r") as font_file:
        font_list = font_file.readlines()
        for line in font_list:
            if stop is not None:
                break
            n+=1
            label = Label(root, bg="black", text=line, fg="white", font=(line.strip(), 18), width=194, height=2, anchor="w")
            label.place(x=20,y=20)
            label2 = Label(root, bg="black", text="EasyPoint", fg="white", font=(line.strip(), 18), width=194, height=2, anchor="w")
            label2.place(x=20,y=60)
            root.update()
            time.sleep(1)

root = tk.Tk()
root.title("Persegi Tanpa Sudut Runcing")




change_font_button = Button(root, text="Change Font", command=change_font)
change_font_button.pack()

stop=Button(root, text="STOP", command=change_font(stop="ya"))
stop.place(x=20,y=300)
root.mainloop()
