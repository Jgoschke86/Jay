"""  Scrapes website for price data  """
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests



#  Todays date
date = datetime.datetime.now()

# Opening Webpage and converting to readable format
proc_page = requests.get(r"https://www.microcenter.com/search/search_results.aspx?N=4294966995&NTK=all&sortby=pricelow&rpp=96&myStore=false")
proc_soup = BeautifulSoup(proc_page.text, "html.parser")
vid_page1 = requests.get(r"https://www.microcenter.com/search/search_results.aspx?N=4294966937&NTK=all&sortby=pricehigh&rpp=96&myStore=false")
vid_soup1 = BeautifulSoup(vid_page1.text, "html.parser")
vid_page2 = requests.get(r"https://www.microcenter.com/search/search_results.aspx?N=4294966937&NTK=all&sortby=pricehigh&rpp=96&page=2&myStore=false")
vid_soup2 = BeautifulSoup(vid_page2.text, "html.parser")


# Opening existing data
amd_file = pd.read_csv(r"C:/Python Stuff/WebScrapers/Micro Center/Data/amd_pricing.csv")
intel_file = pd.read_csv(r"C:/Python Stuff/WebScrapers/Micro Center/Data/intel_pricing.csv")
vid_file = pd.read_csv(r"C:/Python Stuff/WebScrapers/Micro Center/Data/vid_pricing.csv")
amd_content = pd.DataFrame(amd_file)
intel_content = pd.DataFrame(intel_file)
vid_content = pd.DataFrame(vid_file)

# Takes existing data and puts names into a list for comparison
amd_proc_list = amd_content['Name'].tolist()
intel_proc_list = intel_content['Name'].tolist()
vid_list = vid_content['Name'].tolist()
append_to_csv = {}   # Dictionary for new items
amd_proc = {}   #  Stores the data to write to csv
intel_proc = {}   #  Stores the data to write to csv
vid_card = {}    #  Stores the data to write to csv

proc_links = proc_soup.find_all("a")   #  Finds all instances where data is
vid_links1 = vid_soup1.find_all("a")   #  Finds all instances where data is
vid_links2 = vid_soup2.find_all("a")   #  Finds all instances where data is

for link in proc_links:
    if "AMD" in link.text:  #  Scans all of the "a" for AMD
        if link.get("data-name") is None:  #  If not a valid instance, skips it
            pass
        else:
            name = link.get("data-name")  #  Gets the name of the processor
            name = ' '.join(name.split()[:3])  #  Cuts off words of the name to make easier to read
            price = link.get("data-price")  #  Gets price of processor
            amd_proc[name] = price  #  Adds data to dictionary
    if "Intel" in link.text:  #  Scans all of the "a" for Intel
        if link.get("data-name") is None:  #  If not a valid instance, skips it
            pass
        else:
            name = link.get("data-name")  #  Gets the name of the processor
            name = ' '.join(name.split()[:2])  #  Cuts off words of the name to make easier to read
            price = link.get("data-price")  #  Gets price of processor
            intel_proc[name] = price  #  Adds data to dictionary
            
for link in vid_links1:  #  Page 1 of video cards
    if link.get("data-name") is None:  #  If not a valid instance, skips it
        pass
    elif link.get("data-brand") is None:  #  If not a valid instance, skips it
        pass
    else:
        name = link.get("data-name")  #  Gets name of video card
        brand = link.get("data-brand")  #  Gets brand of video card
        name = brand + " " + name  #  Puts brand and name together
        name = ' '.join(name.split()[:-4])
        price = link.get("data-price")  #  Gets price of card
        vid_card[name] = price  #  Adds data to dictionary
for link in vid_links2:  #  Page 2 of video cards
    if link.get("data-name") is None:  #  If not a valid instance, skips it
        pass
    elif link.get("data-brand") is None:  #  If not a valid instance, skips it
        pass
    else:
        name = link.get("data-name")  #  Gets name of video card
        brand = link.get("data-brand")  #  Gets brand of video card
        name = brand + " " + name  #  Puts brand and name together
        name = ' '.join(name.split()[:-4])
        price = link.get("data-price")  #  Gets price of card
        vid_card[name] = price  #  Adds data to dictionary

for key,value in amd_proc.items():
    new_item = {key:value}  #  Takes each instance of data
    if key in amd_proc_list:  #  If processor already in file(dictionary) skips it
        pass
    else:
        print(new_item, " added")  #  Prints new item to be added to file
        append_to_csv["Name"] = key  #  Adds name of processor to file
        amd_content = amd_content.append(append_to_csv, ignore_index=True)
for key,value in intel_proc.items():
    new_item = {key:value}  #  Takes each instance of data
    if key in intel_proc_list:  #  If processor already in file(dictionary) skips it
        pass
    else:
        print(new_item, " added")  #  Prints new item to be added to file
        append_to_csv["Name"] = key  #  Adds name of processor to file
        intel_content = intel_content.append(append_to_csv, ignore_index=True)
for key,value in vid_card.items():
    new_item = {key:value}  #  Takes each instance of data
    if key in vid_list:  #  If card already in file(dictionary) skips it
        pass
    else:
        print(new_item, " added")  #  Prints new item to be added to file
        append_to_csv["Name"] = key  #  Adds name of new card to be added to dictionary
        vid_content = vid_content.append(append_to_csv, ignore_index=True)  #  Adds new card from dict to file under "Name" column

amd_content[date.strftime("%x")] = amd_content["Name"].map(amd_proc)  #  Creates new column with date, finds processor name and adds price to column
intel_content[date.strftime("%x")] = intel_content["Name"].map(intel_proc)  #  Creates new column with date, finds processor name and adds price to column
vid_content[date.strftime("%x")] = vid_content["Name"].map(vid_card)  #  Creates new column with date, finds card name and adds price to column

amd_content = amd_content.sort_values(by = ["Name"])  #  Sorts file by name of processor
intel_content = intel_content.sort_values(by = ["Name"])  #  Sorts file by name of processor
vid_content = vid_content.sort_values(by = ["Name"])  #  Sorts file by name of cards

# print(amd_content)
# print(intel_content)
# print(vid_content)
amd_content.to_csv("C:/Python Stuff/WebScrapers/Micro Center/Data/amd_pricing.csv",index = False)  #  Writes to file and saves it
intel_content.to_csv("C:/Python Stuff/WebScrapers/Micro Center/Data/intel_pricing.csv", index = False)  #  Writes to file and saves it
vid_content.to_csv(r"C:/Python Stuff/WebScrapers/Micro Center/Data/vid_pricing.csv", index = False)  #  Writes to file and saves it

exec(open("C:/Python Stuff/WebScrapers/Micro Center/Proc_Price_analyze.py").read())
