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

import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")
