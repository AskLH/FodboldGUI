# importing tkinter module
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


class payWindowClass:

    def __init__(self, master):
        self.master = master
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,
              text="Pay").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

        self.names = list(self.master.fodboldtur.keys())
        print(self.names[0])

        self.option_var = tk.StringVar(self.payWindow)
        self.option_var.set("Vælg et navn")


        self.label = ttk.Label(self.payWindow,).pack()

        self.option_menu = OptionMenu(
            self.payWindow,
            self.option_var,
            *self.names).pack()

    def addMoney(self):
        try:
            amount = abs(int(self.money.get()))
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        if self.option_var.get() == "Vælg et navn":
            messagebox.showerror(parent=self.payWindow, title="HALLO! - Mark Kommer ind i fede sko", message="Er\nDu\nDum?")
            return

        key=self.option_var.get()

        self.master.fodboldtur[key] += amount

        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        self.payWindow.destroy()