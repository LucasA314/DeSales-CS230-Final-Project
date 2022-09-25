# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:29:06 2022

@author: lucas
"""

import core

class Player(core.Object):
    def __init__(self):
        core.Object.__init__(self, "spr_player", 1, True)
        
        self.hsp = 0;
        self.vsp = 0;
        
        self.walkSpeed = 4;
        
    def update(self, d_map, im):
        core.Object.update(self, d_map, im)
        
        moveLeft = -1 * int(im.left)
        moveRight = int(im.right)
        moveUp = -1 * int(im.up)
        moveDown = int(im.down)
        
        self.hsp = self.walkSpeed * (moveLeft + moveRight)
        self.vsp = self.walkSpeed * (moveUp + moveDown)
        
        
        #Horizontal Collisions
        if (self.hsp > 0):
            if (core.tile_at_coord(d_map.movement, self.x + 16 + self.hsp, self.y) == 1):
                while (core.tile_at_coord(d_map.movement, self.x + 16 + 1, self.y) == 0):
                    self.x += 1
                    
                self.hsp = 0
                
        elif (self.hsp < 0):
            if (core.tile_at_coord(d_map.movement, self.x + self.hsp, self.y) == 1):
                while (core.tile_at_coord(d_map.movement, self.x - 1, self.y) == 0):
                    self.x -= 1
                    
                self.hsp = 0
        
        self.x += self.hsp
        
        
        #Vertical Collisions
        if (self.vsp > 0):
            if (core.tile_at_coord(d_map.movement, self.x, self.y + 16 + self.vsp) == 1):
                while (core.tile_at_coord(d_map.movement, self.x, self.y + 16 + 1) == 0):
                    self.y += 1
                    
                self.vsp = 0
        elif (self.vsp < 0):
            if (core.tile_at_coord(d_map.movement, self.x, self.y + self.vsp) == 1):
                while (core.tile_at_coord(d_map.movement, self.x, self.y - 1) == 0):
                    self.y -= 1
                    
                self.vsp = 0
        
        self.y += self.vsp
        
