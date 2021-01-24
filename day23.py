from turtle import Turtle, Screen
from random import randint, choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.level = 1
        self.fleet = []
        self.create_fleet()
        self.lanes = range(240, -240, -40)
        
    def create_fleet(self):
        for _ in range(20):
            self.add_car()
        
    def add_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len=2)
        car.color(choice(COLORS))
        car.goto(200, choice(self.lanes))
        self.fleet.append(car)
        
    def level_up(self):
        self.level += 1

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level = 1
        
    def advance(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.goto(STARTING_POSITION)
        scoreboard.level_up()
        car_manager.level_up()
        
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.level = 1
        self.update_screen()
        
    def level_up(self):
        self.level += 1
        self.update_screen()
        
    def update_screen(self):
        self.clear()
        self.write(f"Level {self.level}", False, "center", FONT)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player1.advance, "Up")
screen.listen()


def run():
    
    screen.update()
    screen.ontimer(run, 100)

run()
screen.mainloop()
