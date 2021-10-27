#!/usr/bin/python3

from tkinter import *

# return a function that will configure the widget
# (function factory -- uses a closure)
def mk_callback(w,color):
    def turnColor():
        w.configure(activebackground=color)
        w.configure(background=color)
    return turnColor

top = Tk()

for color in ('red','green','blue','yellow','purple','pink','papayawhip'):
    b = Button(top,text="Push Me ({0})".format(color))
    b.configure(command=mk_callback(b,color))
    b.pack()

bye = Button(top,text="Exit", command=top.destroy)
bye.pack()

top.mainloop()  
