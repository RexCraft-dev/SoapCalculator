import tkinter as tk
from tkinter import ttk
from src.frames.Acids import AcidFrame
from src.frames.ListIngredients import ListIngredients


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Left Frame
        frame = tk.Frame(self)
        frame.grid(row=0, column=0)

        title_label = ttk.Label(frame, text='Soap Calculator', font='Calibri 20', background='green')
        title_label.grid(row=0, column=0, sticky='nsew')

        acid_frame = AcidFrame(frame)
        acid_frame.grid(row=1, column=0, sticky='nsew')

        list_frame = ListIngredients(frame)
        list_frame.grid(row=1, column=1, sticky='nsew')

