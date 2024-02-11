from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(i * -20, 0)
            self.segments.append(turtle)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)