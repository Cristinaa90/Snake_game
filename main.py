from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

screen.bgcolor("black")
screen.title("Joc sarpe")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#sus = 90, stanga = 180, jos = 270, dreapta=0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.12)

    snake.move()

    # detecteaza coleziunea cu mancarea
    if snake.head.distance(food) < 13:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # detecteaza coleziunea cu peretii
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detecteaza coleziunea cu propria coada
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()























