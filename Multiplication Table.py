import tkinter, tkinter.ttk

screen= tkinter.Tk()
screen.geometry("500x600")
screen.config(background= "white")
screen.title("Mathematical Table Generator")
label= tkinter.Label(screen, text= "Mathematical Table")
label.place(x=140, y= 50)
label1= tkinter.Label(screen, text= "Number and Range")
label1.place( x= 30, y= 120)
options= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
combo_box= tkinter.ttk.Combobox(screen, width= 15)
combo_box["values"]= options
combo_box.place(x= 160, y=120)

def multiply():
    n= int(combo_box.get())
    n1= int(numbers.get())
    print(n, n1)
    text= str()
    for i in range(1, n1+1):
        text= text+( str(n)+"x"+str(i)+ "="+ str(n*i)+"\n")
    label2.config(text= text)


    

numbers= tkinter.IntVar()
radiobutton= tkinter.Radiobutton(screen, text= "10", variable= numbers, value= 10 )
radiobutton1= tkinter.Radiobutton(screen, text= "20", variable= numbers, value=20)
radiobutton2= tkinter.Radiobutton(screen, text= "30", variable= numbers, value= 30)
radiobutton.place(x=370, y=120 )
radiobutton1.place(x=370, y= 160)
radiobutton2.place(x=370, y= 200)
button= tkinter.Button(screen, text= "Generate", command= multiply)
button.place(x=150, y = 180 )
label2= tkinter.Label(screen,  )
label2.place(x=150, y= 210 )



screen.mainloop()

