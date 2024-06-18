import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
iteration_count = 0

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    iteration_count += 1

    car_manager.create_car()

    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        car_manager.level_up()
        scoreboard.level += 1
        scoreboard.update_scoreboard()

# 6. Extra: Move left, right, and back without changing heading


screen.exitonclick()
