'''Created 9/24/21

Koeth Group'''

import pandas as pd
import matplotlib.pyplot as plt

# Ask user to input the file name, without .csv
x = input("Input csv file name (omit .csv): ")
df = pd.read_csv(x + ".csv")

print(df.head())

w = int(input("Input wavelength: "))


transmittances = df.iloc[w-190].tolist()
transmittances = transmittances[2:]

print(transmittances)


columns = df.columns.tolist()
columns = columns[2:]

print(columns)


plt.plot(columns, transmittances, 'o', color='g')
plt.show()