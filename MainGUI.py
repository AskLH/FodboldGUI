import tkinter as ask
window = ask.Tk()
greeting = ask.Label(
    text="Hello, Aske",
    fg="white",
    bg="black",
    width=10,
    height=10
)
button = ask.Button(
    text="Click Aske!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
greeting.pack()
window.mainloop()
