#!/usr/bin/python3

from tkinter import *

def update_label():
    lang = langlist.get(langlist.curselection()) 
    lab.configure(text="#!/usr/bin/" + lang)

top = Tk()

lab = Label(top,text="Choose a language")
lab.pack()

langlist = Listbox(top,width=20,height=3)
langlist.insert('end',"Python","Perl","PHP","Ruby","Awk")
langlist.pack()

b_choose = Button(top,text="Choose",command=update_label)
b_choose.pack()

b_quit = Button(top,text="Quit",command=top.destroy)
b_quit.pack()

top.mainloop()



