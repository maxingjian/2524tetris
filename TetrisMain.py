#!/usr/bin/python2
# ECE 2524 Final Project - Tetris

import GUI
from Tkinter import *
import random


matrix =  [[2,2,2,2,2,2,2,2,2,2],[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0],[2,0,0,1,0,1,0,2,0,0],[2,0,0,1,2,1,0,1,1,1],[1,0,1,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1]]

#matrix2 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
#	      [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0], \
#	      [0,0,0,0,0,0,0,0,0,0],[2,0,0,1,0,1,0,2,0,0],[2,0,0,1,2,1,0,1,1,1],[1,0,1,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,0,0]]


	      
root = Tk()
app = GUI.Application(master = root)
app.mainloop()

#app.after(1000, changeMatrix, matrix2)
root.destroy()