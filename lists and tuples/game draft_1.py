from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import *

root = Tk()

def Play():
    game = Toplevel(root) 
    game.resizable(False,False) 
    game.wm_attributes("-topmost",True)
    game.title('new game')
    game.geometry("485x560")

    Label(game, text="Welcome").grid(row=7, columnspan=5)
    Label(game, text="guess a word!").grid(row=8, column=0, columnspan=5)

    entries = []
    
    for r in range (6):
        row_entries = []
        for c in range (5):
            entry = Entry(game, width=3, justify = "center")
            entry.grid(row=r,column=c,padx=4,pady=4,ipadx=24,ipady=24)
            row_entries.append(entry)
        entries.append(row_entries)
  
root.title("wordle pirated")

button_play = Button(root, text = "play",command=Play) 
button_close = Button(root, text = "Close", command = root.destroy)

button_close.pack()
button_play.pack()

root.mainloop()
