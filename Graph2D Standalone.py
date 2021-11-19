import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Define the function. File name, y-axis label, plot title, and the maximum of the plot. For absorbance plots, this should be 3. For transmittance, it will be 100.
def plot_2d(file, y_label, title, truemax):
    plt.rcParams["font.family"] = "Times New Roman"

    #######################################################
    # file = input('Enter the csv file with .csv: ')
    # name = input('Enter the desired name of the graph: ')
    #######################################################

    #################### Converts csv to dataframe ####################
    #######################################################
    data = pd.read_csv(file)
    #######################################################
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # data = pd.read_csv("C:\\Users\\kwira\\OneDrive\\Documents\\GitHub\\Quartz-Irradiations-Code\\2.csv")
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #################### Adds wavelength values to list for graphing ####################
    wavelength = data["wavelength"].tolist()

    #################### Creates graph ####################
    fig, ax = plt.subplots()

    #################### Creates dictionary of colors in html format ####################
    color = ['#009900', '#00FFFF', '#003399', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
                 '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
                 '#993333']


    #################### Function for graphing all lines in their respective colors ####################
    colornum = -1
    scan = 1
    minimum = []
    maximum = []
    namelist = []
    namedone = []


    def convert(s):
        # initialization of string to ""
        new = ""
        # traverse in the string
        for x in s:
            new += x
            # return string
        return new


    for (columnName, columnData) in data.iteritems():
        if columnName == 'wavelength':
            continue
        if columnName == 'standard':
            continue
        if columnName == 'blank':
            continue
        else:
            name = list(columnName)
            # name = name[:-2]
            if name[-1] == ' ':
                name = name[:-1]
                namelist.append(convert(name))
            else:
                namelist.append(convert(name))
            # if name[3] == 'P':
            #     namelist.append(convert(name))
            # else:
            #     namelist.append('Irradiations')



    nameid = 0

    for (columnName, columnData) in data.iteritems():
        if columnName == 'wavelength':
            continue
        elif columnName == 'standard':
            y = data[f"{columnName}"].tolist()
            ax.plot(wavelength, y, label=f"{columnName}", color='black')
            minimum.append(min(y))
            maximum.append(max(y))
        elif columnName == 'blank':
            y = data[f"{columnName}"].tolist()
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)  # Makes array full of same scan number
            ax.plot(wavelength, y, label=f"{columnName}", color='#C00000')
            minimum.append(min(y))
            maximum.append(max(y))
        else:
            colornum = colornum + 1
            y = data[f"{columnName}"].tolist()
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            # ax.plot(wavelength, y, color=f"{color[colornum]}")
            ax.plot(wavelength, y, label=f"{namelist[nameid]}", color=f"{color[colornum]}")
            scan = scan + 1
            minimum.append(min(y))
            maximum.append(max(y))
            # if namelist[nameid] in namedone:
            #     y = data[f"{columnName}"].tolist()
            #     scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            #     ax.plot(wavelength, y, color=f"{color[colornum]}")
            #     minimum.append(min(y))
            #     maximum.append(max(y))
            #     scan = scan + 1
            # else:
            #     colornum = colornum + 1  # Changes the color to new color when there is a new batch
            #     namedone.append(namelist[nameid])
            #     y = data[f"{columnName}"].tolist()
            #     scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            #     ax.plot(wavelength, y, label=f"{namelist[nameid]}", color=f"{color[colornum]}")
            #     minimum.append(min(y))
            #     maximum.append(max(y))
            #     scan = scan + 1
            nameid = nameid + 1

    truemin = int(min(minimum))
    # truemax = int(max(maximum))
    # print(truemax)
    # print(truemin)
    # truemin = 0
    # truemax = 100

    #################### Adds labels to graph ####################
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', prop={"size":14})
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    plt.title(title, fontsize=18)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #######################################################
    # plt.title(title)
    #######################################################
    plt.xlabel("Wavelength (nm)", fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    #################### Sets size of figure ####################
    plt.ylim(truemin, truemax)
    plt.xlim(100, 1150)
    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    # mng.window.state("zoomed")

    #################### Sets the tick mark intervals ####################
    plt.xticks(np.arange(100, 1100 + 1, 100))

    #################### Creates lines to show PMT sensitive region ####################
    xpmt1 = np.full(shape=len(list(range(truemin, truemax+1))), fill_value=200, dtype=int)
    ypmt1 = range(truemin, truemax+1)
    xpmt2 = np.full(shape=len(list(range(truemin, truemax+1))), fill_value=600, dtype=int)
    ypmt2 = range(truemin, truemax+1)

    # xpmt1 = np.full(shape=len(list(range(truemin, truemax + 1))), fill_value=200, dtype=int)
    # ypmt1 = range(truemin, truemax + 1)
    # xpmt2 = np.full(shape=len(list(range(truemin, truemax + 1))), fill_value=600, dtype=int)
    # ypmt2 = range(truemin, truemax + 1)

    ax.plot(xpmt1, ypmt1, color='b', linewidth=2)
    ax.plot(xpmt2, ypmt2, color='b', linewidth=2)

    plt.show()

# plot_2d("C:\\Users\\kwira\\OneDrive\\Documents\\GitHub\\Quartz-Irradiations-Code\\S8 Averaged Absorbance.csv",
#         'Transmittance (%)', 'Sample 8 Day 1 - Wavelength vs Transmittance')



# plot_2d("S9 Avg Tra.csv", 'Transmittance (%)', 'Sample 9 Transmittance')
plot_2d("C:\\Users\\kdee2\\Documents\\GitHub\\Quartz-Irradiations-Code\\Avg Tra Quartz Block Fiber Tests.csv", 
        'Transmittance', 'Quartz Block Fiber Tests', 100)

