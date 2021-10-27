#!/usr/bin/python3

from tkinter import *
import re

# function called when the user presses the Enter key or clicks on the 
# Search button
def do_search(widget=None):
    count = 0
    matches = 0

    list.delete('0.0','end')   # clear display window
    
    if ignorecase.get():
        opt = "(?i)"
    else:
        opt = "" # is the ignore case button pressed?
                 # any part of RE preceded by (?i)
                 # is matched caseinsensitively

    re_text = RE_TEXT.get()
    if wc.get():
        # entire word must match pattern
        cre = re.compile("^" + opt + re_text + "$")
    else:
        cre = re.compile(opt + re_text)

   # cre is the compiled RE

    WORDS.seek(0,0)     # rewind file

    for word in WORDS:
        if cre.search(word):
            list.insert('end',word)     # put results in list
            matches += 1                     # count number of matches
        count += 1                        # count total number of words
   # update the label that says how many words were found
    results.configure(text="{0} matches out of {1}".format(matches,count))

# Create a main window
top = Tk()

# Add a label for the RE entry blank
re_label = Label(top,text="Enter RE here")
re_label.pack()


# Add the RE entry blank
RE_TEXT = StringVar(top)
re_entry  = Entry(top,textvariable=RE_TEXT)  # needs more work
re_entry.pack(expand=True)

# Add a checkbox to control whether the search is case sensitive
ignorecase = IntVar()
ic = Checkbutton(top,text="Case insensitive",variable=ignorecase)
ic.pack(anchor="w")

# Add a checkbox to control whether the pattern must match the entire word
wc = IntVar()
ww = Checkbutton(top,text="Match entire word",variable=wc)
ww.pack(anchor="w")

# Add a label for the results
results= Label(top,text="")
results.pack()

# Add a scrolled Text widget
# note: scrollbars="e" puts a scrollbar on the right side
#     you can specify or all any of "n","e", "w", or "s"
list = Text(top,height=25,width=20)
list.pack(expand=True)

# create a frame to hold the bottom two buttons
buttonframe = Frame(top)

# add search & exit buttons to the frame
search = Button(buttonframe,text="Search",command=do_search)
exit = Button(buttonframe,text="Exit",command=top.destroy)

# the buttons get packed into buttonframe
search.pack(side="left")
exit.pack(side="left")

# then buttonframe gets backed into the main window
buttonframe.pack()

# the do_search subroutine is bound to the Enter key, so 
# pressing Enter has the same effect as pressing the Search button
re_entry.bind("<Return>",do_search)

# open data file
try:
    WORDS = open("../../DATA/words.txt","r")
except IOError as e:
    print("Unable to open words.txt",e.message)

# note: words.txt will get closed automatically when the app exits

top.mainloop()

