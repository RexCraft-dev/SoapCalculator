import tkinter as tk
from tkinter import ttk
from src.classes.ingredients import Ingredients


class ListIngredients(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.list_title = ttk.Label(self, text='Oils, Fats, and Waxes')
        self.list_title.grid(row=0, column=0, sticky='nsew', columnspan=2)

        self.list_options = ttk.Combobox(self, values=['All', 'Oil', 'Fat', 'Wax', 'Acid'])
        self.list_options.set('All')
        self.list_options.grid(row=1, column=0, sticky='nsew')

        self.list_ofw = tk.Listbox(self, height=25, width=30)
        self.list_ofw.grid(row=2, column=0, sticky='nsew', rowspan=3, columnspan=2)

        self.view_ofw = tk.Frame(self)
        self.view_ofw.grid(row=5, column=0, sticky='nsew')

        self.lbl_name = ttk.Label(self.view_ofw, text='', width=20, font='Calibri 12')
        self.lbl_name.grid(row=0, column=0, sticky='w', columnspan=2)

        self.lbl_lauric = ttk.Label(self.view_ofw, text='Lauric', width=10)
        self.lbl_lauric.grid(row=1, column=0, sticky='w')

        self.lbl_myristic = ttk.Label(self.view_ofw, text='Myristic', width=10)
        self.lbl_myristic.grid(row=2, column=0, sticky='nsew')

        self.lbl_palmitic = ttk.Label(self.view_ofw, text='Palmitic', width=10)
        self.lbl_palmitic.grid(row=3, column=0, sticky='nsew')

        self.lbl_stearic = ttk.Label(self.view_ofw, text='Stearic', width=10)
        self.lbl_stearic.grid(row=4, column=0, sticky='nsew')

        self.lbl_ricinoleic = ttk.Label(self.view_ofw, text='Ricinoleic', width=10)
        self.lbl_ricinoleic.grid(row=5, column=0, sticky='nsew')

        self.lbl_oleic = ttk.Label(self.view_ofw, text='Oleic', width=10)
        self.lbl_oleic.grid(row=6, column=0, sticky='nsew')

        self.lbl_linoleic = ttk.Label(self.view_ofw, text='Linoleic', width=10)
        self.lbl_linoleic.grid(row=7, column=0, sticky='nsew')

        self.lbl_linolenic = ttk.Label(self.view_ofw, text='Linolenic', width=10)
        self.lbl_linolenic.grid(row=8, column=0, sticky='nsew')

        self.val_lauric = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_lauric.grid(row=1, column=1, sticky='nsew')

        self.val_myristic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_myristic.grid(row=2, column=1, sticky='nsew')

        self.val_palmitic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_palmitic.grid(row=3, column=1, sticky='nsew')

        self.val_stearic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_stearic.grid(row=4, column=1, sticky='nsew')

        self.val_ricinoleic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_ricinoleic.grid(row=5, column=1, sticky='nsew')

        self.val_oleic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_oleic.grid(row=6, column=1, sticky='nsew')

        self.val_linoleic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_linoleic.grid(row=7, column=1, sticky='nsew')

        self.val_linolenic = ttk.Label(self.view_ofw, text='0', width=3)
        self.val_linolenic.grid(row=8, column=1, sticky='nsew')

        # Sample data to populate the Listbox
        self.ingredients = Ingredients()

        self.ingredient_list = self.ingredients.list_ingredients()

        # Insert items into the Listbox
        for ingredient in self.ingredient_list:
            self.list_ofw.insert(tk.END, ingredient.title())

        self.list_ofw.bind('<<ListboxSelect>>', self.update_selection)
        self.list_options.bind('<<ComboboxSelected>>', self.filter_list)

    def update_selection(self, event):
        # Get the selected index
        selected_index = event.widget.curselection()

        if selected_index:
            # Get the value at the selected index
            selected_value = event.widget.get(selected_index[0])
            selected_ingredient = self.ingredients.get_ingredient(name=selected_value)

            self.val_lauric.configure(text=str(int(selected_ingredient['lauric'])))
            self.val_myristic.configure(text=str(int(selected_ingredient['myristic'])))
            self.val_palmitic.configure(text=str(int(selected_ingredient['palmitic'])))
            self.val_stearic.configure(text=str(int(selected_ingredient['stearic'])))
            self.val_ricinoleic.configure(text=str(int(selected_ingredient['ricinoleic'])))
            self.val_oleic.configure(text=str(int(selected_ingredient['oleic'])))
            self.val_linoleic.configure(text=str(int(selected_ingredient['linoleic'])))
            self.val_linolenic.configure(text=str(int(selected_ingredient['linolenic'])))

            # Update the label with the selected value
            self.lbl_name.config(text=selected_value)

    def filter_list(self, event):
        # Use get method to get the selected item from the Combobox
        selected_filter = event.widget.get()

        if selected_filter:
            selected_filter_lower = selected_filter.lower()

            self.list_ofw.delete(0, tk.END)

            if selected_filter_lower == 'all':
                for ingredient in self.ingredient_list:
                    self.list_ofw.insert(tk.END, ingredient.title())
            else:
                for item in self.ingredient_list:
                    data = self.ingredients.get_ingredient(item)
                    if data['type'] == selected_filter_lower:
                        self.list_ofw.insert(tk.END, item.title())


if __name__ == "__main__":
    root = tk.Tk()
    app = ListIngredients(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
