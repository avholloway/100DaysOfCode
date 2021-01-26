from turtle import Turtle, Screen
from random import choice, randint

class FroggerGame():
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.player = Player()
        self.level = 1
        self.SAFETY_LINE = 200
        self.STARTING_LINE = -200
        self.SPEED = 5
        self.traffic = {lane:[] for lane in range(-160, 200, 40)}
        self.screen.onkey(lambda: self.player_control("up"), "Up")
        self.screen.onkey(lambda: self.player_control("down"), "Down")
        self.screen.listen()
        self.scoreboard = Scoreboard()
        self.scoreboard.show_level(self.level)
        self.draw_lanes()
        self.populate_traffic()
        self.run()
        self.screen.mainloop()
        
    def run(self):
        if self.running:
            self.manage_traffic()
            self.screen.update()
            self.screen.ontimer(self.run, 100)
            
    def draw_lanes(self):
        lines = [lane + 20 for lane in self.traffic.keys()]
        lines = [-180] + lines
        for line in lines:
            t = Turtle()
            t.penup()
            t.goto(-310, line)
            t.pendown()
            t.setx(310)
            t.penup()
            t.goto(-1000, -1000)
            
    def manage_traffic(self):
        for lane, cars in self.traffic.items():
            for car in cars:
                car.tick(self.SPEED)
                if car.xcor() < -350:
                    car.setx(self.last_car_in_lane(lane).xcor() + randint(60, 1600))
                    continue
                print(f"check {car.position()=} and {self.player.position()=}")
                if self.overlaps(car, self.player):
                    self.running = False
                    self.scoreboard.game_over()
                
    def overlaps(self, obj1, obj2):
        print(f"{obj1.ycor()=}{obj2.ycor()=}")
        print(f"{obj1.left_side=}{obj2.right_side=}")
        print(f"{obj1.right_side=}{obj2.left_side=}")
        if obj1.ycor() == obj2.ycor():
            if obj1.left_side < obj2.right_side:
                if obj1.right_side > obj2.left_side:
                    print("collisions detected")
                    return True
        return False
        
    def last_car_in_lane(self, lane):
        return max(self.traffic[lane], key=lambda x: x.xcor())
            
    def populate_traffic(self):
        for lane in self.traffic.keys():
            for i in range(4):
                car = Car()
                x = randint(60, 1600)
                if i == 0:
                    x += -300
                else:
                    x += self.traffic[lane][-1].xcor()
                car.goto(x, lane)
                self.traffic[lane].append(car)
            
    def player_control(self, direction):
        if direction == "down" and self.player.ycor() > self.STARTING_LINE:
            self.player.retreat_backwards()
        elif direction == "up":
            self.player.crawl_forwards()
        if self.player.ycor() >= self.SAFETY_LINE:
            self.level_up()
            
    def level_up(self):
        self.SPEED += 3
        self.level += 1
        self.scoreboard.show_level(self.level)
        self.player.sety(self.STARTING_LINE)
        
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.UP = 90
        self.STARTING_POSITION = (0, -200)
        self.penup()
        self.shape("turtle")
        self.setheading(self.UP)
        self.goto(self.STARTING_POSITION)
        self.CRAWL_INCREMENT = 40
        self.left_side = self.xcor() - 5
        self.right_side = self.xcor() + 5
        self.top_side = self.ycor() + 5
        self.bottom_side = self.ycor() - 5
    
    def crawl_forwards(self):
        self.forward(self.CRAWL_INCREMENT)
        self.update_collision_box()
    
    def retreat_backwards(self):
        self.backward(self.CRAWL_INCREMENT)
        self.update_collision_box()
        
    def update_collision_box(self):
        self.left_side = self.xcor() - 5
        self.right_side = self.xcor() + 5
        self.top_side = self.ycor() + 5
        self.bottom_side = self.ycor() - 5
        
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=3, stretch_wid=1.5)
        self.shape("square")
        self.color(choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        self.left_side = self.xcor() - 15
        self.right_side = self.xcor() + 15
        self.top_side = self.ycor() + 7
        self.bottom_side = self.ycor() - 7
        
    def tick(self, speed):
        self.drive_forward(speed)
        self.update_collision_box()
        
    def drive_forward(self, speed):
        self.forward(speed)
        
    def update_collision_box(self):
        self.left_side = self.xcor() - 15
        self.right_side = self.xcor() + 15
        self.top_side = self.ycor() + 7
        self.bottom_side = self.ycor() - 7
        
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.FONT = ("Agency FB", 18, "normal")

    def show_level(self, level):
        self.clear()
        self.write(f"Level {level}", False, "center", self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", self.FONT)

game = FroggerGame()

# class CarManager():
#     def __init__(self):
#         self.level = 1
#         self.fleet = {}
#         self.lanes = range(200, -240, -40)
#         for lane in self.lanes:
#             self.fleet[lane] = []
#         self.create_fleet()
#         self.running = True
#
#     def tick(self):
#         if self.running:
#             for lane, cars in self.fleet.items():
#                 for car in cars:
#                     if car.xcor() > -200:
#                         car.forward(5 + (self.level * 1.5))
#                         if player1.ycor() + 10 > car.ycor() - 10:
#                             if player1.xcor() + 10 > car.xcor() - 20:
#                                 if player1.xcor() - 10 < car.xcor() + 20:
#                                     self.running = False
#                                     scoreboard.game_over()
#                     else:
#                         car.setup()
#                         car.sety(lane)
#                         self.lane_position(car, lane)
#
#     def create_fleet(self):
#         for lane in self.fleet.keys():
#             for _ in range(4):
#                 car = Car()
#                 self.assign_lane(car, lane)
#                 self.lane_position(car, lane)
#
#     def assign_lane(self, car, lane):
#         car.sety(lane)
#         self.fleet[lane].append(car)
#
#     def lane_position(self, car, lane):
#         if len(self.fleet[lane]) == 0:
#             car.setx(randint(280, 380))
#         else:
#             car.setx(self.last_in_lane(lane).xcor() + randint(150, 450))
#
#     def last_in_lane(self, lane):
#         last = None
#         for car in self.fleet[lane]:
#             if not last or car.xcor() > last.xcor():
#                 last = car
#         return last
#
#     def level_up(self):
#         self.level += 1