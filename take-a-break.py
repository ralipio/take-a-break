#!/usr/bin/env python

import time # A library to interact with the system time
import webbrowser # A library to manipulate the current browser
import easygui # A library that implements graphical user interface

total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while (break_count <= 2):
    time.sleep(3)
    easygui.msgbox("Time to take a break!")
    #print ("Time to take a break!")
    #webbrowser.open("https://www.youtube.com/watch?v=_U5IhEAFGwQ")
    break_count = break_count + 1
