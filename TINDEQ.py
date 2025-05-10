import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import pandas as pd
import csv


# Load the CSV file
# df = pd.read_csv('/home/zyster/Documents/coding/data/data_set_1.csv')


# df = pd.read_csv("data_set_1.csv", skiprows=5)
df = pd.read_csv("/home/zyster/Documents/coding/data/data_set_1.csv", skiprows=6)
# Optional: Strip any whitespace from column names
df.columns = df.columns.str.strip()

# Extract the desired columns into variables
time_left = df['time left']
weight_left = df['weight left']
time_right = df['time right']
weight_right = df['weight right']



plt.figure(figsize=(10, 6))

plt.plot(time_left, weight_left, label='Left Side', color='blue')
plt.plot(time_right, weight_right, label='Right Side', color='green')

plt.title("Force Over Time: Left vs Right")
plt.xlabel("Time (s)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()