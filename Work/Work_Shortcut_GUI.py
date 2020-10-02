from tkinter import *
from tkinter import font as tkfont


root = Tk()

root.title("Website Shortcuts")

root.geometry("800x600")


#   About Window
def about_window():
    top = Toplevel()
    top.title("About")
    about_text = Label(top, text = "Created by Justin Goschke\nV1.1", font = 15)
    about_text.pack()
    back_button = Button(top, text = "OK", command = top.destroy, width = 15, font = 16, bg = "dark gray")
    back_button.pack()
    


button_font = tkfont.Font(size = 30)


#   Menu Bar
menu_bar = Menu(root)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "About", command = about_window)
file.add_command(command = root.destroy, label = "Exit")


ex_button = Button(font = button_font, text = "Exmark", bg = "red", fg = "white", width = 10)
ex_button.grid(column = 0, row = 0, columnspan = 2, rowspan = 2)
tor_button = Button(font = button_font, text = "Toro", bg = "red", fg = "white", width = 10)
tor_button.grid(column = 0, row = 2, columnspan = 2, rowspan = 2)
hon_button = Button(font = button_font, text = "Honda", bg = "red", fg = "white", width = 10)
hon_button.grid(column = 2, row = 0, columnspan = 2, rowspan = 2)
red_button = Button(font = button_font, text = "Redmax", bg = "red", fg = "white", width = 10)
red_button.grid(column = 0, row = 4, columnspan = 2, rowspan = 2)
cub_button = Button(font = button_font, text = "Cub Cadet", bg = "red", fg = "white", width = 10)
cub_button.grid(column = 4, row = 0, columnspan = 2, rowspan = 2)





root.config(menu = menu_bar)
root.mainloop()