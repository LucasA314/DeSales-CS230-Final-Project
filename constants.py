from enum import Enum
from enum import auto


#Screen Constants
'''

'''
FRAME_RATE = 30

TILE_SIZE = 16
BASE_WIDTH = 640
BASE_HEIGHT = 360

# Font Constants
'''
	All constants required for the custom font and text display system.
'''

#Font Index Constants
UPPER = 0
LOWER = 1

#Text Centering Constants
CENTER_LEFT	= 1
CENTER_RIGHT  = -1

#Text Spacing Constants
LETTER_SPACING = 8

#Letter Constants
class LETTER_CONSTANTS(Enum):

	A		  = auto()  #a A
	B		  = auto()  #b B
	C		  = auto()  #c C
	D		  = auto()  #d D
	E		  = auto()  #e E
	F		  = auto()  #f F
	G		  = auto()  #g G
	H		  = auto()  #h H
	I		  = auto()  #i I
	J		  = auto()  #j J
	K		  = auto()  #k K
	L		  = auto()  #l L
	M		  = auto()  #m M
	N		  = auto()  #n N
	O		  = auto()  #o O
	P		  = auto()  #p P
	Q		  = auto()  #q Q
	R		  = auto()  #r R
	S		  = auto()  #s S
	T		  = auto()  #t T
	U		  = auto()  #u U
	V		  = auto()  #v V
	W		  = auto()  #w W
	X		  = auto()  #x X
	Y		  = auto()  #y Y
	Z		  = auto()  #z Z
	ZERO		= auto()  #0
	ONE		= auto()  #1
	TWO		= auto()  #2
	THREE	  = auto()  #3
	FOUR		= auto()  #4
	FIVE		= auto()  #5
	SIX		= auto()  #6
	SEVEN	  = auto()  #7
	EIGHT	  = auto()  #8
	NINE		= auto()  #9
	PK		 = auto()  #<PK_>
	MN		 = auto()  #<MN_>
	DASH		= auto()  #-
	QUESTION	= auto()  #?
	EXCLAMATION = auto()  #!
	MALE		= auto()  #<M__>
	FEMALE	 = auto()  #<F__>
	TIMES	  = auto()  #<TIM>
	PAR_L	  = auto()  #(
	PAR_R	  = auto()  #)
	COLON	  = auto()  #:
	SEMICOLON   = auto()  #
	BRAC_L	 = auto()  #[
	BRAC_R	 = auto()  #]
	BACKSLASH   = auto()  # /
	DOT		= auto()  #.
	COMMA	  = auto()  #
	APOSTROPHE  = auto()  #'
	SPACE	  = auto()  # 
	UNDERSCORE  = auto()  #_
	NEW_LINE	= auto()  #<\n_>


#Game States
class GAME_STATES(Enum):
	
	NULL_STATE = auto()
	INTRO_MOVIE = auto()
	TITLE_SCREEN = auto()
	OPENING_SEQUENCE = auto()
	OVERWORLD = auto()
	BATTLE = auto()
	
	#Sub States
	DIALOGUE = auto()
	NAME_ENTRY = auto()


#Event Constants
'''
	All indeces pertaining to events. See documentation for more on the "Recursive Event Queue-Stack System (REQSS)"
'''

#Event Index Constants
EVENT_INDEX		      = 0
EVENT_PARAMETERS	  = 1
EVENT_CONTINUE_SCRIPT = 2
EVENT_DONE			  = 3

#Events List - This is the Standard Events List
class EVENTS_LIST(Enum):

	null_event = auto()

	#Text Events
	printText = auto()


#Text Display Speeds
TEXT_SLOW =4
TEXT_MEDIUM =2
TEXT_FAST =1


#Music System Constants
'''
	Constants used for Indexing Music Tracks. This is because music tracks can have an intro segment,
	looping segment, or both. A null is used to denote a missing segment.
'''

#Music Index Constants
NULL_MUSIC_SEGMENT  = -1
MUSIC_INTRO_SEGMENT  = 0
MUSIC_LOOP_SEGMENT   = 1

#Null Song
SNG_NULL = ['snd_null' , 'snd_null']
SNG_TITLE = [NULL_MUSIC_SEGMENT, 'snd_menu']
SNG_DUNGEON = [NULL_MUSIC_SEGMENT, 'snd_dungeon']
SNG_GAME_OVER = [NULL_MUSIC_SEGMENT , 'snd_game_over']