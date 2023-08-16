# Introduction
This program aims to present a simple and fun crossword that anyone can attempt in Python. It follows the rules of a basic crossword, along with some options that are easy and straightforward. There are two modes which consist of three randomised puzzles each. An included stopwatch records the time the player takes to finish the crossword as well. There are reset and submit buttons as well.


# Files
a) cw_help.txt – This text file contains the rules and basic introduction to the game. It is displayed in the help section of the main menu.

b) easymode.py – This module contains the solutions and clues of each of the three crosswords in the easy mode. The values are stored in the form of lists. There is also a function to randomise and return the values of each crossword to the main program module. 

c) hardmode.py – This module contains the solutions and clues of each of the three crosswords in the hard mode. The values are stored in the form of lists. There is also a function to randomise and return the values of each crossword to the main program module.

d) cw_func.py – This module contains all the main functions to ensure the smooth working of the game. It contains several functions, including but not limited to: resetting, submitting, a stopwatch clock, and the main grid of the crossword itself. 

e) crossword_mainprog.py – This file is the main program file which must be run in order to play the game. This file contains the code for the main menu, as well as a few functions to redirect the user to each part of the game.


# Limitations

a) The game cannot be run more than once in a single compilation.

b) Upon submission, the program does not actually check if all the cells are correctly filled – it only checks for an entirely filled grid. It is based on the assumption that the user will correct their mistakes as they play, with help from the flashing messages underneath the crossword.

c) There is no option to reveal the solution to a particular crossword.

d) There is no option to move onto another puzzle, in case the randomizer picks a crossword that has been already attempted. The program must be run until a previously unattempted crossword appears.
