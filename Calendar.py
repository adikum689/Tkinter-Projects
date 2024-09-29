import tkinter, calendar 
screen=tkinter.Tk()
screen.geometry("600x400") 
screen.configure(background="white")
screen.title("Calendar")

def show_calendar():
    screen1= tkinter.Tk()
    screen1.geometry("600x600")
    year= int(entry.get())
    screen1.configure(background= "grey")
    screen1.title(year)
    text= tkinter.Text(screen1, height= 50)
    text.pack()
    calendartext= calendar.calendar(year)
    text.insert("1.0", calendartext)
    screen1.mainloop()



def exit():
    screen.destroy()
label=tkinter.Label(screen, text= "Calendar", font= ("arial", 50))
label.pack()
label1=tkinter.Label(screen, text="Enter Year", font= ("arial", 30))
label1.pack()
entry=tkinter.Entry(screen)
entry.pack()
button= tkinter.Button(screen, text= "Show Calendar", command= show_calendar)
button.pack()
exit_button= tkinter.Button(screen, text= "Exit", command= exit)
exit_button.pack()
screen.mainloop()
