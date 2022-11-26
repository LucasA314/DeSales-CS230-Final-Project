from constants import *
from core import *

import events_text as te

#Run Events
'''
	Runs the proper event using the correct index from the queue/stack. See documentation for more on the "Recursive Event Queue-Stack System (REQSS)"
	
	PARAMETERS:
		eventData - The information for the current event being run.
	RETURN:
		eventData - The information for the current event being run.
'''
def scr_run_event(main, eventData):
	
	if eventData[EVENT_INDEX] == EVENTS_LIST.null_event.value:
		eventData[EVENT_DONE] = True
	
    #Text Events
	if eventData[EVENT_INDEX] == EVENTS_LIST.printText.value:
		eventData = te.escr_print_text(main, eventData)
	
	
	return eventData