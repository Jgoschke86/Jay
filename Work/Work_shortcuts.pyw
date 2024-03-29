import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import xlrd
import time
import os


# Opens the excel sheet to read it
intwarr = xlrd.open_workbook(r"S:\OPE\OPE Service\INTERNET WARRANTY SIGN ONS.xls")
sheet = intwarr.sheet_by_index(0)
cell = sheet.cell(0,3)
num = 1

# creates Kinter window
root = tk.Tk()

root.title("Website Shortcuts")

# Login information extracted from excel sheet
brg_usr = sheet.cell_value(18, 1)
brg_pass = sheet.cell_value(19, 1)
exm_usr = sheet.cell_value(50, 1)
exm_pass = sheet.cell_value(51, 1)
hon_usr = sheet.cell_value(82, 1)
hon_pass = sheet.cell_value(51, 1)
hon_usr = sheet.cell_value(82, 1)
hon_pass = sheet.cell_value(83, 1)
kaw_usr = sheet.cell_value(103, 1)
kaw_pass = sheet.cell_value(104, 1)
koh_usr = sheet.cell_value(107, 1)
koh_pass = sheet.cell_value(108, 1)
scg_usr = sheet.cell_value(195, 1)
scg_pass = sheet.cell_value(196, 1)
sch_usr = sheet.cell_value(191, 1)
sch_pass = sheet.cell_value(192, 1)
stl_usr = sheet.cell_value(22, 1)
stl_pass = sheet.cell_value(23, 1)
tor_usr = sheet.cell_value(230, 1)
tor_pass = sheet.cell_value(231, 1)


# Manufacturer information in list form to pull to get used
var = tk.StringVar()
Briggs = ["Briggs and Stratton", "https://www.thepowerportal.com/Login.htm",
          str(int(brg_usr)), str(brg_pass)]
Exmark = ["Exmark", "https://user.exmark.com/login?returnUrl=https://extranet.exmark.com",
          str(int(exm_usr)), str(exm_pass)]
Honda = ["Honda", "https://www.in.honda.com/",
         str(hon_usr), str(hon_pass), "310577"]
Kawasaki = ["Kawasaki Engines", "https://www.kawasakipower.com/",
            str(kaw_usr), str(kaw_pass)]
Kohler = ["Kohler Engines", "https://pswusers.arinet.com/Kohler",
          str(int(koh_usr)), str(koh_pass)]
Scag = ["Scag Mowers", "http://www.scagtech.com", str(scg_usr), str(scg_pass)]
Schiller = ["Schiller/Ryan/Bobcat",
            "https://www.schillergcpro.com", str(sch_usr), str(sch_pass)]
Stihl = ["Stihl", "https://dealers.stihlusa.com/Account",
         str(stl_usr), str(stl_pass)]
Toro = ["Toro", "http://dealer.thetorocompany.com/",
        str(tor_usr), str(tor_pass)]


manufacturers = [Briggs, Exmark, Honda, Kawasaki,
                 Kohler, Scag, Schiller, Stihl, Toro]
manufacturers.sort()


