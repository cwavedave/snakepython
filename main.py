from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Finish

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="SNAKE...SNAKEEEEEE")
import time

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0

def game_over():
    screen.bgcolor("grey")
    time.sleep(.3)
    screen.bgcolor("black")
    time.sleep(.3)
    screen.bgcolor("grey")
    time.sleep(.3)
    screen.bgcolor("black")

game_on = True

while game_on:
    if snake.head.xcor() > 290:
        game_on = False
        game_over()
        end = Finish()

    if snake.head.xcor() < -290:
        game_on = False
        game_over()
        end = Finish()

    if snake.head.ycor() > 290:
        game_on = False
        game_over()
        end = Finish()

    if snake.head.ycor() < -290:
        game_on = False
        game_over()
        end = Finish()

    for body_segment in snake.body_segment[1:]:
        if snake.head.distance(body_segment) < 10:
            game_on = False
            game_over()
            end = Finish()

    if snake.head.distance(food) < 15:
        print("Num num")
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    snake.create_snake()
    screen.update()
    time.sleep(.1)
    snake.snake_move()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.down,"Down")

screen.exitonclick()