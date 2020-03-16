import tkinter as tk
import xlrd, time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


trin = xlrd.open_workbook(r"S:\OPE\Justin\Training Info.xlsx")
# trin = xlrd.open_workbook(r"C:\Users\jgosc\Documents\GitHub\Jay\Work\Training Info.xlsx")
sheet = trin.sheet_by_index(0)
manufacturers = ["Briggs", "Exmark", "Honda", "Kawasaki", "Kohler", "Kubota", "MTD", "Scag", "Stihl", "Toro"]
manufacturers.sort()
num = 1


def key_path():
    if manufacturers == "Briggs"
        name_path = 
        password_path = 
        button_press = 
    if manufacturers == "Exmark":
        name_path = "//*[@id=\"userNameBox\"]"
        password_path = "//*[@id=\"passWordBox\"]"
        button_press = "//*[@id=\"submit\"]"
    if manufacturers == "Honda":
        name_path = 
        password_path = 
        button_press = 
    if manufacturers == "kawasaki":
        name_path = 
        password_path = 
        button_press = 
    elif manufacturers == "Kohler":
        name_path = "//*[@id=\"login_userid_tb\"]"
        password_path = "//*[@id=\"login_password_tb\"]"
        button_press = "//*[@id=\"login_btn\"]"
    elif manufacturers == "Kubota":
        name_path = 
        password_path = 
        button_press = 
    elif manufacturers == "MTD":
        name_path = 
        password_path = 
    elif manufacturers == "Scag":
        name_path = "//*[@id=\"login_userid\"]"
        password_path = "//*[@id=\"login_pwd\"]"
        button_press = "//*[@id=\"loginFormBottom\"]/input[2]"
    elif manufacturers == "Stihl":
        additional_press = 
        name_path = "//*[@id=\"login-form\"]/form/table/tbody/tr[2]/td[2]/input"
        password_path = "//*[@id=\"login-form\"]/form/table/tbody/tr[3]/td[2]/input"
        button_press = "//*[@id=\"login\"]"
    elif manufacturers== "Toro":
        additional_press = "//*[@id=\"loginIcon\"]"
        name_path = "//*[@id=\"username\"]"
        password_path = "//*[@id=\"password\"]"
        button_press = "//*[@id=\"loginButton\"]"


root = tk.Tk()
root.title("Training Logins")


def execute(evt):
    driver = webdriver.Chrome(executable_path = r"C:\Users\jgoschke\Downloads\chromedriver.exe")
    driver.maximize_window()
    man_name = man_box.get(man_box.curselection())
    for i in range(sheet.nrows):
        if sheet.cell_value(i,0) == man_name:
            username = sheet.cell_value(i,1)
            password = sheet.cell_value(i,2)
            website = sheet.cell_value(i,3)
        else:
            pass
    driver.get(website)
    name_input = driver.find_element_by_xpath(name_path)
    pass_input = driver.find_element_by_xpath(password_path)
    name_input.send_keys(username)
    pass_input.send_keys(password)
    
    time.sleep(2)
    os.system("taskkill /f /im chromedriver.exe")

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