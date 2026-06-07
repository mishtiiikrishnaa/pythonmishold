from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text="look i clicked a button~",fg='black',bg='blue')
    myLabel.pack()

myButton = Button(root, text="click me!", padx=50,pady=50,command=myClick,fg='blue',bg='black')
myButton.pack()


root.mainloop()


