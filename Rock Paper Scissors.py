import tkinter, random
screen= tkinter.Tk()
screen.geometry("700x400")
screen.configure(background= "white")
screen.title("Rock Paper Scissors")
options= ["rock", "paper", "scissors"]

def play(user_choice):
   r= random.randint(0,2)
   c= options[r]
   label5.config(text=" What You Chose" + user_choice)
   label6.config(text= "What Computer Chose" + c)
   if user_choice == "rock" and c=="scissors" or user_choice== "paper" and c=="rock" or user_choice== "scissors" and c== "paper":
      score= score+1
      label3.config( text= "Score" +str(score))
      label1.config(text= "Player Win")
   if user_choice== "rock" and c=="paper" or user_choice== "paper" and c== "scissors" or user_choice== "scissors" and c=="rock":
      computer_score= computer_score+1
      label4.config( text= "Score" +str(computer_score))
      label1.config(text= "Computer Won")
   if user_choice== c:
      label1.config(text= "Tie")

label= tkinter.Label(screen, text= "Rock Paper Scissors")
label.place(x=280, y=50)
label1= tkinter.Label(screen, text="Player won!!!")
label1.place(x=300, y= 100)
label2= tkinter.Label(screen, text= "Your Options:")
label2.place(x=50, y= 150)
rock_button= tkinter.Button(screen, text="Rock", command= lambda: play("rock")) 
rock_button.place(x=150, y=200)
paper_button= tkinter.Button(screen, text= "Paper", command= lambda: play("paper"))
paper_button.place(x=250, y=200)
scissors_button= tkinter.Button(screen, text= "Scissors", command= lambda: play("scissors"))
scissors_button.place(x=350, y=200)
label3= tkinter.Label(screen, text= "Score:")
label3.place(x=50, y=300)
label4= tkinter.Label(screen, text= "Computer Score:")
label4.place(x=425, y=300)
label5= tkinter.Label(screen, text= "What You Chose")
label5.place(x= 50, y=350)
label6= tkinter.Label(screen, text= "What Computer Chose")
label6.place(x=425, y=350)
score= 0
computer_score=0

def play(user_choice): 
   global score, computer_score
   r= random.randint(0,2)
   c= options[r]
   label5.config(text=" What You Chose" + user_choice)
   label6.config(text= "What Computer Chose" + c)
   if user_choice == "rock" and c=="scissors" or user_choice== "paper" and c=="rock" or user_choice== "scissors" and c== "paper":
      score= score+1
      label3.config( text= "Score" +str(score))
      label1.config(text= "Player Win")
   if user_choice== "rock" and c=="paper" or user_choice== "paper" and c== "scissors" or user_choice== "scissors" and c=="rock":
      computer_score= computer_score+1
      label4.config( text= "Score" +str(computer_score))
      label1.config(text= "Computer Won")
   if user_choice== c:
      label1.config(text= "Tie")
      
      








screen.mainloop()

