from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 
# GAME
GAME_NAME = "Cars Game"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 900
GRASS_WIDTH = 222
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "car_game/assets/fonts\\zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "car_game/assets/sounds\\boing.wav"
CRASH_SOUND = "car_game/assets/sounds\\crash.wav"
WELCOME_SOUND = "car_game/assets/sounds\\start.wav"
OVER_SOUND = "car_game/assets/sounds\\over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
T_LEFT = "j"
T_RIGHT = "l"
T_UP = "i"
T_DOWN = "k"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "car_game/assets/data\\level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
BG_GROUP = "bg"
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
SCORE2_GROUP = "score2"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "PLAYER 1: {}"
SCORE2_FORMAT = "PLAYER 2: {}"

# CARS
#car_code
CAR_GROUP = "cars"
TRAFFIC_GROUP = "traffic"
TRAFFIC_IMAGE = "car_game/assets/images\\police_car.png"
CAR_IMAGE = "car_game/assets/images\\deportive_car.png"
BG_IMAGE = "car_game/assets/images\\bg_2_0.png"
CAR_WIDTH = 120
CAR_HEIGHT = 254
CAR_VELOCITY = 10

#FRUITS
FRUIT_GROUP = "fruits"
FRUIT_IMAGE = "car_game/assets/images\\fruit.png"
FRUIT_WIDTH = 96
FRUIT_HEIGHT = 71
FRUIT_VELOCITY = 10
FRUIT_POINTS = 30
#car_code
BG_IMAGES = [f"car_game/assets/images\\bg_2_{i:1}.png" for i in range(0,3)]
BG_DELAY = 0.1
BG_RATE = 1

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "car_game/assets/images\\000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"car_game/assets/images\\{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"car_game/assets/images\\{i:03}.png" for i in range(10,19)],
    "g": [f"car_game/assets/images\\{i:03}.png" for i in range(20,29)],
    "p": [f"car_game/assets/images\\{i:03}.png" for i in range(30,39)],
    "y": [f"car_game/assets/images\\{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO IGNITE MOTORS"
PREP_TO_LAUNCH = "PREPARING WHEELS"
WINNER = "THE WINNER IS: "
WAS_GOOD_GAME = "GAME OVER"