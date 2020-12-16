from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime

date = datetime.datetime.now()

def set_value(row_number, assigned_value): 
    return assigned_value[row_number] 

# page = requests.get("https://www.microcenter.com/search/search_results.aspx?N=4294966995&NTK=all&sortby=pricelow&rpp=96")
# source = page.content
# soup = BeautifulSoup(source, "lxml")

# soup = BeautifulSoup(open(r"C:/Users/jgosc/Downloads/Processors_CPUs _ Micro Center.html"), "html.parser")  #Home file source
soup = BeautifulSoup(open(r"C:/Python Stuff/Processors_CPUs _ Micro Center.html"), "html.parser")   #Work file source

amd_content = pd.read_csv(r"C:\Python Stuff\amd_pricing.csv")
intel_content = pd.read_csv(r"C:\Python Stuff\intel_pricing.csv")


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
for link in links:
    if "Intel" in link.text:
        if link.get("data-name") == None:
            pass
        else:
            name = link.get("data-name")
            name = ' '.join(name.split()[:2])
            price = link.get("data-price")
            intel_proc[name] = price
in_list = exists = key in amd_content.A
for key in amd_proc.keys():
    if key not in in_list:
        amd_proc.pd.DataFrame({key : [value]})


amd_content[date.strftime("%x")] = amd_content["Name"].apply(set_value, args = (amd_proc, ))
intel_content[date.strftime("%x")] = intel_content["Name"].apply(set_value, args = (intel_proc, ))

df.sort_values(by=['Name'])
amd_content.to_csv(r"C:\Python Stuff\amd_pricing.csv", index = False)
intel_content.to_csv(r"C:\Python Stuff\intel_pricing.csv", index = False)

print(amd_content)
print(intel_content)