from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime

date = datetime.datetime.now()

def set_value(row_number, assigned_value):
    if "nan":
        pass
    else:
        return assigned_value[row_number] 

# page = requests.get("https://www.microcenter.com/search/search_results.aspx?N=4294966995&NTK=all&sortby=pricelow&rpp=96")
# source = page.content
# soup = BeautifulSoup(source, "lxml")

# soup = BeautifulSoup(open("Processors_CPUs _ Micro Center.html"), "html.parser")  #Home file source
soup = BeautifulSoup(open(r"C:/Python Stuff/Processors_CPUs _ Micro Center.html"), "html.parser")   #Work file source

amd_file = pd.read_csv(r"C:/Python Stuff/amd_pricing.csv")
# intel_content = pd.read_csv(r"D:\Python Stuff\intel_pricing.csv")
amd_content = pd.DataFrame(amd_file)

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
# for link in links:
#     if "Intel" in link.text:
#         if link.get("data-name") == None:
#             pass
#         else:
#             name = link.get("data-name")
#             name = ' '.join(name.split()[:2])
#             price = link.get("data-price")
#             intel_proc[name] = price

for key,value in amd_proc.items():
    new_item = {key:value}
    if amd_content.isin(new_item).any().any():
        pass
    else:
        print(new_item, " added")
        amd_content.append(new_item, ignore_index=True)

amd_content[date.strftime("%x")] = amd_content["Name"].map(amd_proc)
print(amd_content)
# amd_content.sort_values(by = ["Name"])
# intel_content.sort_values(by = ["Name"])

# amd_content[date.strftime("%x")] = amd_content["Name"].apply(set_value, args = (amd_proc, ))
# intel_content[date.strftime("%x")] = intel_content["Name"].apply(set_value, args = (intel_proc, ))


amd_content.to_csv("C:/Python Stuff/amd_pricing.csv",index = False)
# intel_content.to_csv(r"C:\Python Stuff\intel_pricing.csv", index = False)

# print(amd_content)
# print(intel_content)
