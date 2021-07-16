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
# data = pd.read_csv("C:\\Users\\kwira\\Downloads\\Day_1.csv")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

#################### Adds wavelength values to list for graphing ####################
wavelength = data["wavelength"].tolist()

#################### Creates graph ####################
fig, ax = plt.subplots()

#################### Creates dictionary of colors in html format ####################
color = ['#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
         '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
         '#993333']

#################### Function for graphing all lines in their respective colors ####################
colornum = 0
minimum = []
maximum = []
scan = 1

for (columnName, columnData) in data.iteritems():
    if columnName == 'wavelength':
        continue
    elif columnName == 'standard':
        y = data[f"{columnName}"].tolist()
        ax.plot(wavelength, y, label=f"{columnName}", color='black', linewidth=0.5)
        minimum.append(min(y))
        maximum.append(max(y))
    else:
        if scan%4 == 0:
            y = data[f"{columnName}"].tolist()
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            ax.plot(wavelength, y, label=f"{columnName}", color=f"{color[colornum]}", linewidth=0.5)
            minimum.append(min(y))
            maximum.append(max(y))
            colornum = colornum+1 # Changes the color to new color when there is a new batch
            scan = scan+1
        else:
            y = data[f"{columnName}"].tolist()
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            ax.plot(wavelength, y, label=f"{columnName}", color=f"{color[colornum]}", linewidth=0.5)
            minimum.append(min(y))
            maximum.append(max(y))
            scan = scan + 1

truemin = int(min(minimum)) - 10
truemax = int(max(maximum)) + 10

#################### Adds labels to graph ####################
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', ncol=2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# plt.title('Both Holders 2')
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

#################### Creates lines to show PMT sensitive region ####################
xpmt1 = np.full(shape=len(list(range(truemin,truemax))), fill_value=200, dtype=int)
ypmt1 = range(truemin, truemax)
xpmt2 = np.full(shape=len(list(range(truemin,truemax))), fill_value=600, dtype=int)
ypmt2 = range(truemin, truemax)
ax.plot(xpmt1, ypmt1, color='b', linewidth=2)
ax.plot(xpmt2, ypmt2, color='b', linewidth=2)

plt.show()