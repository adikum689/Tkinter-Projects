import tkinter
screen=tkinter.Tk()
screen.geometry("800x200")
screen.title("Weight Converter")
screen.configure(background= "white")
label= tkinter.Label(screen, text= "Enter weight in kg", )
label.grid(row=1, column=1, padx=50, pady= 20)
entry= tkinter.Entry(screen)
entry.grid(row=1, column= 2, padx=50, pady= 20 )
gram= tkinter.Label(screen, text= "Grams")
gram.grid(row=2, column=1, padx=50, pady= 20)
pounds= tkinter.Label(screen, text= "Pounds")
pounds.grid(row=2, column=2, padx=50, pady= 20)
ounce= tkinter.Label(screen, text= "Ounce")
ounce.grid( row=2, column=3, padx=50, pady= 20)
text= tkinter.Text(screen, height=1, width= 15 )
text.grid(row=3, column=1, padx=50, pady= 20)
text1= tkinter.Text(screen, height=1, width= 15 )
text1.grid(row=3, column=2, padx=50, pady= 20)
text2= tkinter.Text(screen, height=1, width= 15 )
text2.grid(row=3, column=3, padx=50, pady= 20)

def show_weight():
    weight= int(entry.get())
    gram_weight= weight*1000
    pound_weight= weight*2.205
    ounce_weight= weight*35.274
    text.insert("1.0", gram_weight)
    text1.insert("1.0", pound_weight)
    text2.insert("1.0", ounce_weight)

button=tkinter.Button(screen, text= "Convert", command= show_weight)
button.grid(row=1, column=3, padx=50, pady= 20)




    
    
screen.mainloop()