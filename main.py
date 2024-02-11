import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
