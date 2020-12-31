from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import subprocess




date = datetime.datetime.now()
page = requests.get(r"https://www.microcenter.com/search/search_results.aspx?N=4294966995&NTK=all&sortby=pricelow&myStore=false&rpp=96")
soup = BeautifulSoup(page.text, "html.parser")

# soup = BeautifulSoup(open("Processors_CPUs _ Micro Center.html"), "html.parser")  #Home file source
# soup = BeautifulSoup(open(r"D:/Python Stuff/Processors_CPUs _ Micro Center.html"), "html.parser")   #Work file source

amd_file = pd.read_csv(r"D:/Python Stuff/WebScrapers/Processors/amd_pricing.csv")
intel_file = pd.read_csv(r"D:/Python Stuff/WebScrapers/Processors/intel_pricing.csv")
amd_content = pd.DataFrame(amd_file)
intel_content = pd.DataFrame(intel_file)


amd_proc_list = amd_content['Name'].tolist()
intel_proc_list = intel_content['Name'].tolist()
append_to_csv = {}
amd_proc = {}
intel_proc = {}

links = soup.find_all("a")
for link in links:
    if "AMD" in link.text:
        if link.get("data-name") == None:
            pass
        else:
            name = link.get("data-name")
            name = ' '.join(name.split()[:3])
            price = link.get("data-price")
            amd_proc[name] = price
    if "Intel" in link.text:
        if link.get("data-name") == None:
            pass
        else:
            name = link.get("data-name")
            name = ' '.join(name.split()[:2])
            price = link.get("data-price")
            intel_proc[name] = price

for key,value in amd_proc.items():
    new_item = {key:value}
    if key in amd_proc_list:
        pass
    else:
        print(new_item, " added")
        append_to_csv["Name"] = key
        amd_content = amd_content.append(append_to_csv, ignore_index=True)
for key,value in intel_proc.items():
    new_item = {key:value}
    if key in intel_proc_list:
        pass
    else:
        print(new_item, " added")
        append_to_csv["Name"] = key
        intel_content = intel_content.append(append_to_csv, ignore_index=True)

amd_content[date.strftime("%x")] = amd_content["Name"].map(amd_proc)
intel_content[date.strftime("%x")] = intel_content["Name"].map(intel_proc)


amd_content = amd_content.sort_values(by = ["Name"])
intel_content = intel_content.sort_values(by = ["Name"])

print(amd_content)
print(intel_content)
amd_content.to_csv("D:/Python Stuff/WebScrapers/Processors/amd_pricing.csv",index = False)
intel_content.to_csv("D:/Python Stuff/WebScrapers/Processors/intel_pricing.csv", index = False)


subprocess.call("Proc_Price_analyze.py", shell = True)