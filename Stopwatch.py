import tkinter, time
screen=tkinter.Tk()
screen.geometry("600x400")
screen.title("Stopwatch")
screen.configure(background="white")
hours= tkinter.IntVar()
minutes= tkinter.IntVar()
seconds= tkinter.IntVar()
hours.set("00")
minutes.set("00")
seconds.set("00")


def start_timer(): 
    h= int(entry.get())
    m= int(entry1.get())
    s= int(entry2.get())
    ts= 3600*h+60*m+s
    while ts>0:
        ts-=1
        print(ts)
        hours.set(ts//3600)
        minutes.set(ts%3600//60)
        seconds.set(ts%60)
        screen.update()
        time.sleep(1)
        


entry= tkinter.Entry(screen, width=4, textvariable=hours)
entry.place(x=200, y= 100)
entry1= tkinter.Entry(screen, width=4, textvariable= minutes)
entry1.place(x=250, y=100)
entry2=tkinter.Entry(screen, width= 4, textvariable= seconds)
entry2.place(x=300, y=100)
button= tkinter.Button(screen, text="Set Time Countdown", command= start_timer)
button.place(x= 200, y= 250)



screen.mainloop()