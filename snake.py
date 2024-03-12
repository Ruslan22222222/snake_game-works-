from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
w = 90
s = 270
a = 180
d = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
          self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup ()
        new_segment.goto(position)
        self.segments.append(new_segment)

        
    
    def extend(sel f):
        self.add_segment(self.segments[-1].position())




    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != s:
            self.head.setheading(w)
        
    def down(self):
        if self.head.heading() != w:
            self.head.setheading(s)
    
    def left(self):
        if self.head.heading() != d:
            self.head.setheading(a)
    
    def right(self):
         if self.head.heading() != a:
            self.head.setheading(d)
    
