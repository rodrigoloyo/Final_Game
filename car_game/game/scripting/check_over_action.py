from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        fruits = cast.get_actors(FRUIT_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        if len(fruits) == 0:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            winner = WINNER
            if stats.get_score() > stats.get_score2():
                winner += "Player 1"
                stats.add_winner(winner)
            elif stats.get_score2() > stats.get_score():
                winner += "Player 2"
                stats.add_winner(winner)
            elif stats.get_score2() == stats.get_score():
                winner = 'DRAW GAME'
                stats.add_winner(winner)

            callback.on_next(GAME_OVER)