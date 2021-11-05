import tkinter
import tkinter.ttk

#from listWindow import listWindowClass
#from payWindow import payWindowClass
#from saveWindow import saveWindowClass


class mainWindow:
    def __init__(self):
        self.total = 1200
        self.target = 4500
        # creating tkinter window
        self.root = Tk()

        #TEXT

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
#        self.progressLabelText = StringVar()
#        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")
#
#        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
#        self.progressLabel.pack()
#        self.progress = Progressbar(self.root, orient = HORIZONTAL,
#                    length = 250, mode = 'determinate')
#        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
#        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()

if __name__ == '__main__':
    main = mainWindow()
