import pandas as pd
import numpy as np 



amd_file = pd.read_csv(r"D:/Python Stuff/amd_pricing.csv")
intel_file = pd.read_csv(r"D:/Python Stuff/intel_pricing.csv")
amd_file = pd.DataFrame(amd_file)
intel_file = pd.DataFrame(intel_file)
files = [amd_file, intel_file]
amd_file.set_index("Name", inplace = True)
intel_file.set_index("Name", inplace = True)


name = []
min = []
max = []
aver = []

all_data = {"Name":name, "Min $":min, "Max $":max, "Aver $":aver}

for file in files:
    for indx,row in file.iterrows():
        price = row.values
        aver_price = np.nanmean(price)
        aver_price = np.around(aver_price, decimals = 2)
        high_price = np.nanmax(price)
        low_price = np.nanmin(price)
        name.append(indx)
        min.append(low_price)
        max.append(high_price)
        aver.append(aver_price)
        # print(f"""{indx}
        #         Min cost {low_price}
        #         High {high_price}
        #         Average {aver_price}""")

df = pd.DataFrame(all_data)
df.to_csv("Proc_Price_Data.csv", index = False)