# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:29:34 2022

@author: lucas
"""
import math

TILE_SIZE = 16

class Object():
    def __init__(self, spr, frms, vis):
        #Initialize
        self.x = 0
        self.y = 0
        self.sprite_index = spr
        self.sprite_frames = frms
        self.visible = vis
        self.image_index = 0
        self.image_speed = 1
        self.image_alpha = 1
    
    def create(self):
        #Nothing To Do Here, As Class Is Abstract
        num = 0
    
    def update(self, d_map, im):
        #Nothing To Do Here, As Class Is Abstract
        num = 0
        
        

def instance_create(x, y, obj):
    obj.x = x
    obj.y = y

    obj.create()
    
    return obj


class InputManager():
    def __init__(self):
        self.up = False
        self.up_pressed = False
        self.down = False
        self.down_pressed = False
        self.left = False
        self.left_pressed = False
        self.right = False
        self.right_pressed = False
        
        
def tile_at_coord(movement_map, x_pos, y_pos):
    r = math.floor(y_pos * 1.0/TILE_SIZE)
    c = math.floor(x_pos * 1.0/TILE_SIZE)
    
    return movement_map[r][c]

def sign(x):
    if x > 0:
        return 1;
    elif x == 0:
        return 0;
    else:
        return -1;