from tkinter import *
from tkinter import ttk

import random

#Variables
WHITE = '#FFFFFF'

#Creating a basic window
window = Tk()
window.title("Algorithms Visualizer")
window.maxsize(1000, 700)
window.config(bg = WHITE)



#User Interface
UI_frame = Frame(window, width=900, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)


#Canvas
main_canvas = Canvas(window, width=800, height=400, bg=WHITE)
main_canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()