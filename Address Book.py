import tkinter, tkinter.filedialog
screen=tkinter.Tk()
screen.geometry("600x600")
screen.configure(background="white")
screen.title("Address Book")

contact= {}
def update_list():
    name2= contact.keys()
    listbox.delete(0, tkinter.END)
    for name in name2:
        listbox.insert(tkinter.END, name )

def display_values(event):
    selected_values= listbox.curselection()
    name=listbox.get(selected_values)
    values= contact[name]
    tkinter.messagebox.showinfo(name, "\nName"+name+"\nAddress"+values[0]+"\nMobile"+values[1]+"\nEmail"+values[2]+"\nBirthday"+values[3])



    
def save_values():
    name1= entry1.get()
    address1= entry2.get()
    mobile1= entry3.get()
    email1= entry4.get()
    birthday1= entry5.get()
    contact[name1]= [address1, mobile1, email1, birthday1]
    update_list()
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)
    entry5.delete(0, tkinter.END)

def edit_values():
    selected_values= listbox.curselection()
    name= listbox.get(selected_values)
    entry1.insert(tkinter.END, name)
    record= contact[name]
   
    entry2.insert(tkinter.END, record[0])
    entry3.insert(tkinter.END, record[1])
    entry4.insert(tkinter.END, record[2])
    entry5.insert(tkinter.END, record[3])

def delete_values():
    selected_values= listbox.curselection()
    name=listbox.get(selected_values)
    del contact[name]
    update_list()

def save_contact():
    save_file=tkinter.filedialog.asksaveasfile()
    if save_file!=None:
        print(contact, file=save_file)
        listbox.delete(0,tkinter.END)

def open_contact(): 
    global contact
    opened_value= tkinter.filedialog.askopenfile()
    if opened_value!=None:
        contact= eval(opened_value.readline())
        update_list()
        


      
    
    
    





open= tkinter.Button(screen, text="Open", command= open_contact)
update= tkinter.Button(screen, text="Update/Add", command= save_values)
delete= tkinter.Button(screen, text="Delete", command= delete_values)
edit= tkinter.Button(screen, text="Edit", command= edit_values)
save= tkinter.Button(screen, text= "Save", width=20, command= save_contact)
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
listbox.bind('<<ListboxSelect>>', display_values)
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

