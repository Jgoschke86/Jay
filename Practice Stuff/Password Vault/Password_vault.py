import sqlite3, hashlib
from tkinter import *




#Database Code
with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")


#Initiate Window
window =Tk()
window.title("Password Vault")

def hash_password(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()
    return hash


def first_time_screen():
    window.geometry("250x140")

    def save_password(evt):
        if txt.get() == txt1.get():
            hashed_password = hash_password(txt.get().encode("utf-8"))
            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashed_password)])
            db.commit()
            password_vault()
        else:
            lbl2.config(text = "Passwords do not match")
            txt.delete(0, END)
            txt1.delete(0,END)
            txt.focus()

    def move_cursor(event = None):
        txt1.focus()

    lbl = Label(window, text = "Create Master Password")
    lbl.config(anchor = CENTER)
    lbl.pack()

    txt = Entry(window, width = 20, show = "*")
    txt.bind("<Return>", move_cursor)
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text = "Re-enter Master Password")
    lbl1.config(anchor = CENTER)
    lbl1.pack()

    txt1 = Entry(window, width = 20, show = "*")
    txt1.bind("<Return>", save_password)
    txt1.pack()

    lbl2 = Label(window)
    lbl2.pack()

    btn = Button(window, text = "Submit", command = save_password)
    btn.pack(pady = 10)

def login_screen():
    window.geometry("250x100")

    def get_master_password():
        check_hashed_password = hash_password(txt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(check_hashed_password)])
        return cursor.fetchall()

    def check_password(evt):
        password = get_master_password()
        if password:
            password_vault()
        else:
            wrong_lbl.config(text = "Wrong Password")
            txt.delete(0, END)

    lbl = Label(window, text = "Enter Master Password")
    lbl.config(anchor = CENTER)
    lbl.pack()

    txt = Entry(window, width = 20, show = "*")
    txt.bind("<Return>", check_password)
    txt.pack()
    txt.focus()

    wrong_lbl = Label(window)
    wrong_lbl.pack()

    btn = Button(window, text = "Submit", command = check_password)
    btn.pack(pady = 10)



def password_vault():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("700x350")


    lbl = Label(window, text = "Password Vault")
    lbl.config(anchor = CENTER)
    lbl.pack()

cursor.execute("SELECT * FROM masterpassword")
if (cursor.fetchall()):
    login_screen()
else:
    first_time_screen()

window.mainloop()