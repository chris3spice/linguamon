"""
The class for our Battle scene is found here.
"""

import pygame as pg

from .. import prepare, tools


class Battle(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.next = "GAME"
        self.bgm = prepare.MUSIC["Anitek_-_07_-_Contact"]
        self.font = pg.font.Font(prepare.FONTS["Fixedsys500c"], 50)
        self.timer = 0.0

    def startup(self, current_time, persistant):
        # Initialize state attributes
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)
        return tools._State.startup(self, current_time, persistant)

    def cleanup(self):
        """Stop the music when scene is done."""
        pg.mixer.music.stop()
        return tools._State.cleanup(self)

    def get_event(self, event):
        """Go back to game on escape key."""
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True

    def draw(self, surface):
        """Blit all elements to surface."""
        image = prepare.GFX['battle_1']
        surface.blit(image, (0,0))


    def update(self, surface, keys, current_time, time_delta):
        """Update blink timer and draw everything."""
        self.current_time = current_time
        self.draw(surface)

    # Determine what phase the battle is on and set the next one
    def determine_phase(self):
        pass

    # Change from one phase to another
    def trans_phase(self):
        pass

    # Perform action chosen by player (run/fight/capture)
    def perf_action(self):
        pass

    # Check match status to see if it should continue or not (user spirit/linguamon capture/destroyed)
    def check_match_status(self):
        pass

    # Check if the user got the answer right
    def check_answer(self):
        pass

    # calculate the gold you get for winning
    def get_new_gold(self):
        gold = 10
        # TODO: Add in calculation so it's not just a fixed rate
        return gold

    # Create sprite for the player's character
    def make_player(self):
        pass

    # Create sprite for enemy character
    def make_enemy(self):
        pass
