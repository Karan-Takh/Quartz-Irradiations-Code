import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_2dAvg(file, y_label, title, y_limit):
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
    color = ['#009900', '#003399', '#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
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

    for (columnName, columnData) in data.iteritems():
        if columnName == 'wavelength':
            continue
        if columnName == 'standard':
            continue
        if columnName == 'blank':
            continue
        else:
            namelist.append(columnName)

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
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int) # Makes array full of same scan number
            ax.plot(wavelength, y, label=f"{columnName}", color='#C00000')
            minimum.append(min(y))
            maximum.append(max(y))
        else:
            if namelist[nameid] in namedone:
                y = data[f"{columnName}"].tolist()
                scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
                ax.plot(wavelength, y, color=f"{color[colornum]}")
                minimum.append(min(y))
                maximum.append(max(y))
                scan = scan + 1
            else:
                colornum = colornum+1 # Changes the color to new color when there is a new batch
                namedone.append(namelist[nameid])
                y = data[f"{columnName}"].tolist()
                scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
                ax.plot(wavelength, y, label=f"{namelist[nameid]}", color=f"{color[colornum]}")
                minimum.append(min(y))
                maximum.append(max(y))
                scan = scan+1
            nameid = nameid + 1

    truemin = int(min(minimum))
    truemax = int(max(maximum))

    #################### Adds labels to graph ####################
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', prop={"size":11.5})
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # plt.title('Day 1 Sample 6 Measurements')
    # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #######################################################
    plt.title(title)
    #######################################################
    plt.xlabel("Wavelength (nm)")
    plt.ylabel(y_label)

    #################### Sets size of figure ####################
    plt.ylim(truemin,truemax)
    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.window.state("zoomed")

    #################### Sets the tick mark intervals ####################
    plt.xticks(np.arange(100, 1100+1, 100))

    #################### Creates lines to show PMT sensitive region ####################
    xpmt1 = np.full(shape=len(list(range(truemin,truemax+1))), fill_value=200, dtype=int)
    ypmt1 = range(truemin, y_limit+1)
    xpmt2 = np.full(shape=len(list(range(truemin,truemax+1))), fill_value=600, dtype=int)
    ypmt2 = range(truemin, y_limit+1)
    ax.plot(xpmt1, ypmt1, color='b', linewidth=2)
    ax.plot(xpmt2, ypmt2, color='b', linewidth=2)

    plt.show()