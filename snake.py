from turtle import Turtle

starting_positions = [(0, 0),(-15, 0), (-30, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body_segment = []
        self.create_snake()
        self.total = 0
        self.head = self.body_segment[0]

    def create_snake(self):
        if len(self.body_segment) < 3:
            for position in starting_positions:
                self.add_body(position)


    def add_body(self,position):
        new_body = Turtle(shape="square")
        new_body.penup()
        new_body.fillcolor("white")
        new_body.goto(position)
        new_body.speed("fastest")
        self.body_segment.append(new_body)

    def extend_snake(self):
        self.add_body(self.body_segment[-1].position())

    def snake_move(self):
        for body in range(len(self.body_segment) - 1, 0, -1):
            new_x = self.body_segment[body - 1].xcor()
            new_y = self.body_segment[body - 1].ycor()
            self.body_segment[body].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)