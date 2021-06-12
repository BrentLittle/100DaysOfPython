from turtle import Turtle

startingPos = [(0,0),(-20,0),(-40,0),(-80,0),(-100,0)]
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.generateSegments()

    def generateSegments(self):
        for pos in startingPos:
            self.addSeg(pos)
    
    def move(self):
        for i in range(len(self.segments)-1, -1, -1):
            if i==0:
                self.segments[0].forward(MOVEDISTANCE) 
            else:
                self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())

    def addSeg(self, position):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(position)
        self.segments.append(seg)
    
    def grow(self):
        self.addSeg(self.segments[-1].pos())    

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)