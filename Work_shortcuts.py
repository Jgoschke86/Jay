from tkinter import *


root = Tk()

root.title("Website Shortcuts")



def on_selection(evt):
    selected = man_box.curselection()
    details = man_box.get(selected[0])
    if details == "Briggs":
        print("yes")
        Labelvar.set("""Briggs and Stratton
        www.brigssandstratton.com
        Username = blak black
        password = lfdkjngvlkdsfng""")

Labelvar = StringVar()
details = StringVar()

man_box = Listbox(width = 30)
man_box.insert(1, "Briggs")
man_box.insert(2, "Exmark")
man_box.insert(3, "Honda")
man_box.insert(4, "Kawasaki")
man_box.insert(5, "Kohler")
man_box.insert(6, "Scag")
man_box.insert(7, "Schiller")
man_box.insert(8, "Toro")
man_box.bind("<<ListboxSelect>>", on_selection)
man_box.grid(row = 0, column = 0, rowspan = 3)


go_button = Button(root, text = "GO", font = 16, width = 15, bg = "dark gray")
go_button.grid(row = 1, column = 2)


info_box_top = Label(root, text = "Login Information")
info_box = Label(root, textvariable = Labelvar, width = 30, height = 10)
info_box.config(textvariable = Labelvar)
info_box_top.grid(row = 0, column = 4)
info_box.grid(row = 1, column = 4)

    


root.mainloop()