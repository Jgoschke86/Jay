from tkinter import *
import xlrd, time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

trin = xlrd.open_workbook(r"S:\OPE\Justin\Training info.xlsx")
sheet = trin.sheet_by_index(0)


root = Tk()
root.title("Training Logins")


def execute(evt):
    for i in range(sheet.nrows):
        if sheet.cell_value(i,0) == "Honda":
            username = sheet.cell_value(i,1)
            password = sheet.cell_value(i,2)
        else:
            pass
    




# About window in menu
def about_window():
    top = Toplevel()
    top.title("About")
    about_text = Label(top, text = """Created by Justin Goschke
    v1.0""", font = 15)
    about_text.pack()
    back_button = Button(top, text = "Back", command = top.destroy, width = 15, font = 16, bg = "dark gray")
    back_button.pack()
    top.mainloop()


man_box = Listbox(width = 15, border = 2)
man_box.insert(1, "Briggs")
man_box.insert(2, "Exmark")
man_box.insert(3, "Honda")
man_box.insert(4, "Kawasaki")
man_box.insert(5, "Kohler")
man_box.insert(6, "Kubota")
man_box.insert(7, "MTD")
man_box.insert(8, "Scag")
man_box.insert(9, "Stihl")
man_box.insert(10, "Toro")
man_box.bind("<<listboxSelect>>")
man_box.grid(row = 1, column = 0, rowspan = 3)


go_button = Button(text = "Go", font = 16, width = 15, bg = "dark gray").grid(row = 1, column = 1)
go_button.bind("<Button-1>", execute)


# Menu Bar details
menu_bar = Menu(root)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "About", command = about_window)
file.add_command(command = root.destroy, label = "Exit")


root.config(menu = menu_bar)
root.mainloop()