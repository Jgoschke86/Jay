speed = int(input("What is the speed? "))
over_speed = int((speed - 70)/5)
if over_speed <= 12:
    print(f"Points {over_speed}")
else:
    print("License suspended")






# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import os, time, psutil

# browser = webdriver.Firefox()
# browser.maximize_window()
# browser.get("https:\\www.facebook.com")

# username = browser.find_element_by_css_selector("#email")
# username.send_keys("jgoschke86@gmail.com")

# password = browser.find_element_by_css_selector("#pass")
# password.send_keys("Justin1986" + Keys.ENTER)

# time.sleep(5)



# def findProcessIdByName(processName):
#     listOfProcessObjects = []
#     for proc in psutil.process_iter():
#        try:
#            pinfo = proc.as_dict(attrs=['pid', 'name'])
#            if processName.lower() in pinfo['name'].lower() :
#                listOfProcessObjects.append(pinfo)
#        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
#            pass
#     return listOfProcessObjects;
# listOfProcessIds = findProcessIdByName('geckodriver')
# if len(listOfProcessIds) > 0:
#     for elem in listOfProcessIds:
#         processID = elem['pid']
#         os.system("taskkill /f /PID " + str(processID))



# game_on = True
# def Jay():
#     if answer == "y":
#         return True
#     else:
#         return False
    

# while game_on:
#     print(game_on)
#     answer = input("play again? ")
#     print(answer)
#     game_on = Jay()
    
# import openpyxl
# from openpyxl.xml.constants import MAX_COLUMN, MAX_ROW
# wb = openpyxl.load_workbook(r"D:\Python Stuff\Test Log.xlsx")
# print(wb.sheetnames)
# ws = wb.active
# row_length = len(ws["B"])
# print(row_length)
# for i in range(0, int(row_length)):
#     print(i, ws.cell(row = i, column = 1).value)



# import datetime
# date = datetime.datetime.now()
# print(date.strftime("%x"))


