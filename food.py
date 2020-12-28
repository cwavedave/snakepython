from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(self.randomx(),self.randomy())

    def randomx(self):
        randomx = 2
        n = 0
        while randomx % 10 != 0:
            randomx = random.randint(-270, 270)
        return randomx

    def randomy(self):
        randomy = 2
        n = 0
        while randomy % 10 != 0:
            randomy = random.randint(-270, 260)
        return randomy