from tkinter import *

root=Tk()

e=Entry(root, width=50, bg='black',fg='white', borderwidth=5)
e.pack()
e.insert(0,"name")

def myClick():
    hello="hello "+e.get()
    myLabel=Label(root, text=hello)
    myLabel.pack()
myButton = Button(root, text="enter your name", padx=50,pady=50,command=myClick,fg='blue',bg='black')
myButton.pack()

root. mainloop()
