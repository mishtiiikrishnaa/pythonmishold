from tkinter import *

root = Tk()

def Play():
    game = Toplevel(root)
    game.title('New Game')
    game.geometry("650x850")

    Label(game, text="Welcome", font=('Curlz MT', 20)).grid(row=0, column=0, columnspan=5, pady=(10, 0))
    Label(game, text="Guess a word!", font=('Curlz MT', 16)).grid(row=1, column=0, columnspan=5, pady=(0, 20))

    for r in range(6):
        for c in range(5):
            entry = Entry(game, width=5, font=('Curlz MT', 20), justify="center",
                          relief="groove")  # Try 'raised', 'sunken', 'groove', or 'ridge'
            entry.grid(row=r+2, column=c, padx=5, pady=5, ipadx=30, ipady=30)

root.title("Wordle Game")

button_play = Button(root, text="Play", command=Play)
button_close = Button(root, text="Close", command=root.destroy)

button_close.pack(pady=10)
button_play.pack()

root.geometry("300x150")
root.mainloop()
