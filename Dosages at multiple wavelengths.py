#Graph of %T vs Dosage at up to four different wavelengths
# Use TransDosage
import pandas as pd
import matplotlib.pyplot as plt

x = input("Input csv file name (omit .csv): ")
df = pd.read_csv(x + ".csv")

y = int(input("How many wavelengths would you like to put on this graph? (Up to 5): "))

columns = df.iloc[0].tolist()
columns = columns[3:]

if y == 1:
        w = int(input("Input wavelength: "))
        transmittances = df.iloc[w - 189].tolist()
        transmittances = transmittances[3:]
        plt.plot(columns, transmittances, '-o', color='k', label=w)
else:
        print("")


if y == 2:
    w = int(input("Input wavelength: "))
    transmittances = df.iloc[w - 189].tolist()
    transmittances = transmittances[3:]
    u = int(input("Input wavelength: "))
    transmittance = df.iloc[u - 189].tolist()
    transmittance = transmittance[3:]
    plt.plot(columns, transmittances, '-o', color='k', label=w)
    plt.plot(columns, transmittance, '-o', color='b', label=u)
else:
    print("")

if y== 3:
    w = int(input("Input wavelength: "))
    transmittances = df.iloc[w - 189].tolist()
    transmittances = transmittances[3:]
    u = int(input("Input wavelength: "))
    transmittance = df.iloc[u - 189].tolist()
    transmittance = transmittance[3:]
    p = int(input("Input wavelength: "))
    transmittanc = df.iloc[p - 189].tolist()
    transmittanc = transmittanc[3:]
    plt.plot(columns, transmittances, '-o', color='k', label=w)
    plt.plot(columns, transmittance, '-o', color='b', label=u)
    plt.plot(columns, transmittanc, '-o', color='m', label=p)
else:
    print("")


if y==4:
    w = int(input("Input wavelength: "))
    transmittances = df.iloc[w - 189].tolist()
    transmittances = transmittances[3:]
    u = int(input("Input wavelength: "))
    transmittance = df.iloc[u - 189].tolist()
    transmittance = transmittance[3:]
    p = int(input("Input wavelength: "))
    transmittanc = df.iloc[p - 189].tolist()
    transmittanc = transmittanc[3:]
    s = int(input("Input wavelength: "))
    transmittan = df.iloc[s - 189].tolist()
    transmittan = transmittan[3:]
    plt.plot(columns, transmittances, '-o', color='k', label=w)
    plt.plot(columns, transmittance, '-o', color='b', label=u)
    plt.plot(columns, transmittanc, '-o', color='m', label=p)
    plt.plot(columns, transmittan, '-o', color='c', label=s)
else:
    print("")

if y==5:
    w = int(input("Input wavelength: "))
    transmittances = df.iloc[w - 189].tolist()
    transmittances = transmittances[3:]
    u = int(input("Input wavelength: "))
    transmittance = df.iloc[u - 189].tolist()
    transmittance = transmittance[3:]
    p = int(input("Input wavelength: "))
    transmittanc = df.iloc[p - 189].tolist()
    transmittanc = transmittanc[3:]
    s = int(input("Input wavelength: "))
    transmittan = df.iloc[s - 189].tolist()
    transmittan = transmittan[3:]
    t = int(input("Input wavelength: "))
    transmitta = df.iloc[t - 189].tolist()
    transmitta = transmitta[3:]
    plt.plot(columns, transmittances, '-o', color='k', label=w)
    plt.plot(columns, transmittance, '-o', color='b', label=u)
    plt.plot(columns, transmittanc, '-o', color='m', label=p)
    plt.plot(columns, transmittan, '-o', color='c', label=s)
    plt.plot(columns, transmitta, '-o', color='g', label=t)
else:
    print("")


plt.legend(title = 'Wavelength (nm):')
plt.xlabel('Dosage (pulses as arbitrary units)')
plt.ylabel('%T')
#plt.xscale('log')
plt.title("Percent Transmittance as a function of Dosage (arbitrary value)", loc="center", fontsize = "20")
plt.show()