# What to do when button is pressed
def execute(evt):
    selected = man_box.curselection()
    details = man_box.get(selected[0])
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\jgoschke\Downloads\chromedriver.exe", chrome_options=options)

    if details == "Briggs and Stratton":
        driver.get(Briggs[1])
        name_input = driver.find_element_by_xpath(
            "//*[@id=\"usernameloginBlock1\"]")
        name_input.send_keys(Briggs[2])
        pass_input = driver.find_element_by_xpath(
            "//*[@id=\"passwordloginBlock1\"]")
        pass_input.send_keys(Briggs[3])
        driver.find_element_by_xpath(
            "//*[@id=\"loginSubmitloginBlock1\"]").click()
    elif details == "Exmark":
        driver.get(Exmark[1])
        name_input = driver.find_element_by_xpath("//*[@id=\"UserName\"]")
        name_input.send_keys(Exmark[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"Password\"]")
        pass_input.send_keys(Exmark[3])
        driver.find_element_by_xpath(
            "//*[@id=\"form0\"]/div/div/div[3]/div/p/input").click()
    elif details == "Honda":
        driver.get(Honda[1])
        dlr_input = driver.find_element_by_xpath(
            "/html/body/form/table[2]/tbody/tr[2]/td[2]/input")
        dlr_input.send_keys(Honda[4])
        name_input = driver.find_element_by_xpath("//*[@id=\"txtLogonID\"]")
        name_input.send_keys(Honda[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"txtPassword\"]")
        pass_input.send_keys(Honda[3])
        driver.find_element_by_xpath("//*[@id=\"btnLogon\"]").click()
    elif details == "Kawasaki Engines":
        driver.get(Kawasaki[1])
        name_input = driver.find_element_by_xpath("//*[@id=\"W_USERNAME\"]")
        name_input.send_keys(Kawasaki[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"LW3USRPAS\"]")
        pass_input.send_keys(Kawasaki[3])
        driver.find_element_by_xpath("//*[@id=\"Login\"]").click()
    elif details == "Kohler Engines":
        driver.get(Kohler[1])
    elif details == "Scag Mowers":
        driver.get(Scag[1])
        name_input = driver.find_element_by_xpath("//*[@id=\"txtUserName\"]")
        name_input.send_keys(Scag[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"txtUserPass\"]")
        pass_input.send_keys(Scag[3])
        driver.find_element_by_xpath("//*[@id=\"Button1\"]").click()
    elif details == "Schiller/Ryan/Bobcat":
        driver.get(Schiller[1])
        name_input = driver.find_element_by_xpath("//*[@id=\"sgcuser\"]")
        name_input.send_keys(Schiller[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"sgcpass\"]")
        pass_input.send_keys(Schiller[3])
        driver.find_element_by_xpath("//*[@id=\"sgcDoLogin\"]").click()
    elif details == "Stihl":
        driver.get(Stihl[1])
        name_input = driver.find_element_by_xpath("//*[@id=\"username\"]")
        name_input.send_keys(Stihl[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"password\"]")
        pass_input.send_keys(Stihl[3])
        driver.find_element_by_xpath(
            "//*[@id=\"content\"]/div/div/div/form/p[4]/input").click()
    elif details == "Toro":
        driver.get(Toro[1])
        name_input = driver.find_element_by_xpath("//*[@id=\"username\"]")
        name_input.send_keys(Toro[2])
        pass_input = driver.find_element_by_xpath("//*[@id=\"password\"]")
        pass_input.send_keys(Toro[3])
        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/form/div[6]/a").click()

    time.sleep(2)
    options.add_experimental_option("detach", True)
    os.system("taskkill /f /im chromedriver.exe")


# changes display in info_box based on what is selected for manufacturer
def on_selection(evt):
    selected = man_box.curselection()
    manu_info = manufacturers[selected[0]]
    var.set(manu_info[0] + "\n" + manu_info[1] + "\n" +
            "Username: " + manu_info[2] + "\n" + "Password: " + manu_info[3])


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


# Menu Bar details
menu_bar = tk.Menu(root)
file = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "About", command = about_window)
file.add_command(command = root.destroy, label = "Exit")

# The selection box details
Labelvar = tk.StringVar()
details = tk.StringVar()


# man_box = tk.Listbox(width = 20, border = 2)
# for name in manufacturers:
#     man_box.insert(num, name[0])
#     num += 1
# man_box.bind("<<ListboxSelect>>", on_selection)
# man_box.grid(row = 1, column = 0, rowspan = 3)


# Execute button
# go_button = tk.Button(root, text = "GO", font = 16, width = 15, bg = "dark gray")
# go_button.grid(row = 1, column = 1)
# go_button.bind("<Button-1>", execute)


# Display box for information
# info_box_top = tk.Label(root, text = "Login Information")
# info_box = tk.Label(root, width = 45, height = 10, relief = tk.SUNKEN, border = 2, bg = "white")
# info_box.config(textvariable = var)
# info_box_top.grid(row = 0, column = 4)
# info_box.grid(row = 1, column = 4)


# root.config(menu = menu_bar)
# root.mainloop()
