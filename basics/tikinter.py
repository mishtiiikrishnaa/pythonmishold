import tkinter as tk
import tkinter as ttk
window=tk.Tk()
greeting=tk.Label(text="tutorial")
greeting.pack()
label=tk.Label(
    text="label",
    foreground="#FF3382",
    background="#FFEE33",
    width=20,
    height=10,
)
label.pack()
button=tk.Button(
    text="button",
    width=25,
    height=5,
    foreground="pink",
    background="black",
)
button.pack()
entry=tk.Entry(
    fg="cyan",
    bg="black",
    width=70
)
entry.pack()
window.mainloop()
