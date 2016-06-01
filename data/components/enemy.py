# Class for the Linguamon
import pygame as pg
import random
from . import lingdict
from .. import prepare, tools

class Linguamon:
    def __init__(self):
        self.name = ""
        self.image = None
        self.shield = None
        self.question = ""
        self.answer = ""
        self.incorrect_answers = []

    def get_enemy(self, area):
        rand_linguamon = []
        for l in lingdict.linguamon_list: # Goes through the list
            for a in l[0]: # Loops through the areas
                if a == area:
                    rand_linguamon.append(l)
        return random.choice(rand_linguamon)