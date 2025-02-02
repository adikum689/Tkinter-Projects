import tkinter, random, tkinter.messagebox
screen=tkinter.Tk()
screen.geometry("450x350")
screen.title("Tic Tac Toe")
screen.configure(background="white")

def check_winner():
    winning_combinations= [(button1,button4,button7), (button2,button5,button8), (button3,button6,button9), (button1,button2,button3), (button4,button6,button5), (button7,button8,button9), (button1, button5, button9), (button3,button5,button7)]
    for i in winning_combinations:
        if i[0]["text"]== "X" and i[1]["text"]== "X" and i[2]["text"]=="X":
            tkinter.messagebox.showinfo("Tic Tac Toe", "You Win!")
            return True
        if i[0]["text"]== "O" and i[1]["text"]=="O" and i[2]["text"]== "O":
            tkinter.messagebox.showinfo("Tic Tac Toe", "Computer Wins")
            return True
    if len(available_buttons)==0:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Tie")
        return True
    return False






        
def place_x(button_clicked): 
    if button_clicked in available_buttons:
        button_clicked.config(text="X")
        available_buttons.remove(button_clicked)
        x= check_winner()
        if not x:
            place_o()
            x=check_winner()
   

def place_o():
    computer_choice= random.choice(available_buttons)
    computer_choice.config(text="O")
    available_buttons.remove(computer_choice)
    




button1= tkinter.Button(screen, text="", width=12, height=5, command=lambda:place_x(button1))
button2= tkinter.Button(screen, text="", width=12, height= 5, command= lambda:place_x(button2))
button3=tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button3))
button4= tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button4))
button5=tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button5))
button6= tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button6))
button7= tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button7))
button8= tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button8))
button9= tkinter.Button(screen, text="", width=12, height=5, command= lambda:place_x(button9))
label= tkinter.Label(screen, text="Player", width=12)
label1=tkinter.Label(screen, text="Computer", width=12)

label.grid(row=1, column=2)
label1.grid(row=2, column=2)
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
button4.grid(row=4, column=1)
button5.grid(row=4, column=2)
button6.grid(row=4, column=3)
button7.grid(row=5, column=1)
button8.grid(row=5, column=2)
button9.grid(row=5, column=3)

available_buttons= [button1, button2, button3, button4, button5, button6, button7, button8, button9]

screen.mainloop()