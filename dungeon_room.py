# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:56:36 2022

@author: lucas
"""

class DungeonRoom():
    def __init__(self, w, h):
        self.room_width = w
        self.room_height = h
        self.tiles = {}
        self.movement = {}
        
        for r in range(self.room_height):
            self.tiles[r] = {}
            self.movement[r] = {}
            
            for c in range(self.room_width):
                self.tiles[r][c] = 0
                self.movement[r][c] = 0
                
    def set_tile(self, pos_x, pos_y, val, mval):
        self.tiles[pos_y][pos_x] = val
        self.movement[pos_y][pos_x] = mval
        
        
    def set_tiles(self, tile_map, movement_map):
        self.tiles = tile_map
        self.movement = movement_map
        
        