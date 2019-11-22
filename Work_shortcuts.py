from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


root = Tk()

root.title("Website Shortcuts")


Briggs = {"Manufacturer:": "Briggs and Stratton", "Website:": "https://www.thepowerportal.com/Login.htm", "Username:": "117690", "Password:": "briggs"}


manufacturers = [Briggs]



def execute(evt):
    selected = man_box.curselection()
    details = man_box.get(selected[0])
    driver = webdriver.Chrome(executable_path=r"C:\Users\jgoschke\Downloads\chromedriver.exe")
    if details == "Briggs":
        driver.get("https://www.thepowerportal.com/Login.htm")
        name_input = driver.find_element_by_xpath("//*[@id=\"usernameloginBlock1\"]")
        name_input.send_keys("117690")
        pass_input = driver.find_element_by_xpath("//*[@id=\"passwordloginBlock1\"]")
        pass_input.send_keys("briggs")
        login_button = driver.find_element_by_xpath("//*[@id=\"loginSubmitloginBlock1\"]").click()
        
def on_selection(evt):
    selected = man_box.curselection()
    details = man_box.get(selected[0])
    manu_info = manufacturers[selected[0]]
    print(selected)
    print(details)
    Labelvar.set(manu_info.items())
        
    # elif details == "Exmark":
    #     Labelvar.set("""Exmark Mowers
    #     https://www.exmark.com/
    #     Username = 320163
    #     Password = MJBwz54-""")
    # elif details == "Honda":
    #     Labelvar.set("""Honda Power Equipment
    #     http://www.in.honda.com/
    #     Username = bps
    #     Password = Buckeyebps23""")
    # elif details == "Kawasaki":
    #     Labelvar.set("""Kawasaki Engines
    #     www.kawasaki.com
    #     Username = blak black
    #     Password = lfdkjngvlkdsfng""")
    # elif details == "Kohler":
    #     Labelvar.set("""Kohler Engines
    #     www.brigssandstratton.com
    #     Username = blak black
    #     Password = lfdkjngvlkdsfng""")
    # elif details == "Scag":
    #     Labelvar.set("""Scag Mowers
    #     www.scag.com
    #     Username = blak black
    #     Password = lfdkjngvlkdsfng""")
    # elif details == "Schiller":
    #     Labelvar.set("""Schiller/Bobcat/Ryan
    #     www.schiller.com
    #     Username = blak black
    #     Password = lfdkjngvlkdsfng""")
    # elif details == "Stihl":
    #     Labelvar.set("""Bryan Equipment
    #     www.bryanequipment.com
    #     Username = rmorrison@buckeyepowersales.com
    #     Password = BUCKEYE1""")
    # elif details == "Toro":
    #     Labelvar.set("""Toro Power Equipment
    #     www.toro.com
    #     Username = blak black
    #     Password = lfdkjngvlkdsfng""")

def about_window():
    top = Toplevel()
    top.title("About")
    about_text = Label(top, text = """Created by Justin Goschke
    v1.0""", font = 15)
    about_text.pack()
    back_button = Button(top, text = "Back", command = top.destroy, width = 15, font = 16, bg = "dark gray")
    back_button.pack()
    top.mainloop()


menu_bar = Menu(root)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "About", command = about_window)
file.add_command(command = root.destroy, label = "Exit")

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
man_box.insert(8, "Stihl")
man_box.insert(9, "Toro")
man_box.bind("<<ListboxSelect>>", on_selection)
man_box.grid(row = 0, column = 0, rowspan = 3)


go_button = Button(root, text = "GO", font = 16, width = 15, bg = "dark gray")
go_button.grid(row = 1, column = 1)
go_button.bind("<Button-1>", execute)

info_box_top = Label(root, text = "Login Information")
info_box = Label(root, textvariable = Labelvar, width = 45, height = 10)
info_box.config(textvariable = Labelvar)
info_box_top.grid(row = 0, column = 4)
info_box.grid(row = 1, column = 4)


root.config(menu = menu_bar)
root.mainloop()