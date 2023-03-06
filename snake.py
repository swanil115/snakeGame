from turtle import Turtle

sp = [(0, 0),(-20, 0),(-40, 0)]
UP = 90
DOWN= 270
LEFT=180
RIGHT=0


class Snake():
    def __init__(self):
        self.nsl= []
        self.create_snake()
        self.head = self.nsl[0]
    
    def create_snake(self):
        for np in sp:
            self.addns(np)
            
    def addns(self, np):
        ns = Turtle()
        ns.penup()
        ns.goto(np)
        ns.shape("square")
        ns.color("red")
        self.nsl.append(ns) 
    
    def extend(self):
        self.addns(self.nsl[-1].position())            
    
    def move(self):  
        for seg in range(len(self.nsl)-1, 0, -1):
            nx= self.nsl[seg-1].xcor()   #here nx is new x position 
            ny= self.nsl[seg-1].ycor()   #here ny is new y position
            self.nsl[seg].goto(nx,ny)    #here nsl is new segment list
        self.head.forward(20)

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
            
    # def addfood(self):
    #     pass