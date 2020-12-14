from bs4 import BeautifulSoup
import pandas as pd
import requests


# page = requests.get("https://www.microcenter.com/search/search_results.aspx?N=4294966995&NTK=all&sortby=pricelow&rpp=96")
# source = page.content
# soup = BeautifulSoup(source, "lxml")
soup = BeautifulSoup(open(r"C:/Users/jgosc/Downloads/Processors_CPUs _ Micro Center.html"), "html.parser")


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
            # print(name, price)
for link in links:
    if "Intel" in link.text:
        if link.get("data-name") == None:
            pass
        else:
            name = link.get("data-name")
            name = ' '.join(name.split()[:2])
            price = link.get("data-price")
            intel_proc[name] = price
            # print(name, price)
# print(amd_proc)
# print(intel_proc)

amd_db = pd.DataFrame({"Name" : list(amd_proc.keys()), "Price" : list(amd_proc.values())})
print(amd_db)
intel_db = pd.DataFrame({"Name" : list(intel_proc.keys()), "Price" : list(intel_proc.values())})
print(intel_db)