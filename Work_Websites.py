from tkinter import *
import xlrd


def about_window():
    top = Toplevel()
    top.title("About")
    about_text = Label(top, text = """This program was made to assist with accessing certain websites.
    Created by Justin Goschke
    v1.0""", font = 15)
    about_text.pack()
    back_button = Button(top, text = "Back", command = top.destroy, width = 15, font = 16, bg = "dark gray")
    back_button.pack()
    top.mainloop()



root = Tk()

root.title("Website Shortcuts")




menu_bar = Menu(root)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "About", command = about_window)
file.add_command(label = "Exit", command = root.destroy)

username = []
password = []
website = []

top_frame = Frame(root)
top_frame.pack()

top_label = Label(top_frame, text = "Warranty Site Logins", font = 26)
top_label.grid(columnspan = 4)


briggs = Button(top_frame, text = "Briggs", width = 15, font = 16, bg = "dark gray")
exmark = Button(top_frame, text = "Exmark", width = 15, font = 16, bg = "dark gray")
honda = Button(top_frame, text = "Honda", width = 15, font = 16, bg = "dark gray")
kawasaki = Button(top_frame, text = "Kawasaki", width = 15, font = 16, bg = "dark gray")
kohler = Button(top_frame, text = "Kohler", width = 15, font = 16, bg = "dark gray")
scag = Button(top_frame, text = "Scag", width = 15, font = 16, bg = "dark gray")
schiller = Button(top_frame, text = "Schiller", width = 15, font = 16, bg = "dark gray")
toro = Button(top_frame, text = "Toro", width = 15, font = 16, bg = "dark gray")


briggs.grid(row = 1, column = 0)
exmark.grid(row = 1, column = 1)
honda.grid(row = 1, column = 2)
kawasaki.grid(row = 1, column = 3)
kohler.grid(row = 2, column = 0)
scag.grid(row = 2, column = 1)
schiller.grid(row = 2, column = 2)
toro.grid(row = 2, column = 3)

bottom_box = Listbox(top_frame, width = 50, height = 3)
bottom_box.insert(1, "Website = " + str(website))
bottom_box.insert(2, "Username = " + str(username))
bottom_box.insert(3, "Password = " + str(password))
bottom_box.grid(columnspan = 5)


root.config(menu = menu_bar)
root.mainloop()