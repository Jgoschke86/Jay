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

manufacturer = ["Exmark", "Honda", "Toro", "Redmax", "Briggs", "Cub Cadet", "Kohler", "Kawasaki", "Scag"]
row_num = 1
column_num = 1
for i in manufacturer:
    if column_num == 4:
        column_num = 1
        row_num += 1
    i = Button(font = button_font, text = i, bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
    i.grid(column = column_num, row = row_num)
    column_num += 1
    


# ex_button = Button(font = button_font, text = "Exmark", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# ex_button.grid(column = 1, row = 1)
# tor_button = Button(font = button_font, text = "Toro", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# tor_button.grid(column = 1, row = 2)
# hon_button = Button(font = button_font, text = "Honda", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# hon_button.grid(column = 2, row = 1)
# red_button = Button(font = button_font, text = "Redmax", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# red_button.grid(column = 1, row = 3)
# cub_button = Button(font = button_font, text = "Cub Cadet", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# cub_button.grid(column = 3, row = 1)
# briggs_button = Button(font = button_font, text = "Briggs", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# briggs_button.grid(column = 2, row = 2)
# kaw_button = Button(font = button_font, text = "Kawasaki", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# kaw_button.grid(column = 3, row = 2)
# kohl_button = Button(font = button_font, text = "Kohler", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# kohl_button.grid(column = 2, row = 3)
# scag_button = Button(font = button_font, text = "Scag", bg = "gray", fg = "black", width = 10, relief = GROOVE, border = 5, activebackground = "dark gray")
# scag_button.grid(column = 3, row = 3)


#  Blank BOxes
left_box = Label(width = 5)
left_box.grid(column = 0, row = 0, rowspan = 5)
right_box = Label(width = 5)
right_box.grid(column = 5, row = 0, rowspan = 5)
top_box = Label(height = 3)
top_box.grid(row = 0, column = 1, columnspan = 3)

root.config(menu = menu_bar)
root.mainloop()