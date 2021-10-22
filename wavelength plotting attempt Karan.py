'''Created 9/24/21

Koeth Group'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ask user to input the file name, without .csv
x = input("Input csv file name (omit .csv): ")
df = pd.read_csv(x + ".csv")

print(df.head())
w = int(input("Input wavelength: "))


transmittances = df.iloc[w-190].tolist()
transmittances = transmittances[2:]

# print(transmittances)


columns = df.columns.tolist()
columns = columns[2:]




# Make the array of the pulses (this will vary by experiment. For sample 9, it was 20,000 pulses each time)
pulses = [20000, 40000, 60000, 80000, 100000, 120000, 140000, 
        160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000]



# Make the figure
fig, ax = plt.subplots()
ax.set_xlabel('Irradiation Number and Total Pulses')
plt.xticks(rotation=70)
ax.set_ylabel('Transmittance')
ax.plot(columns, transmittances, 'o', color='g')

# Add second axis
# axes1 = plt.gca()
# axes2 = axes1.twiny()
# axes2.set_xticks([pulses]) # not sure if need brackets
# axes2.set_xlabel("Pulses")


plt.show()