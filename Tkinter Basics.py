import tkinter
screen= tkinter.Tk()
screen.geometry("800x800")
screen.title("Basics")
screen.configure(background= "red")
label= tkinter.Label(screen, text="Hello")
label.pack()
entry= tkinter.Entry(screen, text= "Entry")
entry.pack()
text= tkinter.Text(screen)
text.pack()
button= tkinter.Button(screen, text="Button")
button.pack()
screen.mainloop()