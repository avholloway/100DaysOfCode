import math
from time import sleep
from random import randint
from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 285)
        self.score = -1
        self.update_score()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center")
        
class GameOverSign(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", False, align="center")

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("coral")
        self.relocate()
        
    def relocate(self):
        while True:
            x, y = randint(-12, 12) * 21, randint(-12, 12) * 21
            dist = math.hypot(self.position()[0] - x, self.position()[1] - y)
            if dist > 21 * 6:
                self.curr_pos = self.position()
                break
        self.goto(x, y)

class Snake:
    def __init__(self):
        """a new snake is born"""
        
        # move directions
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        
        # body segments
        self.SEGWIDTH = 21
        self.segments = []
        
        # create the head
        self.create_head()
        
        # add two additional body segments
        self.add_segment()
        self.add_segment()
        
        return None
    
    def create_head(self):
        self.head = self.base_segment()
        self.segments.append(self.head)
        self.update_color()
    
    def base_segment(self):
        segment = Turtle(shape="square")
        segment.penup()
        return segment
    
    def add_segment(self):
        segment = self.base_segment()
        segment.goto(self.segments[-1].position())
        self.segments.append(segment)
        self.update_color()
    
    def slither(self):
        """the snake slithers on"""
        
        # move all segments, from tail to neck, into the segment's position ahead of it
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        
        # now move the head
        self.head.forward(self.SEGWIDTH)
        
        return self
    
    def update_color(self):
        self.segments[-1].color(
            int((math.sin((.3 * len(self.segments)) + 0) * 127) + 127.5),
            int((math.sin((.3 * len(self.segments)) + 2) * 127) + 127.5),
            int((math.sin((.3 * len(self.segments)) + 4) * 127) + 127.5)
        )
    
    def face_up(self):
        if self.head.heading() not in [self.UP, self.DOWN]:
            self.head.setheading(self.UP)
        return self
    
    def face_down(self):
        if self.head.heading() not in [self.DOWN, self.UP]:
            self.head.setheading(self.DOWN)
        return self
    
    def face_left(self):
        if self.head.heading() not in [self.LEFT, self.RIGHT]:
            self.head.setheading(self.LEFT)
        return self
    
    def face_right(self):
        if self.head.heading() not in [self.RIGHT, self.LEFT]:
            self.head.setheading(self.RIGHT)
        return self
    
    def has_collided_with_wall(self):
        return (self.head.ycor() >= 273
            or self.head.ycor() <= -273
            or self.head.xcor() >= 273
            or self.head.xcor() <= -273)
    
    def has_collided_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 7:
                return True
        return False
        

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

sb = ScoreBoard()
snake = Snake()
food = Food()

screen.onkey(snake.face_up, "Up")
screen.onkey(snake.face_down, "Down")
screen.onkey(snake.face_left, "Left")
screen.onkey(snake.face_right, "Right")
screen.listen()

running = True
while running:
    snake.slither()
    
    if snake.head.distance(food) < 7:
        sb.update_score()
        snake.add_segment()
        food.relocate()
        
    if snake.has_collided_with_wall() or snake.has_collided_with_tail():
        gg = GameOverSign()
        running = False
        
    screen.update()
    sleep(1 / 8)

screen.exitonclick()