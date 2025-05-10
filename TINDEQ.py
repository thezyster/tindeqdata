import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import pandas as pd
import csv
import glob
import zipfile


# Load the CSV file
zip_paths = glob.glob('/home/zyster/Documents/coding/data/*.zip')
dfs = []

for zp in zip_paths:
    # optional: grab a label from the zip name
    label = zp.rsplit('/', 1)[-1].replace('.zip','')
    
    with zipfile.ZipFile(zp, 'r') as z:
        # iterate every file inside the zip
        for fname in z.namelist():
            # skip non-CSV
            if not fname.lower().endswith('.csv'):
                continue
            
            # open the CSV file inside the archive
            with z.open(fname) as f:
                df = pd.read_csv(f)
                
                # if you want to tag each row with its source zip:
                df['source_zip'] = label
                
                dfs.append(df)

# 3. Concatenate all into one big DataFrame:
if dfs:
    big_df = pd.concat(dfs, ignore_index=True,)
else:
    big_df = pd.DataFrame()
    
print(f"Loaded {len(dfs)} CSV files into one DataFrame with {len(big_df)} rows")




# df = pd.read_csv("data_set_1.csv", skiprows=5)
#df = pd.read_csv("/home/zyster/Documents/coding/data/data_set_1.csv", skiprows=6)
# Optional: Strip any whitespace from column names
df.columns = df.columns.str.strip()

# Extract the desired columns into variables
# time_left = df['time left']
# weight_left = df['weight left']
# time_right = df['time right']
# weight_right = df['weight right']



# plt.figure(figsize=(10, 6))

# plt.plot(time_left, weight_left, label='Left Side', color='blue')
# plt.plot(time_right, weight_right, label='Right Side', color='green')

# plt.title("Force Over Time: Left vs Right")
# plt.xlabel("Time (s)")
# plt.ylabel("Weight (kg)")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()