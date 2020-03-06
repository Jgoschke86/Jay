import tkinter as tk
import xlrd, time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

trin = xlrd.open_workbook(r"C:\Users\jgosc\Documents\GitHub\Jay\Work\Training Info.xlsx")
sheet = trin.sheet_by_index(0)
manufacturers = ["Briggs", "Exmark", "Honda", "Kawasaki", "Kohler", "Kubota", "MTD", "Scag", "Stihl", "Toro"]
manufacturers.sort()
num = 1


root = tk.Tk()
root.title("Training Logins")


def execute(evt):
    man_name = man_box.get(man_box.curselection())
    for i in range(sheet.nrows):
        if sheet.cell_value(i,0) == man_name:
            username = sheet.cell_value(i,1)
            password = sheet.cell_value(i,2)
            website = sheet.cell_value(i,3)
        else:
            pass
    print(username, password)
    

# About window in menu
def about_window():
    top = tk.Toplevel()
    top.title("About")
    about_text = tk.Label(top, text = """Created by Justin Goschke
    v1.0""", font = 15)
    about_text.pack()
    back_button = tk.Button(top, text = "Back", command = top.destroy, width = 15, font = 16, bg = "dark gray")
    back_button.pack()
    top.mainloop()


man_box = tk.Listbox(width = 15, border = 2)
for name in manufacturers:
    man_box.insert(num, name)
    num += 1
man_box.bind("<<listboxSelect>>")
man_box.grid(row = 1, column = 0, rowspan = 3)


go_button = tk.Button(text = "Go", font = 16, width = 15, bg = "dark gray")
go_button.grid(row = 1, column = 1)
go_button.bind("<Button-1>", execute)


# Menu Bar details
menu_bar = tk.Menu(root)
file = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "About", command = about_window)
file.add_command(command = root.destroy, label = "Exit")


root.config(menu = menu_bar)
root.mainloop()