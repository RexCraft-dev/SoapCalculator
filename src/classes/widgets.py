import tkinter as tk
from tkinter import ttk


class AcidBar(tk.Frame):
    def __init__(self, parent, acid):
        super().__init__(parent)

        self.acid_value = tk.IntVar(value=0)

        self.label = ttk.Label(self, text=acid, width=15)
        self.operands = ttk.Combobox(self, values=['>', '<'], width=2)
        self.operands.set('-')
        self.value_box = ttk.Entry(self, textvariable=self.acid_value, width=3)

        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.operands.grid(row=0, column=1, padx=5, pady=5)
        self.value_box.grid(row=0, column=2, padx=5, pady=5)