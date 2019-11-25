from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



root = Tk()

root.title("Website Shortcuts")

var = StringVar()
Briggs = ["Briggs and Stratton", "https://www.thepowerportal.com/Login.htm", "117690", "briggs"]
Exmark = ["Exmark", "https://user.exmark.com/login?returnUrl=https://extranet.exmark.com", "320163", "MJBwz54-"]
Honda = ["Honda", "https://www.in.honda.com/", "bps", "Buckeyebps23"]
Kawasaki = ["Kawasaki Engines", "www.kawasakipower.com", "rmorrison", "bep0wer2"]
Kohler = ["Kohler Engines", "https://pswusers.arinet.com/Kohler", "28950002064", "Buckeye1"]
Scag = ["Scag Mowers", "www.scagtech.com", "338035dlr", "shadow"]
Schiller = ["Schiller/Ryan/Bobcat", "www.schillergcpro.com", "rmorrison", "reneem"]
Stihl = ["Stihl", "www.stihleservice.com", "Service", "buckeye"]
Toro = ["Toro", "http://dealer.thetorocompany.com/", "405214bohlg1", "shadow12"]

manufacturers = [Briggs, Exmark, Honda, Kawasaki, Kohler, Scag, Schiller, Stihl, Toro]


def execute(evt):
    selected = man_box.curselection()
    details = man_box.get(selected)
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
    var.set(manu_info[0] + "\n" + manu_info[1] + "\n" + "Username: " + manu_info[2] + "\n" + "Password: " + manu_info[3])
    print(selected)
    print(details)
    

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
info_box = Label(root, textvariable = var, width = 45, height = 10)
info_box.config(textvariable = var)
info_box_top.grid(row = 0, column = 4)
info_box.grid(row = 1, column = 4)





root.config(menu = menu_bar)
root.mainloop()