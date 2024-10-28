import tkinter, time 

screen= tkinter.Tk()
screen.geometry("200x200")
screen.config(background= "white")
screen.title("Digital Clock")

def show_time():
    clock_time= time.strftime("%I: %M: %S:%p")
    label.config(text= "The Time Is " + clock_time)
    label.after(1000, show_time)
label= tkinter.Label(screen)
label.place( x=100, y=50)
show_time()



screen.mainloop()

