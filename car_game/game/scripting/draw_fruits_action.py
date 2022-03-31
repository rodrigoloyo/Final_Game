from constants import *
from game.scripting.action import Action


class DrawFruitsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        fruits = cast.get_actors(FRUIT_GROUP)

        for fruit in fruits:
            body = fruit.get_body()

            if fruit.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = fruit.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
    
    def _create_fruits(self):
        pass

    def _create_granates(self):
        pass