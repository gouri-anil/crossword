#GOURI ANIL
#H00MACL2022000069
#PYTHON FOR NLP
#SECOND SEMESTER


import tkinter as tk
from tkinter import messagebox
from functools import partial
import time

entries = [] #initialising variable since it will be declared as global later

#function to change numbers into superscript. this will be the clue numbers in the crossword grid
def to_superscript(text): 
    superscript_map = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
    }
    return ''.join(superscript_map.get(char, char) for char in text)


#function to bind the validate_input function to the KeyRelease event for each entry
def key_release(entry, puzzle, solvedpuzzle):
    global flash_label
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            entry.bind("<KeyRelease>", lambda event, puzzle=puzzle, solvedpuzzle=solvedpuzzle,: validate_input(event, puzzle, solvedpuzzle))
            

#check whether the entered value is correct
def validate_input(event, puzzle, solvedpuzzle):
    global flash_label
    entry = event.widget
    row = entry.grid_info()["row"]
    column = entry.grid_info()["column"]
    expected_value = solvedpuzzle[row][column]
    entered_value = entry.get()
    if expected_value == entered_value.upper():
        flash_label.configure(text="Correct!", fg="red", font=("Times New Roman", 12, "bold"))
    else:
        flash_label.configure(text="Incorrect!", fg="red", font=("Times New Roman", 12, "bold"))
                    

#window for reset, reveal, and submit buttons
def reset_submit():
    window4=tk.Tk()
    window4.title("RESET & SUBMIT")

    reset_button_label = tk.Label(window4, text='RESET', font = ("Times New Roman", 12), justify="center", highlightthickness=1, relief="solid", cursor="hand2")
    reset_button_label.pack(side=tk.LEFT, padx=10, pady=10)
    reset_button_label.bind("<Button-1>", lambda event: on_reset())
  
    submit_button_label = tk.Label(window4, text='SUBMIT', font = ("Times New Roman", 12), justify="center", highlightthickness=1, relief="solid", cursor="hand2")
    submit_button_label.pack(side=tk.RIGHT, padx=10, pady=10)
    submit_button_label.bind("<Button-1>", lambda event: on_submit(flash_submit))

    flash_submit = tk.Label(window4, text='', fg="red", font=("Arial", 12, "bold")) #flash label for successful submission. this is passed as an argument to the #on_submit function
    flash_submit.pack()


#function to flash message and reset the entire crossword grid on confirmation
def on_reset():
    global entries
    option=messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset the game?")
    if option==True:
        for i in range(len(entries)):
            for j in range(len(entries[i])):
                if entries[i][j]:
                    entries[i][j].delete(0, tk.END)  # Clear the entry
                    entries[i][j].unbind("<KeyRelease>")  # Unbind the event to prevent further validation


#function to flash message on submission
def on_submit(flash_submit):
    if check_grid_filled(entries)==True:
        flash_submit.config(text="You have successfully completed the crossword! Congratulations!")
        flash_submit.after(2000, lambda: flash_submit.config(text=""))
        stop_stopwatch()
    else:
        flash_submit.config(text="The crossword isn't completed yet!")
        flash_submit.after(2000, lambda: flash_submit.config(text=""))


#function to check if the grid is filled for submission
def check_grid_filled(entries):
    for row in entries:
        for entry in row:
            if entry.get().strip() == "":    #if even one cell is empty, then return False   
                return False
    return True     #if all the cells are filled then return True


