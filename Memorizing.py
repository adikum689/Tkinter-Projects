import tkinter, tkinter.filedialog

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

def save():
    items_saved= listbox.get(0,tkinter.END)
    save_file= tkinter.filedialog.asksaveasfile()
    if save_file!=None:
        for i in items_saved:
            print(i, file=save_file)

def open():
    opened_file= tkinter.filedialog.askopenfile()
    if opened_file!= None:
        items= opened_file.readlines()
        for i in items:
            listbox.insert(tkinter.END, i)

button= tkinter.Button(screen, text="Open", width= 15, command=open)
button1=tkinter.Button(screen, text= "Delete", width=15, command=remove) 
button2= tkinter.Button(screen, text="Save", width=15, command=save)
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