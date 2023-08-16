#GOURI ANIL
#H00MACL2022000069
#PYTHON FOR NLP
#SECOND SEMESTER


import tkinter as tk
import easymode
import hardmode
import cw_func as cw


def easy_label_click(event): #function that runs when EASY MODE is clicked
    result = easymode.randomize()
    puzzle, solvedpuzzle, across_clues_list, down_clues_list = result
    program(puzzle, solvedpuzzle, across_clues_list, down_clues_list)
    
def hard_label_click(event):    #function that runs when HARD MODE is clicked
    result = hardmode.randomize()
    puzzle, solvedpuzzle, across_clues_list, down_clues_list = result
    program(puzzle, solvedpuzzle, across_clues_list, down_clues_list)

def help_label_click(event):    #function that runs when HELP is clicked

    help_window=tk.Tk()
    help_window.title("HELP PAGE")

    text_widget = tk.Text(help_window, wrap=tk.WORD, font=("Times New Roman", 12))
    text_widget.pack(padx=20, pady=20)

    filepath = "C:\\Users\\user\\Desktop\\python\\cw_help.txt.txt"
    
    cw.readhelp(filepath, text_widget)

def exiting_label_click(event): #function that runs when EXIT is clicked
    quit()


def program(puzzle, solvedpuzzle, across_clues_list, down_clues_list):

    #code for stopwatch window
    sw_window=tk.Tk()
    sw_window.title("STOPWATCH")
    sw_label = tk.Label(sw_window, text="00:00", font=("Arial", 20))
    sw_label.pack(pady=20)
    cw.start_stopwatch(sw_label) #invoking the stopwatch start code from #crossword_func function

    #invoking the reset-submit buttons
    cw.reset_submit()
    
    #invoking the main crossword grid
    cw.main_grid(puzzle,solvedpuzzle, across_clues_list, down_clues_list)


#crossword_mainprog main function
    
#window for the menu
window3 = tk.Tk()
window3.title("MAIN MENU")

#title panel and label
title_panel = tk.Frame(window3, width=400, height=100)
title_panel.pack(side=tk.TOP, padx=10, pady=10)

title_label = tk.Label(title_panel, text='LET\'S DO A CROSSWORD! ', font = ("Times New Roman", 20), justify="center", relief="solid")
title_label.pack()

#menu panel and subsequent labels below
menu_panel = tk.Frame(window3)
menu_panel.pack(padx=20, pady=20)

easy_label = tk.Label(menu_panel, text='1. EASY MODE\t', font = ("Times New Roman", 16), justify="left", highlightthickness=1, relief="solid", cursor="hand2")
easy_label.pack(pady=10)
easy_label.bind("<Button-1>", easy_label_click)

hard_label = tk.Label(menu_panel, text='2. HARD MODE\t', font = ("Times New Roman", 16), justify="left", highlightthickness=1, relief="solid", cursor="hand2")
hard_label.pack(pady=10)
hard_label.bind("<Button-1>", hard_label_click)

help_label = tk.Label(menu_panel, text='3. HELP\t', font = ("Times New Roman", 16), justify="left", highlightthickness=1, relief="solid", cursor="hand2")
help_label.pack(pady=10)
help_label.bind("<Button-1>", help_label_click)

exiting_label = tk.Label(menu_panel, text='4. EXIT\t', font = ("Times New Roman", 16), justify="left", highlightthickness=1, relief="solid", cursor="hand2")
exiting_label.pack(pady=10)
exiting_label.bind("<Button-1>", exiting_label_click)


window3.mainloop()


