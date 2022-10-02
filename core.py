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
        
        self.indexing = -1
    
    def create(self, main):
        #Nothing To Do Here, As Class Is Abstract
        num = 0
    
    def update(self, main):
        #Nothing To Do Here, As Class Is Abstract
        num = 0
        
    def destroy(self, main):
        #Nothing To Do Here, As Class Is Abstract
        num = 0
        
        

def instance_create(main, x, y, obj):
    obj.x = x
    obj.y = y
    
    main.objects.append(obj)
    
    obj.indexing = len(main.objects) - 1

    obj.create(main)
    
    return obj


def instance_destroy(main, obj):
    obj.destroy(main)

    main.objects.pop(obj.indexing)

    for i in range(len(main.objects)):
        main.objects[i].indexing = i

    return main


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
        self.a = False
        self.a_pressed = False
        self.b = False
        self.b_pressed = False
        
        
def tile_at_coord(movement_map, x_pos, y_pos):
    r = math.floor(y_pos * 1.0/TILE_SIZE)
    c = math.floor(x_pos * 1.0/TILE_SIZE)
    
    return movement_map[r][c]

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def array_create(length):
    arr = []

    for i in range(length):
        arr.append(-1)

    return arr

def array_length(arr):
    return len(arr)


#Add Event To Queue
'''
	Adds a given event to the queue. See documentation for more on the "Recursive Event Queue-Stack System (REQSS)"
'''
def scr_add_event_to_queue(main, event, eventParameters):
	main.event_queue.append([event, eventParameters, 0, False])

	return main


#Add Event To Stack
'''
	Adds a given event to the stack. See documentation for more on the "Recursive Event Queue-Stack System (REQSS)"
'''

def scr_add_event_to_stack(main, event, eventParameters):
	main.event_stack.insert(0, [event, eventParameters, 0, False])
	
	return main