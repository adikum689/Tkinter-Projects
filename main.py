import tkinter, random, tkinter.messagebox

screen= tkinter.Tk()
screen.geometry("500x400")
screen.configure(background= "white")
screen.title("Guess The Number")

def get_name():
    message= "Hello "+ entry.get()+" I am thinking of a number from 1-20" 
    tkinter.messagebox.showinfo("Get Number", message)
random_number= random.randint(1, 20)

def guess_number():
    user_number= int(entry1.get())
    if user_number> random_number:
        tkinter.messagebox.showinfo("Too High!", "Too High!")
    if user_number< random_number:
        tkinter.messagebox.showinfo( "Too Low!", "Too Low!")
    if user_number== random_number:
        tkinter.messagebox.showinfo( "Good Job!", "Good Job!")
    

    

label= tkinter.Label(screen, text= "Welcome to our Game!")
label1= tkinter.Label( screen, text= "What's your name?")
label2= tkinter.Label(screen, text= "Take a Guess")
label.place( x=200, y=50)
label1.place( x=50, y=100)
label2.place( x=50, y=200)
entry= tkinter.Entry(screen)
entry1= tkinter.Entry(screen)
entry.place(x=50, y=125)
entry1.place(x=50, y=225)
button= tkinter.Button(screen, text= "OK", command= get_name)
button1= tkinter.Button(screen, text= "Guess", command= guess_number)
button.place(x=250, y=125)
button1.place( x=250, y= 225)



screen.mainloop()
    