from turtle import Turtle, Screen
from random import randint, choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.level = 1
        self.fleet = {}
        self.lanes = range(200, -240, -40)
        for lane in self.lanes:
            self.fleet[lane] = []
        self.create_fleet()
        self.running = True
        
    def tick(self):
        if self.running:
            for lane, cars in self.fleet.items():
                for car in cars:
                    if car.xcor() > -200:
                        car.forward(5 + (self.level * 1.5))
                        if player1.ycor() + 10 > car.ycor() - 10:
                            if player1.xcor() + 10 > car.xcor() - 20:
                                if player1.xcor() - 10 < car.xcor() + 20:
                                    self.running = False
                                    scoreboard.game_over()
                    else:
                        car.setup()
                        car.sety(lane)
                        self.lane_position(car, lane)
                
    def create_fleet(self):
        for lane in self.fleet.keys():
            for _ in range(4):
                car = Car()
                self.assign_lane(car, lane)
                self.lane_position(car, lane)
                
    def assign_lane(self, car, lane):
        car.sety(lane)
        self.fleet[lane].append(car)
        
    def lane_position(self, car, lane):
        if len(self.fleet[lane]) == 0:
            car.setx(randint(280, 380))
        else:
            car.setx(self.last_in_lane(lane).xcor() + randint(150, 850))
            
    def last_in_lane(self, lane):
        last = None
        for car in self.fleet[lane]:
            if not last or car.xcor() > last.xcor():
                last = car
        return last
        
    def level_up(self):
        self.level += 1

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()
        
    def setup(self):
        self.reset()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(choice(COLORS))
        self.setheading(180)
        
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240

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
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player1.advance, "Up")
screen.listen()

def run():
    if car_manager.running:
        car_manager.tick()
        screen.update()
        screen.ontimer(run, 100)

run()
screen.mainloop()
