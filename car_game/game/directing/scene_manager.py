import random
from turtle import position
from constants import *
from game.casting.animation import Animation

#car_code
from game.casting.car import Car
from game.casting.fruits import Fruits

from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction

#car_code
from game.scripting.collide_car_action import CollideCarAction
from game.scripting.control_car_action import ControlCarAction
from game.scripting.draw_bg_action import DrawBgAction
from game.scripting.draw_car_action import DrawCarAction
from game.scripting.draw_traffic_action import DrawTrafficAction
from game.scripting.draw_fruits_action import DrawFruitsAction

from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction

#car_code
from game.scripting.move_car_action import MoveCarAction

from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    #COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)

    #car_code
    COLLIDE_CAR_ACTION = CollideCarAction(PHYSICS_SERVICE, AUDIO_SERVICE)

    #car_code
    CONTROL_CAR_ACTION = ControlCarAction(KEYBOARD_SERVICE)
    DRAW_BG_ACTION = DrawBgAction(VIDEO_SERVICE)
    DRAW_FRUITS_ACTION = DrawFruitsAction(VIDEO_SERVICE)
    DRAW_CAR_ACTION = DrawCarAction(VIDEO_SERVICE)
    DRAW_TRAFFIC_ACTION = DrawTrafficAction(VIDEO_SERVICE)

    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    #car_code
    MOVE_CAR_ACTION = MoveCarAction(CAR_GROUP)
    MOVE_TRAFFIC_ACTION = MoveCarAction(TRAFFIC_GROUP)
    
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_background(cast)
        self._add_stats(cast)
        self._add_score(cast)
        self._add_score(cast, True)

        #car_code
        self._add_fruits(cast)
        self._add_car(cast, CAR_GROUP)
        self._add_car(cast, TRAFFIC_GROUP)
        
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        #car_code
        self._add_fruits(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)
        self._add_car(cast, CAR_GROUP)
        self._add_car(cast, TRAFFIC_GROUP)
        

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_CAR_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        stats = cast.get_first_actor(STATS_GROUP)
        print(stats.get_winner())
        self._add_dialog(cast, stats.get_winner())

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    #car_code
    def _add_background(self, cast):
        cast.clear_actors(BG_GROUP)
        position = Point(0, 0)
        size = Point(SCREEN_WIDTH, SCREEN_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Animation(BG_IMAGES, BG_RATE, BG_DELAY)
        bg = Car(body, image)
        cast.add_actor(BG_GROUP, bg)
    
    def _add_car(self, cast, group = CAR_GROUP):
        cast.clear_actors(group)
        if ( group == CAR_GROUP ):
            x = CENTER_X + CAR_WIDTH + 10
            image = Image(CAR_IMAGE)
        elif ( group == TRAFFIC_GROUP):
            x = CENTER_X - CAR_WIDTH - 10
            image = Image(TRAFFIC_IMAGE)
        y = SCREEN_HEIGHT - RACKET_HEIGHT - CAR_HEIGHT  
        position = Point(x, y)
        size = Point(CAR_WIDTH, CAR_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        car = Car(body, image, True)
        cast.add_actor(group, car)

    def _add_fruits(self, cast):
        cast.clear_actors(FRUIT_GROUP)
        for i in range(10):
            x = random.randint(GRASS_WIDTH, (SCREEN_WIDTH - GRASS_WIDTH - FRUIT_WIDTH))
            y = random.randint(0, SCREEN_HEIGHT / 3)
            points = FRUIT_POINTS
            position = Point(x, y)
            size = Point(FRUIT_WIDTH, FRUIT_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FRUIT_IMAGE)
            fruit = Fruits(body, image, points, True)
            cast.add_actor(FRUIT_GROUP, fruit)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast, second = False):
        group = SCORE2_GROUP if second else SCORE_GROUP
        cast.clear_actors(group)
        text = Text(SCORE2_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(SCREEN_WIDTH - HUD_MARGIN - 85, HUD_MARGIN ) if second else Point(HUD_MARGIN + 85, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(group, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_BG_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        
        #car_code
        script.add_action(OUTPUT, self.DRAW_FRUITS_ACTION)
        script.add_action(OUTPUT, self.DRAW_CAR_ACTION)
        script.add_action(OUTPUT, self.DRAW_TRAFFIC_ACTION)
        
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        #script.add_action()
        script.add_action(UPDATE, self.COLLIDE_CAR_ACTION)
        script.add_action(UPDATE, self.MOVE_CAR_ACTION)
        script.add_action(UPDATE, self.MOVE_TRAFFIC_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)