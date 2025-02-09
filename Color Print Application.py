import tkinter
class Drawing():
    def __init__(self):
        self.screen=tkinter.Tk()
        self.screen.geometry("600x600")
        self.screen.title("Color Paint Application")
        self.Pen= tkinter.Button(self.screen, text="Pen")
        self.Color= tkinter.Button(self.screen, text= "Color")
        self.Brush= tkinter.Button(self.screen, text= "Brush")
        self.Eraser= tkinter.Button(self.screen, text="Eraser")
        self.Scale= tkinter.Scale(self.screen, from_= 1, to= 10, orient= "horizontal")
        self.Canvas= tkinter.Canvas(self.screen, background= "white", width=600, height=550)
        self.Pen.grid(row=1, column=1)
        self.Color.grid(row=1, column=2)
        self.Brush.grid(row=1, column=3)
        self.Eraser.grid(row=1, column=4)
        self.Scale.grid(row=1, column=5)
        self.Canvas.grid(row=2, column=1, columnspan= 5)
        self.setup()
        self.screen.mainloop()
    def setup(self):
        self.pencolor= "blue"
        self.thickness= 1
        self.oldx= None
        self.oldy=None
        self.eraseron= False
        self.selectedbutton= self.Pen
        self.Canvas.bind("<B1-Motion>", self.draw)
        self.Canvas.bind("<ButtonRelease-1>", self.reset)

    def draw(self, event):
        if self.oldx and self.oldy: 
            self.Canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill= "blue", width= self.thickness, smooth=True)
        self.oldx= event.x
        self.oldy= event.y
    def reset(self, event): 
        self.oldx= None
        self.oldy= None



Drawing()


