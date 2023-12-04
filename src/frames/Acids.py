import tkinter as tk
from tkinter import ttk
from src.classes.widgets import AcidBar

class AcidFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.lauric_frame = AcidBar(self, 'Lauric Acid')
        self.lauric_frame.grid(row=0, column=0)

        self.myristic_frame = AcidBar(self, 'Myristic Acid')
        self.myristic_frame.grid(row=1, column=0)

        self.palmitic_frame = AcidBar(self, 'Palmitic Acid')
        self.palmitic_frame.grid(row=2, column=0)

        self.stearic_frame = AcidBar(self, 'Stearic Acid')
        self.stearic_frame.grid(row=3, column=0)

        self.oleic_frame = AcidBar(self, 'Oleic Acid')
        self.oleic_frame.grid(row=4, column=0)

        self.linoleic_frame = AcidBar(self, 'Linoleic Acid')
        self.linoleic_frame.grid(row=5, column=0)

        self.linolenic_frame = AcidBar(self, 'Linolenic Acid')
        self.linolenic_frame.grid(row=6, column=0)