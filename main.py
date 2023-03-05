from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Scbd

# from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard= Scbd()
snake = Snake()
food= Food()
# scoreboard= Scbd()
game_is_on=True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on: 
    screen.update ()
    time.sleep(.1)
    snake.move()
    
    if snake.head.distance(food) <20:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.gameover()
        game_is_on= False
    
    for segment in snake.nsl:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on =False
            scoreboard.gameover()
    # else:
    #     continue


screen.exitonclick()

    
