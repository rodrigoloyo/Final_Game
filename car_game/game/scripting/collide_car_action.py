from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideCarAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        traffic = cast.get_first_actor(TRAFFIC_GROUP)
        fruits = cast.get_actors(FRUIT_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        car_body = car.get_body()
        traffic_body = traffic.get_body()

        if self._physics_service.has_collided(car_body, traffic_body):
            sound = Sound(CRASH_SOUND)
            self._audio_service.play_sound(sound)

        for fruit in fruits:
            fruit_body = fruit.get_body()

            if self._physics_service.has_collided(fruit_body, car_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = fruit.get_points()
                stats.add_points(points)
                cast.remove_actor(FRUIT_GROUP, fruit)
            
            if self._physics_service.has_collided(fruit_body, traffic_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = fruit.get_points()
                stats.add_points2(points)
                cast.remove_actor(FRUIT_GROUP, fruit)