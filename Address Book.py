import tkinter
screen=tkinter.Tk()
screen.geometry("600x600")
screen.configure(background="white")
screen.title("Address Book")

open= tkinter.Button(screen, text="Open")
update= tkinter.Button(screen, text="Update/Add")
delete= tkinter.Button(screen, text="Delete")
edit= tkinter.Button(screen, text="Edit")
save= tkinter.Button(screen, text= "Save", width=20)
name= tkinter.Label(screen, text= "name")
address= tkinter.Label(screen, text="address")
mobile= tkinter.Label(screen, text="mobile")
email= tkinter.Label(screen, text="email")
birthday= tkinter.Label(screen, text="birthday")
label= tkinter.Label(screen, text= "My Address Book")
entry1= tkinter.Entry(screen)
entry2= tkinter.Entry(screen)
entry3= tkinter.Entry(screen)
entry4= tkinter.Entry(screen)
entry5= tkinter.Entry(screen)
listbox= tkinter.Listbox(screen, width=35, height= 20)
label.grid(row=1, column=1)
open.grid(row=1, column=2)
listbox.grid(row=2, column=1, rowspan=5)
name.grid(row=2, column=2)
entry1.grid(row=2, column=3)
address.grid(row=3, column=2)
entry2.grid(row=3, column=3)
mobile.grid(row=4, column=2)
entry3.grid(row=4, column=3)
email.grid(row=5, column=2)
entry4.grid(row=5, column=3)
birthday.grid(row=6, column=2)
entry5.grid(row=6, column=3)
edit.grid(row=7, column=1)
delete.grid(row=7, column=2)
update.grid(row=7, column=3)
save.grid(row=8, column=1, columnspan=3, pady=20)

screen.mainloop()

