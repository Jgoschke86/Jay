from bs4 import BeautifulSoup
import pandas as pd
import requests


page = requests.get("https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=pricelow&N=4294966995&myStore=false")
source = page.content
soup = BeautifulSoup(source, "lxml")

links = soup.find_all("li", attrs = {"class": "product_wrapper"})
for link in range(len(links)):
    print(link)

# if "AMD" in links:
#     name = links.div.a.get("data-name")
#     # name = ' '.join(name.split()[:3])
#     price = links.div.a.get("data-price")
#     print(name, price)

    # if "Intel" in links.text:
    #     name = links.h2.a.get("data-name")
    #     name = ' '.join(name.split()[:2])
    #     price = links.h2.a.get("data-price")
    #     print(name, price)
