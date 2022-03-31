from raylib import GROUP_PADDING
from constants import *
from game.scripting.draw_car_action import DrawCarAction


class DrawTrafficAction(DrawCarAction):

    def execute(self, cast, script, callback):
        car = cast.get_first_actor("traffic")
        body = car.get_body()

        if car.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = car.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)