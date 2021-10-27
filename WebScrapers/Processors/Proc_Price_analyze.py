import pandas as pd
import numpy as np


# opening files
amd_file = pd.read_csv(r"C:/Python Stuff/Jay/WebScrapers/Processors/Data/amd_pricing.csv")
intel_file = pd.read_csv(r"C:/Python Stuff/Jay/WebScrapers/Processors/Data/intel_pricing.csv")
# amd_file = pd.DataFrame(amd_file)
# intel_file = pd.DataFrame(intel_file)
files = [amd_file, intel_file]
amd_file.set_index("Name", inplace = True)
intel_file.set_index("Name", inplace = True)

# Lists to store data from scraped data
name = []
min_price = []
max_price = []

# Get name, low and high price of processor from files
for file in files:
    for indx,row in file.iterrows():
        price = row.values
        high_price = np.nanmax(price)
        low_price = np.nanmin(price)
        name.append(indx)
        min_price.append(low_price)
        max_price.append(high_price)
        # print(f"""{indx}
        #         Min cost {low_price}
        #         High {high_price}""")

# Create dataframe to write to file
price_df = pd.DataFrame({"Name" :name, "Min Price" : min_price, "Max Price" : max_price})

# Write to file
price_df.to_csv("C:/Python Stuff/Jay/WebScrapers/Processors/Data/Proc_Price_Data.csv", index = False)