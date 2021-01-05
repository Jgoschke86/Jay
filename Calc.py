import tkinter as tk
import tkinter.messagebox as tm
import time

login = tk.Tk()
access = False
username = "Justin"
password = "Password"
def login_staus():
    input_name = name_entry.get()
    input_pass = pass_entry.get()
    if input_name != username or input_pass != password:
        tm.showerror("Login Failed", "Login information is wrong")
    else:
        login.destroy()
        window = tk.Tk()
        window.title("Calculator")
        window.geometry("500x600")
        window.resizable(0,0)
        access = True
        return access
if access == False:
    tk.Label(login, text = "Username").grid(row = 0)
    tk.Label(login, text = "Password").grid(row = 1)
    login_button = tk.Button(login, text = "Login", command = login_staus).grid(row = 2, columnspan = 2)
    name_entry = tk.Entry(login)
    name_entry.grid(row = 0, column = 1)
    pass_entry = tk.Entry(login, show = "*")
    pass_entry.grid(row = 1, column = 1)


elif access == True:
    login.destroy()
    window = tk.Tk()
    butt1 = tk.Button(text = "Button").grid(row = 0, column = 1)
    window.mainloop()



login.mainloop()