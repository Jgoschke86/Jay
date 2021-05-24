from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime




date = datetime.datetime.now()
proc_page = requests.get(r"https://www.microcenter.com/search/search_results.aspx?N=4294966995&NTK=all&sortby=pricelow&myStore=false&rpp=96")
proc_soup = BeautifulSoup(proc_page.text, "html.parser")
# vid_page = requests.get(r"https://www.microcenter.com/search/search_results.aspx?N=4294966937&NTK=all&sortby=pricelow&rpp=96&myStore=false")
# vid_soup = BeautifulSoup(vid_page.text, "html.parser")
# proc_soup = BeautifulSoup(open("Processors_CPUs _ Micro Center.html"), "html.parser")  #Home file source
# proc_soup = BeautifulSoup(open(r"D:/Python Stuff/Processors_CPUs _ Micro Center.html"), "html.parser")   #Work file source
# vid_soup = BeautifulSoup(open(r"D:/Python Stuff/Video Cards _ Micro Center", "html.parser"))

amd_file = pd.read_csv(r"Z:/Python Stuff/Jay\WebScrapers/Processors/amd_pricing.csv")
intel_file = pd.read_csv(r"Z:/Python Stuff/Jay\WebScrapers/Processors/intel_pricing.csv")
# vid_file = pd.read_csv(r"D:/Python Stuff/vid_pricing.csv")
amd_content = pd.DataFrame(amd_file)
intel_content = pd.DataFrame(intel_file)
# vid_content = pd.DataFrame(vid_file)

amd_proc_list = amd_content['Name'].tolist()
intel_proc_list = intel_content['Name'].tolist()
# vid_list = vid_content['Name'].tolist()
append_to_csv = {}
amd_proc = {}
intel_proc = {}
vid_card = {}

proc_links = proc_soup.find_all("a")
# vid_links = vid_soup.find_all("a")

for link in proc_links:
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
    links = proc_soup.find_all("a")
# for link in vid_links:
#     if link.get("data-name") == None:
#         pass
#     else:
#         name = link.get("data-name")
#         brand = link.get("data-brand")
#         name = brand, " ", name
#         price = link.get("data-price")
#         vid_card[name] = price

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
# for key,value in vid_card.items():
#     new_item = {key:value}
#     if key in vid_list:
#         pass
#     else:
#         print(new_item, " added")
#         append_to_csv["Name"] = key
#         vid_content = vid_content.append(append_to_csv, ignore_index=True)

amd_content[date.strftime("%x")] = amd_content["Name"].map(amd_proc)
intel_content[date.strftime("%x")] = intel_content["Name"].map(intel_proc)
# vid_content[date.strftime("%x")] = vid_content["Name"].map(vid_content)

amd_content = amd_content.sort_values(by = ["Name"])
intel_content = intel_content.sort_values(by = ["Name"])
# vid_content = vid_content.sort_values(by = ["Name"])

print(amd_content)
print(intel_content)
amd_content.to_csv("Z:\Python Stuff\Jay\WebScrapers\Processors/amd_pricing.csv",index = False)
intel_content.to_csv("Z:\Python Stuff\Jay\WebScrapers\Processors/intel_pricing.csv", index = False)


exec(open("Z:/Python Stuff/Jay/WebScrapers/Processors/Proc_Price_analyze.py").read())