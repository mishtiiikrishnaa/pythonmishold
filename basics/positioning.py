from tkinter import *

root = Tk()

#creating a Label widget
myLabel1 = Label(root, text= "hello world")
myLabel2 = Label(root, text= "i'm maya")
#shoving it on to the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)

root.mainloop( )