#function for clues window using tkinter
def clues_window(across_clues_list, down_clues_list):
    window2 = tk.Tk()
    window2.title("Clues")
    
    #create clues window
    across_panel = tk.Frame(window2, width=200, height=300)
    across_panel.pack(side=tk.LEFT, padx=10, pady=10)

    down_panel = tk.Frame(window2, width=200, height=300)
    down_panel.pack(side=tk.RIGHT, padx=10, pady=10)

    across_title = tk.Label(across_panel, text="Across", font=("Times New Roman", 16))
    across_title.pack()

    down_title = tk.Label(down_panel, text="Down", font=("Times New Roman", 16))
    down_title.pack()

    for i in range(len(across_clues_list)):
        if across_clues_list[i]==" ":
            down_clues=tk.Label(down_panel, text=down_clues_list[i], font=("Times New Roman", 12), justify="left", anchor="sw")
            down_clues.pack()
        elif down_clues_list[i]==" ":
            across_clues=tk.Label(across_panel, text=across_clues_list[i], font=("Times New Roman", 12), justify="left", anchor="sw")
            across_clues.pack()
        else:
            across_clues=tk.Label(across_panel, text=across_clues_list[i], font=("Times New Roman", 12), justify="left", anchor="sw")
            across_clues.pack()
            down_clues=tk.Label(down_panel, text=down_clues_list[i], font=("Times New Roman", 12), justify="left", anchor="sw")
            down_clues.pack()
    
    window2.mainloop()
        


#function for main crossword grid. this function deals with production and entry of the cells.
def main_grid(puzzle, solvedpuzzle, across_clues_list, down_clues_list):

    window1 = tk.Tk()
    window1.title("Crossword Puzzle")
    
    labels = []
    global entries
    for i in range(len(solvedpuzzle)):
        row_labels = []
        row_entries = []
        for j in range(len(solvedpuzzle[i])):
            if not solvedpuzzle[i][j] == '':
                if solvedpuzzle[i][j] == '':  #Check if the cell is empty
                    label = tk.Label(window1, text='', font = ("Times New Roman", 12), width=3,highlightthickness=1, justify="center", bg='black', relief="solid")  #Create a blacked out label
                    label.grid(row=i, column=j)
                    row_labels.append(label)
    
                elif puzzle[i][j].isdigit() == True: #check if the cell has a number
                        clueno = puzzle[i][j]+" "+solvedpuzzle[i][j]
                        label = tk.Label(window1, text=to_superscript(clueno), font = ("Times New Roman", 12), width=3, highlightthickness=1, bg="white", justify="left", anchor="sw", relief="sunken") #create a cell with the respective letter and superscript clue number
                        label.grid(row=i, column=j)
                        row_labels.append(label)
                    
                else:
                    entry = tk.Entry(window1, validate="key", text='', font = ("Times New Roman", 12), width=3,highlightthickness=1, justify="center") #accept input from the user in a single cell
                    entry.grid(row=i, column=j)
                    row_entries.append(entry)
                    global flash_label
                    flash_label = tk.Label(window1, text="", fg="red", font=("Arial", 12, "bold"))      #label for "correct/incorrect" messages
                    flash_label.grid(row=len(puzzle), columnspan=len(puzzle[0]))
                    key_release(entry, puzzle, solvedpuzzle)       #calling function to check the binding and subsequently invoke the #validate_input function
                    
                    
        labels.append(row_labels)
        entries.append(row_entries)

    clues_window(across_clues_list, down_clues_list)    #calling clues window function

    window1.mainloop()

    
#function to update the stopwatch each second
def update_stopwatch(sw_label):
    global running
    if running:
        current_time = time.time() - start_time
        minutes, seconds = divmod(int(current_time), 60)
        sw_label.config(text=f"{minutes:02d}:{seconds:02d}")
        sw_label.after(1000, lambda: update_stopwatch(sw_label))  # Update every 1000ms (1 second)


#function to start the stopwatch automatically
def start_stopwatch(sw_label):
    global running, start_time
    running = True
    start_time = time.time()
    update_stopwatch(sw_label)


#function to stop the stopwatch automatically
def stop_stopwatch():
    global running
    running = False

#function to read and display the help file
def readhelp(filepath, text_widget):
    with open(filepath,'r', encoding="utf8") as file:
        content = file.read()
        text_widget.delete("1.0", tk.END)  # Clear the text widget
        text_widget.insert(tk.END, content)




