#!/usr/bin/env python

#
#  Created by scoutchorton
#  Please don't take credit for code, but feel free to use it or modify as long as credit is given to me
#  Thanks!
#  Happy coding!
#

import curses #Import the curses module
import random
import time

screen = curses.initscr() #Start an instance of curses
curses.start_color() #Initiates colors for curses

curses.noecho() #Disables echoing key input. This allows us to make a custom display
curses.cbreak() #Makes keyboard input instant
screen.keypad(1) #Processes keys like arrow keys in a special way. Thanks terminal.
curses.curs_set(1) #Sets the cursor to be an underline
screen.nodelay(True) #Forces curses to not wait until user input https://stackoverflow.com/questions/28816837/python-curses-dynamic-value-user-input

curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED) #Sets a color pair to be used by curses

def winFunc(s):
	height, width = s.getmaxyx() #Gets the width and height of the terminal https://stackoverflow.com/questions/53019526/get-updated-screen-size-in-python-curses

	window = curses.newwin(height, width) #Creates a new curses window

	message = ""
	messagePrefix = "> "
	curLocation = 0
	curFrame = 1 
	while True: #Main loop for curses stuff
		textFile = open('chatLog.txt', 'r')
		text = textFile.read() #Reads the file with messages
		textFile.close()

		screen.addstr(0, 0, ' '*width*2, curses.color_pair(1)) #Adds top border
		screen.addstr(height-2, 0, ' '*((width*2)-1), curses.color_pair(1)) #Adds bottom border minus bottom right corner (because that's where the cursor is supposed to go)

		c = screen.getch()
		if c == ord(':') and len(message) == 0:
			messagePrefix = ": "
		elif c == curses.KEY_BACKSPACE and len(message) > 0 and curLocation > 0:
			message = message[:curLocation - 1] + message[curLocation:]
			curLocation -= 1
			if len(message) == 0 and messagePrefix == ": ":
				messagePrefix = "> "
		elif c == curses.KEY_LEFT and curLocation > 0:
			curLocation -= 1
		elif c == curses.KEY_RIGHT and curLocation < len(message):
			curLocation += 1
		elif c == curses.KEY_ENTER or c == 10 or c == 13:
			if messagePrefix == "> ":
				textFile = open('chatLog.txt', 'a')
				textFile.write("\n" + message)
				textFile.close()
				message = ""
				curLocation = 0
		elif c == curses.KEY_HOME:
			curLocation = 0
		elif c == curses.KEY_END:
			curLocation = len(message)
		else:
			try:
				message = message[:curLocation] + chr(c) + message[curLocation + 1:]
				curLocation += 1
			except:
				pass

		for y in range(2, height-2): #For every line in between the borders
			screen.addstr(y, 0, '  ', curses.color_pair(1)) #Adds left border
			screen.addstr(y, width-2, '  ', curses.color_pair(1)) #Adds right border

		if len(text.split('\n')) >= height - 5:
			pass
		else:
			for y in range(0, len(text.split('\n'))):
				if len(text.split('\n')[y]) > width - 4:
					screen.addstr(2 + y, 2, text.split('\n')[y][:y])
				else:
					screen.addstr(2 + y, 2, text.split('\n')[y])
		screen.addstr(height - 3, 2, " "*(width - 4))
		screen.addstr(height - 3, 2, messagePrefix + message)
		if curLocation < width - 4 and curLocation == len(message):
			screen.addstr(height - 3, 4 + curLocation, " ", curses.A_UNDERLINE)
		elif curLocation < len(message) and curLocation >= 0:
			screen.addstr(height - 3, 4 + curLocation, message[curLocation], curses.A_UNDERLINE)
		#screen.addstr(height - 4, 2, str(curLocation))

		curses.doupdate()

	curses.nocbreak(); screen.keypad(0); curses.echo() #Reverts screen settings
	curses.endwin() #Returning to your regularly scheduled terminal.

curses.wrapper(winFunc) #Will help if the program deicdes to blow up and take care of the nuclear waste :)
