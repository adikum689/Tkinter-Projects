import tkinter

screen=tkinter.Tk()
screen.geometry("600x600")
screen.config(background="white")
screen.title("Memorizer")

def add():
    saved_value= entry.get()
    listbox.insert(tkinter.END, saved_value)
    entry.delete(0, tkinter.END)

def remove():
    selected_items= listbox.curselection()
    for i in reversed(selected_items):
        listbox.delete(i)

button= tkinter.Button(screen, text="Open", width= 15)
button1=tkinter.Button(screen, text= "Delete", width=15, command=remove) 
button2= tkinter.Button(screen, text="Save", width=15)
button3= tkinter.Button(screen, text="Add", width=15, command= add)
button.grid(row=1, column=1, padx= 10, pady=10)
button1.grid(row=1, column=2, padx=10, pady=10)
button2.grid(row=1, column=3, padx= 10,pady=10)
button3.grid(row=2, column=3)
entry= tkinter.Entry(screen, width= 30)
entry.grid(row=2, column=1, columnspan=2, pady=10)
listbox= tkinter.Listbox(screen, width= 60, height=40, selectmode= tkinter.MULTIPLE)
listbox.grid(row=3, column=1, columnspan=3)



screen.mainloop()