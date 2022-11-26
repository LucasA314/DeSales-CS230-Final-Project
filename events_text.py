from constants import *
from core import *
    
    
#Event: Print Text
def escr_print_text(main, eventData):

    #Parameters
    messageToPrint = eventData[EVENT_PARAMETERS][0]

    #Event Actions
    if eventData[EVENT_CONTINUE_SCRIPT] == 0:
        main.sub_state = GAME_STATES.DIALOGUE.value
        main.textbox.formatted_message = messageToPrint
        
        eventData[EVENT_CONTINUE_SCRIPT] = 1
    
    elif eventData[EVENT_CONTINUE_SCRIPT] == 1:
        if (main.textbox.text_done):
            eventData[EVENT_CONTINUE_SCRIPT] = -1
    
    else:
        main.sub_state = GAME_STATES.NULL_STATE.value
        eventData[EVENT_DONE] = True
    

    return eventData