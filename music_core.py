# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:28:02 2022

@author: lucas
"""

from constants import *
from core import *

import pygame

#Song Functions

#Set Song
'''
	Assigns the Current Song.
'''
def scr_set_song(main, song):
	main.previous_song = main.current_song
	main.current_song = song



#Stop Song
'''
	Stops the Current Song from Playing.
'''
def scr_stop_song(main, song):

	if audio_is_playing(main, song[MUSIC_INTRO_SEGMENT]):
		audio_stop_sound()
	elif audio_is_playing(main, song[MUSIC_LOOP_SEGMENT]):
		audio_stop_sound()


#Song Is Playing
'''
	Checks if a Given Song is Playing.
'''
def scr_song_is_playing(main, song):
	
	if audio_is_playing(main, song[MUSIC_INTRO_SEGMENT]) or audio_is_playing(main, song[MUSIC_LOOP_SEGMENT]):
	
		return True	
	
	
	return False



#Same Song
'''
	Checks if Two Songs are the Same
'''
def scr_same_song(song1, song2):

	if song1[MUSIC_INTRO_SEGMENT] == song2[MUSIC_INTRO_SEGMENT] and song1[MUSIC_LOOP_SEGMENT] == song2[MUSIC_LOOP_SEGMENT]:
	
		return True
	
	
	return False


def scr_music_system(main, previous_song, current_song):
	
	#Check If the the Old Song Is Playing But Is Different From the Current One We Should Be Playing
	if scr_song_is_playing(main, previous_song) and not scr_same_song(current_song, previous_song):
		
		#Stop the Previous Song
		scr_stop_song(main, previous_song)
		
		#If the Song Has and Intro Start With It First
		if current_song[MUSIC_INTRO_SEGMENT] != NULL_MUSIC_SEGMENT and not audio_is_playing(main, current_song[MUSIC_INTRO_SEGMENT]):
		
			main = audio_play_sound(main, current_song[MUSIC_INTRO_SEGMENT], False)
		
	#If the Current Loop Is Not Playing and One Exists and The Intro Is Over, Start the Loop
	if (not audio_is_playing(main, current_song[MUSIC_LOOP_SEGMENT]) and current_song[MUSIC_LOOP_SEGMENT] != NULL_MUSIC_SEGMENT) and (current_song[MUSIC_INTRO_SEGMENT] == NULL_MUSIC_SEGMENT or not audio_is_playing(main, current_song[MUSIC_INTRO_SEGMENT])):
	
		main = audio_play_sound(main, current_song[MUSIC_LOOP_SEGMENT], True)

def audio_play_sound(main, snd, loops):
		pygame.mixer.music.load('audio/' + snd + '/' + snd + '.wav')
		
		if loops:
			pygame.mixer.music.play(loops=-1, fade_ms=5)
		else:
			pygame.mixer.music.play(loops=0, fade_ms=5)
			
		main.currently_playing = snd
	

def audio_is_playing(main, snd):
	
	if main.currently_playing == snd:
		return True
	else:
		return False
	
def audio_stop_sound():
	pygame.mixer.music.fadeout(0)


def audio_play_sfx(main ,snd, loops):
	sfx = pygame.mixer.Sound('audio/' + snd + '/' + snd + '.wav')
		
	if loops:
		pygame.mixer.Channel(0).play(sfx, loops=-1, fade_ms=5)
	else:
		pygame.mixer.Channel(0).play(sfx, loops=0, fade_ms=5)