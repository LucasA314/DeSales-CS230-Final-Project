
from numpy import true_divide
import core

class Skill():
    def __init__(self, main, n, t, c, a):
        self.name = n
        self.type = t

        self.cooldown = 0
        self.max_cooldown = c

        self.activation = 0
        self.max_activation = a

        if (self.name == "recklessness"):
            main.main_player.max_health -= 20
            main.main_player.health = main.main_player.max_health
            main.main_player.damage += 10