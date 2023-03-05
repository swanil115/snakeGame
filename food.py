from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5)
        self.color("blue")
        self.speed("fastest")
        self.x= random.randint(-280,280)
        self.y= random.randint(-280,280)
        self.goto(self.x,self.y)
        self.refresh()
        
    def refresh(self):
        self.x= random.randint(-280,280)
        self.y= random.randint(-280,280)
        self.goto(self.x,self.y)