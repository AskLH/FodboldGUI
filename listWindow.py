# importing tkinter module
from tkinter import *
#from PIL import ImageTk,Image #image stuff - install package: Pillow
import pickle


filename = 'betalinger.pk'
fodboldtur ={}


class listWindowClass:
    def showlist(self):
        for item in fodboldtur.item():
            Label(self.listWindow, text=item)


    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger.. eller.. noget der ligner en cylinder").pack()


infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
  #      img = ImageTk.PhotoImage(Image.open("assets/img/cyl.png"))
 #       panel = Label(self.listWindow, image=img)
#        panel.image = img
#        panel.pack(side="bottom", fill="both", expand="yes")