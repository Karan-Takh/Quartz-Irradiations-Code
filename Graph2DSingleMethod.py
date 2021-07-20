import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#######################################################
file = input('Enter the csv file with .csv: ')
name = input('Enter the desired name of the graph: ')
#######################################################

#################### Converts csv to dataframe ####################
#######################################################
data = pd.read_csv(file)
#######################################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data = pd.read_csv("C:\\Users\\kwira\\Downloads\\one holder b marker vs no marker.csv")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

#################### Adds wavelength values to list for graphing ####################
wavelength = data["wavelength"].tolist()

#################### Creates graph ####################
fig, ax = plt.subplots()


#################### Creates dictionary of colors in html format ####################
color = ['#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
         '#FF0066', '#993300', '#FF3300', '#660033']

#################### Function for graphing all lines in their respective colors ####################
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
        ax.plot(wavelength, y, label=f"{columnName}", color=f"{color[colornum]}", linewidth=2)
        minimum.append(min(y))
        maximum.append(max(y))
        colornum = colornum + 1  # Changes the color to new color when there is a new batch
        scan = scan + 1

truemin = int(min(minimum)) - 10
truemax = int(max(maximum)) + 10

#################### Adds labels to graph ####################
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# plt.title('2 cm Sample in One Holder with Marker to Maintain Position')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#######################################################
plt.title(name)
#######################################################
plt.xlabel("Wavelength (nm)")
plt.ylabel("Percent Transmission (%)")

#################### Sets size of figure ####################
plt.ylim(truemin,truemax)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.tight_layout()

#################### Sets the tick mark intervals ####################
plt.xticks(np.arange(100, 1100+1, 100))

plt.show()