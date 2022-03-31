from constants import *
from game.scripting.action import Action


class DrawBgAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bg = cast.get_first_actor(BG_GROUP)
        body = bg.get_body()

        if bg.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = bg.get_image()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)