from constants import *
from game.scripting.action import Action


class ControlCarAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
    
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        traffic = cast.get_first_actor(TRAFFIC_GROUP)

        if self._keyboard_service.is_key_down(LEFT): 
            car.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            car.swing_right()  
        elif self._keyboard_service.is_key_down(UP): 
            car.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            car.swing_down()  
        else: 
            car.stop_moving()
        
        if self._keyboard_service.is_key_down(T_LEFT): 
            traffic.swing_left()
        elif self._keyboard_service.is_key_down(T_RIGHT): 
            traffic.swing_right()  
        elif self._keyboard_service.is_key_down(T_UP): 
            traffic.swing_up()
        elif self._keyboard_service.is_key_down(T_DOWN): 
            traffic.swing_down()  
        else: 
            traffic.stop_moving()