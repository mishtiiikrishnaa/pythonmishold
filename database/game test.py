from tkinter import *
from tkinter.ttk import *
import mysql.connector
import random

root = Tk()


# Connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # your MySQL username
        password="12345678",  # your MySQL password
        database="wordle_game"
    )


# Fetch a random word from the database
def fetch_random_word():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT word FROM words ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    db.close()
    return result[0]


# Function to check the guess and apply color changes
def check_guess(entries, word_to_guess):
    for r, row_entries in enumerate(entries):
        guess = ''.join([entry.get().lower() for entry in row_entries])

        if len(guess) != 5:
            return  # ignore incomplete guesses

        for c, char in enumerate(guess):
            if char == word_to_guess[c]:
                # Green for correct letter in the correct position
                row_entries[c].config(bg="green", fg="white")
            elif char in word_to_guess:
                # Yellow for correct letter in wrong position
                row_entries[c].config(bg="yellow", fg="black")
            else:
                # Gray for incorrect letter
                row_entries[c].config(bg="gray", fg="white")

        # Disable the entire row after a guess is submitted
        for entry in row_entries:
            entry.config(state="disabled")


def Play():
    game = Toplevel(root)
    game.resizable(False, False)
    game.wm_attributes("-topmost", True)
    game.title('New Game')
    game.geometry("485x560")

    word_to_guess = fetch_random_word()
    print(f"Word to guess: {word_to_guess}")  # for testing purposes

    Label(game, text="Welcome").grid(row=7, columnspan=5)
    Label(game, text="Guess a word!").grid(row=8, column=0, columnspan=5)

    entries = []

    for r in range(6):
        row_entries = []
        for c in range(5):
            entry = Entry(game, width=3, justify="center")
            entry.grid(row=r, column=c, padx=4, pady=4, ipadx=24, ipady=24)
            row_entries.append(entry)
        entries.append(row_entries)

    # Add a "Submit Guess" button to check the guess
    submit_button = Button(game, text="Submit Guess", command=lambda: check_guess(entries, word_to_guess))
    submit_button.grid(row=10, columnspan=5)


root.title("Wordle Pirated")

button_play = Button(root, text="Play", command=Play)
button_close = Button(root, text="Close", command=root.destroy)

button_close.pack()
button_play.pack()

root.mainloop()
