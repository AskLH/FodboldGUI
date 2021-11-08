from tkinter import *
from tkinter.ttk import *
import pickle

class saveWindowCLass:
    def __init__(self, master):
        self.master = master
        self.saveWindow = Toplevel(self.master.root)
        self.saveWindow.title("Pay Window")
        self.saveWindow.geometry("200x200")

        Label(self.saveWindow,
              text="vil du gemme?").pack()

        YesButton = Button(self.saveWindow, text="Ja", command=self.gem)
        YesButton.pack(padx=20, pady=10, side=LEFT)

        NoButton = Button(self.saveWindow, text="Nej", command=self.master.root.destroy)
        NoButton.pack(padx=20, pady=10, side=LEFT)



    def gem(self):
        filename = 'betalinger.pk'
        outfile = open(filename, 'wb')
       # pickle.dump(fodboldtur, outfile)
        outfile.close()
        print("Dataen er gemt")
        self.master.root.destroy()
