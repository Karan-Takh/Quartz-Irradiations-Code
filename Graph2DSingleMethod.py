import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:\\Users\\kdee2\\Documents\\GitHub\\Quartz-Irradiations-Code\\One Holder 1 vs 2.csv")
wavelength = data["wavelength"].tolist()

fig, ax = plt.subplots()


# Creates dictionary of colors in html format
color = ['#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
         '#FF0066', '#993300', '#FF3300', '#660033']

# Function for graphing all lines in their respective colors
colornum = 0
minimum = []
maximum = []
scan = 1

for (columnName, columnData) in data.iteritems():
    if columnName == 'wavelength':
        continue
    else:
        y = data[f"{columnName}"].tolist()
        scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
        ax.plot(wavelength, y, label=f"{columnName}", color=f"{color[colornum]}", linewidth=0.5)
        minimum.append(min(y))
        maximum.append(max(y))
        colornum = colornum + 1  # Changes the color to new color when there is a new batch
        scan = scan + 1

truemin = int(min(minimum)) - 10
truemax = int(max(maximum)) + 10

#Adds labels to graph
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Both Holders 2')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Percent Transmission (%)")

#Sets size of figure
plt.ylim(truemin,truemax)
# fig = plt.gcf()
# fig.set_size_inches(9, 6)

# Sets the tick mark intervals
plt.xticks(np.arange(100, 1100+1, 100))

plt.show()