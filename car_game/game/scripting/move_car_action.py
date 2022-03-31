from tokenize import group
from constants import *
from game.casting.point import Point
from game.scripting.action import Action

class MoveCarAction(Action):

    def __init__(self, group):
        self._group = group
        pass

    def execute(self, cast, script, callback):
        car = cast.get_first_actor(self._group)
        body = car.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        position = position.add(velocity)

        if x < GRASS_WIDTH:
            position = Point(GRASS_WIDTH, y)
        elif x > (SCREEN_WIDTH - CAR_WIDTH - GRASS_WIDTH):
            position = Point(SCREEN_WIDTH - CAR_WIDTH - GRASS_WIDTH, y)
        elif y < 0:
            position = Point(x, 0)
        elif y > (SCREEN_HEIGHT - CAR_HEIGHT):
            position = Point(x, (SCREEN_HEIGHT - CAR_HEIGHT))
            
        body.set_position(position)
        