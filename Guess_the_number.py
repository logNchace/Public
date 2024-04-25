import random
import tkinter as tk


def check_guess():
    global num_guesses, n, guesses
    guess = int( entry.get() )
    num_guesses += 1
    guesses.append( guess )

    if guess < n:
        feedback_label.config( text=f"Too low. Your guesses so far: {guesses}" )
    elif guess > n:
        feedback_label.config( text=f"Too high! Your guesses so far: {guesses}" )
    else:
        feedback_label.config( text=f"Congratulations! You guessed the number in {num_guesses} guesses. Your guesses: {guesses}" )
        submit_button.config( state="disabled" )

def reset_game():
    global num_guesses, n, guesses
    num_guesses = 0
    guesses = []
    n = random.randrange( 1, 100 )
    submit_button.config( state="normal" ) # re-enable the submit button
    feedback_label.config( text="" ) # clear the feedback label


n = random.randrange( 1, 100 )
num_guesses = 0
guesses = []

app = tk.Tk()
app.title( "Number Guessing Game" )

# Set window size
app.geometry("500x400")  # Width=500, Height=400

label = tk.Label( app, text="Enter a number between 1 and 100:" )
label.pack()

entry = tk.Entry( app )
entry.pack()

submit_button = tk.Button( app, text="Submit", command=check_guess )
submit_button.pack()

reset_button = tk.Button( app, text="Reset", command=reset_game ) # added reset button
reset_button.pack()

feedback_label = tk.Label( app, text="" )
feedback_label.pack()

app.mainloop()