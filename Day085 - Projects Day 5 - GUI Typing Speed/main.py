# IMPORTS #
from tkinter import *
from random import randint,choice
from time import time

# --------------------------------------------------- CONSTANTS ------------------------------------------------------------- #

sentence_bank = [
                 ("He set out for a short walk, but now all he could see were mangroves and water were for miles. "
                  "They looked up at the sky and saw a million stars. "
                  "Improve your goldfish's physical fitness by getting him a bicycle. "
                  "I want a giraffe, but I'm a turtle eating waffles."),
                 ("He was the type of guy who liked Christmas lights on his house in the middle of July. "
                  "He embraced his new life as an eggplant. "
                  "It was the best sandcastle he had ever seen. "
                  "They improved dramatically once the lead singer left."),
                 ("She let the balloon float up into the air with her hopes and dreams. "
                  "The urgent care center was flooded with patients after the news of a new deadly virus was made public. "
                  "Orchards seemed like a frivolous crop when so many people needed food. "
                  "She folded her handkerchief neatly.")
                ]


# ------------------------------------------------- HELPER VARIABLES --------------------------------------------------------- #

used_sentence = sentence_bank[randint(0,2)]
correct = 0
type_speed = 0
start_time = 0
end_time = 0
seconds = end_time-start_time

hasStarted = False


# -------------------------------------------------- FUNCTIONALITY ----------------------------------------------------------- #

def start_game():
    global start_time, hasStarted

    # get the start time of the test and signal that a test is underway
    start_time = time()
    hasStarted = True

def reset():
    global correct, hasStarted, used_sentence
    
    # Reset attributes
    correct = 0
    hasStarted = False
    used_sentence = choice(sentence_bank)
    
    # Reset GUI for next typing test. 
    user_entry.delete(0, 'end')
    text_label.config(text = f'{used_sentence}')
    time_taken.config(text = f"TIME TAKEN:\n0 s")
    correct_word.config(text = f"CPM:\n0")
    num_correct.config(text = f"WORDS CORRECT:\n0")

def results():
    global correct, accuracy, end_time, type_speed, seconds, hasStarted

    # Check if there is a test currently underway
    if hasStarted:
        hasStarted = False
    else: # If not, do not run the results code
        return None
    
    end_time = time()
    
    # Calculate Correct Answer
    user_text = user_entry.get().split(' ')
    text = used_sentence.split(' ')
    for index in range(len(user_text)):
        if user_text[index] == text[index]: 
            correct += 1

    # Calculate Typing Speed
    seconds = round((end_time - start_time),2)
    type_speed = round((correct / (seconds / 60)),2)

    # Update Labels On GUI with appropriate results
    time_taken.config(text = f"TIME TAKEN:\n{seconds} s")
    correct_word.config(text = f"CPM:\n{type_speed}")
    num_correct.config(text = f"WORDS CORRECT:\n{correct}/{len(text)}")


# --------------------------------------------------------- UI ---------------------------------------------------------------- #

# DEFINE AND CONFIGURE WINDOW
window = Tk()
window.geometry('1300x500')
window.title("Typing Speed Test")
window.configure(bg = 'black', padx = 100, pady = 25)


# TITLE AND SENTENCE
title_label = Label(text = 'TYPING SPEED TEST', font = ("Arial", 55, 'bold'), pady = 25, bg = 'black', fg = 'gold')
title_label.grid(row = 0, column = 1)
text_label = Label(text = f"{used_sentence}", font = ("Arial",12, 'bold'), wraplength = 400, padx = 50, pady = 25)
text_label.grid(row = 1, column = 1)


# INFORMATION LABELS
time_taken = Label(text = f'TIME TAKEN:\n0 s', font = ("Arial",12,'bold'), bg = 'black', fg = "white")
time_taken.grid(row = 4, column = 0)
correct_word = Label(text = f'CPM:\n0 ', font = ("Arial",12,'bold'), bg = 'black', fg = "white")
correct_word.grid(row = 4, column = 2)
num_correct = Label(text = f"WORDS CORRECT:\n0", font = ("Arial",12,'bold'), bg = 'black', fg = "white")
num_correct.grid(row = 4, column = 1)


# ENTRY BOX
user_entry = Entry(width = 100)
user_entry.grid(row = 2, column = 1, pady = 25)


# BUTTONS
start_btn = Button(text = 'START',font = ("Arial",12, 'bold'), command = start_game )
start_btn.grid(row = 3, column = 0, pady = 25)
reset_btn = Button(text = 'RESET',font = ("Arial",12, 'bold'), command = reset)
reset_btn.grid(row = 3, column = 1,  pady = 25)
result_btn = Button(text = 'RESULT', font = ("Arial",12, 'bold'), command = results)
result_btn.grid(row = 3, column = 2,  pady = 25)


window.mainloop()