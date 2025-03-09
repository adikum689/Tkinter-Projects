import tkinter
screen=tkinter.Tk()
screen.geometry("800x600")
screen.title("Ping Pong")

canvas= tkinter.Canvas(screen, width= 800, height=600)
canvas.grid(row=1, column=1)
canvas.create_line(400,0, 400,600, fill="white", width= 4)
canvas.create_oval(370, 330,430, 270, outline="white", width=4)

class Ball():
    def __init__(self, player1, player2):
        self.ball1= canvas.create_oval(200, 230, 170, 260, outline="blue", width=4)
        self.changex= +10
        self.changey= +10
        self.point1= 0
        self.point2= 0
        self.player1= player1
        self.player2= player2
    def draw(self):
        canvas.move(self.ball1, self.changex, self.changey)
        self.coordinates= canvas.coords(self.ball1)
        if self.coordinates[0]<0:
            self.changex= +10
        if self.coordinates[2]>800:
            self.changex= -10
        if self.coordinates[1]<0:
            self.changey= +10
        if self.coordinates[3]>600:
            self.changey= -10
    def collision(self):
        self.coordinates1= canvas.coords(self.player1.pad1)
        self.coordinates2= canvas.coords(self.player2.pad2)
        if self.coordinates1[1]<self.coordinates[3]and self.coordinates1[3]> self.coordinates[1]:
            if self.coordinates1[2]> self.coordinates[0] and self.coordinates1[0]< self.coordinates[0]:
                self.changex= +10 

        if self.coordinates2[1]<self.coordinates[3] and self.coordinates2[3]>self.coordinates[1]:
            if self.coordinates2[0]>self.coordinates[2] and self.coordinates2[2]>self.coordinates[2]:
                self.changex= -10


class Player1():
    def __init__(self):
        self.pad1= canvas.create_rectangle(50, 500, 70, 700, fill= "blue")

class Player2():
    def __init__(self):
        self.pad2= canvas.create_rectangle(50, 500, 70, 700, fill= "blue")

player1= Player1()
player2= Player2()
ball1= Ball(player1, player2)

while True:
    ball1.draw()
    ball1.collision()
    screen.update_idletasks()
    screen.update()

screen.mainloop()