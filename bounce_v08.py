# Import important modules
from tkinter import *
from time import sleep
from random import shuffle

# Build program envirnoment
env = Tk()
env.title("Bounce Game - Rayyan")
env.resizable(0, 0)
env.wm_attributes("-topmost", 1)

# Create and prepare our canvas
canvas = Canvas(env, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()
env.update()

# Create the ball object and its functions using Class
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 393, 20)
        starts = [2, 1, -1, -2]
        shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if self._is_hit(pos) == True:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        
    def _is_hit(self, pos):
        _ppos = self.canvas.coords(self.paddle.id)
        if pos[2] >= _ppos[0] and pos[0] <= _ppos[2]:
            if pos[3] >= _ppos[1] and pos[3] <= _ppos[3]:
                return True
        return False



# Create the paddle object and its functions using Class
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 151, 10, fill=color)
        self.canvas.move(self.id, 350, 500)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.go_left)
        self.canvas.bind_all("<KeyPress-Right>", self.go_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def go_right(self, event):
        self.x = 5

    def go_left(self, event):
        self.x = -5
     
paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

# Build the main loop of our program
while 1:
    ball.draw()
    paddle.draw()
    env.update_idletasks()
    env.update()
    sleep(0.01)
    