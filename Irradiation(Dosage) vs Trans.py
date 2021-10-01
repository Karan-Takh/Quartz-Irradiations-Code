
import pandas as pd
import matplotlib.pyplot as plt


x = input("Input csv file name (omit .csv): ")
df = pd.read_csv(x + ".csv")

#print(df.head())

w = int(input("Input wavelength: "))


transmittances = df.iloc[w-189].tolist()
transmittances = transmittances[3:]

print(transmittances)


columns = df.iloc[0].tolist()
columns = columns[3:]

print(columns)


plt.plot(columns, transmittances, 'o', color='k', label= w )
plt.xlabel('Dosage (pulses)')
plt.ylabel('%T')
#plt.title("Percent Transmittance vs Dosage at one wavelength", loc="left", fontsize = "10")
plt.legend()
plt.show()
