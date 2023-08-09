from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall.
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset()

screen.exitonclick()