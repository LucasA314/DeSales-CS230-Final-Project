import core

class obj_Gold(core.Object):
    def __init__(self, amount):
        core.Object.__init__(self, "spr_gold", 1, True)

        self.amount = amount

    def update(self, main):
        if (main.main_player == -1):
            core.instance_destroy(main, self)

        #Collect
        if (core.scr_collision(self, main.main_player)):
            main.main_player.gold += self.amount

            main.main_player.hud.update_ui(main)

            core.instance_destroy(main, self)