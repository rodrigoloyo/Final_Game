from constants import *
from game.scripting.action import Action


class DrawCarAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        body = car.get_body()

        if car.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = car.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)