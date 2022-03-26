from constants import *
from game.scripting.action import Action


class DrawCarAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):

        cicle = cast.get_actors(CAR_GROUP)
        # car = cast.get_first_actor(CAR_GROUP)
        # body = car.get_body()

        # if car.is_debug():
        #     rectangle = body.get_rectangle()
        #     self._video_service.draw_rectangle(rectangle, PURPLE)
            
        # image = car.get_image()
        # position = body.get_position()
        # self._video_service.draw_image(image, position)

        cicle1= cicle[0]
        body = cicle1.get_body()

        if cicle1.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = cicle1.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        traffic = cast.get_actors("traffic")
        cicle2= traffic[0]
        body = cicle2.get_body()

        if cicle2.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = cicle2.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)