from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_playing = True
while game_playing:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_playing = False
        scoreboard.game_over()

    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_playing = False
            scoreboard.game_over()







screen.exitonclick()











