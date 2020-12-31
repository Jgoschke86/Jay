
from bs4 import BeautifulSoup
import pandas as pd 
import datetime

date = datetime.datetime.now()

def set_value(row_number, assigned_value): 
    return assigned_value[row_number] 



soup = BeautifulSoup(open("Processors_CPUs _ Micro Center.html"), "html.parser")  #Home file source
amd_content = pd.read_csv(r"D:\Python Stuff\amd_pricing.csv")

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
amd_db = pd.DataFrame({"Name" : list(amd_proc.keys()), date.strftime("%x") : list(amd_proc.values())})
# amd_content[date.strftime("%x")] = amd_content["Name"].apply(set_value, args = (amd_proc, ))

amd_db.to_csv(r"D:/Python Stuff/amd_pricing.csv", index = False)

