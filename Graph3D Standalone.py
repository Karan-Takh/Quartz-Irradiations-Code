import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np

#######################################################
# file = input('Enter the csv file with .csv: ')
# name = input('Enter the desired name of the graph: ')
#######################################################

#################### Converts csv to dataframe ####################
#######################################################
# data = pd.read_csv(file)
#######################################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data = pd.read_csv("C:\\Users\\kwira\\OneDrive\\Documents\\GitHub\\Quartz-Irradiations-Code\\S8 Day 1 Transmittance.csv")
data = pd.read_csv("C:\\Users\\kwira\\Downloads\\S8 Day 1 Transmittance.csv")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

#################### Adds wavelength values to list for graphing ####################
wavelength = data["wavelength"].tolist()

#################### Makes plot 3D ####################
ax = plt.axes(projection='3d')

#################### Creates dictionary of colors in html format ####################
color = ['#00FFFF', '#FF61B0', '#FF6600', '#006600', '#FFCC00', '#666699', '#FF0000', '#9900CC', '#66FF33', '#009999',
         '#FF0066', '#993300', '#FF3300', '#660033', '#999966', '#4472C4', '#800000', '#7030A0', '#CC3300', '#CCCC00',
         '#993333']

#################### Function for graphing all lines in their respective colors ####################
colornum = -1
scan = 1
minimum = []
maximum = []
namelist = []
namedone = []
nameid = 0


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
    elif columnName == 'blank':
        continue
    else:
        name = list(columnName)
        name = name[:-2]
        namelist.append(convert(name))

nameid = 0

for (columnName, columnData) in data.iteritems():
    if columnName == 'wavelength':
        continue
    elif columnName == 'standard':
        y = data[f"{columnName}"].tolist()
        scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)  # Makes array full of same scan number
        ax.plot3D(scanlist, wavelength, y, label=f"{columnName}", color='black')
        minimum.append(min(y))
        maximum.append(max(y))
    elif columnName == 'blank':
        y = data[f"{columnName}"].tolist()
        scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)  # Makes array full of same scan number
        ax.plot3D(scanlist, wavelength, y, label=f"{columnName}", color='#C00000')
        minimum.append(min(y))
        maximum.append(max(y))
    else:
        if namelist[nameid] in namedone:
            y = data[f"{columnName}"].tolist()
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            ax.plot3D(scanlist, wavelength, y, color=f"{color[colornum]}")
            minimum.append(min(y))
            maximum.append(max(y))
            scan = scan + 1
        else:
            colornum = colornum + 1  # Changes the color to new color when there is a new batch
            namedone.append(namelist[nameid])
            y = data[f"{columnName}"].tolist()
            scanlist = np.full(shape=len(wavelength), fill_value=scan, dtype=int)
            ax.plot3D(scanlist, wavelength, y, label=f"{namelist[nameid]}", color=f"{color[colornum]}")
            minimum.append(min(y))
            maximum.append(max(y))
            scan = scan + 1
        nameid = nameid + 1

newmin = int(min(minimum)) - 1
newmax = int(max(maximum)) + 1
print(newmin)
print(newmax)
print(len(list(range(0, scan + 1))))

#################### Adds labels to graph ####################
plt.legend(bbox_to_anchor=(1.1, 0.8), loc='upper left', ncol=2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
plt.title('Sample 8 Day 1 Transmittance vs Wavelength')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#######################################################
# plt.title(name)
#######################################################
ax.set_xlabel("Scan Number", size=15)
ax.set_ylabel("Wavelength (nm)", size=15)
ax.set_zlabel("Percent Transmission (%)", size=15)

#################### Sets size of figure ####################
ax.set_xlim(0, scan)
ax.set_ylim(-1, 71) #
ax.set_zlim(-2, 100) #
plt.tight_layout()
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
ax.view_init(elev=10., azim=-40) #

#################### Sets the tick mark intervals ####################
plt.autoscale(False)
plt.yticks(np.arange(100, 1100 + 1, 100))
ax.set_zticks(np.arange(newmin, newmax + 1, 10))

# Makes z axis longer than x and y axes for better visibility
ax.zaxis.set_tick_params(labelsize=1)
for t in ax.zaxis.get_major_ticks(): t.label.set_fontsize(10)

x_scale = 4
y_scale = 4.5
z_scale = 4

scale = np.diag([x_scale, y_scale, z_scale, 1.0])
scale = scale * (1.0 / scale.max())
scale[3, 3] = 1.0


def short_proj():
    return np.dot(Axes3D.get_proj(ax), scale)


ax.get_proj = short_proj

#################### Creates rectangular prism to show the PMT sensitive region ####################
# zpmt = list(range(newmin, newmax))
zpmt = list(range(-1, 101))
# xpmt = [0] * len(range(newmin, newmax))
xpmt = [0] * len(range(-1, 101))
# ypmt = np.full(shape=len(list(range(newmin, newmax))), fill_value=200, dtype=int)
ypmt = np.full(shape=len(list(range(-1, 101))), fill_value=200, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = list(range(newmin, newmax))
zpmt = list(range(-1, 101))
# xpmt = [scan] * len(range(newmin, newmax))
xpmt = [71] * len(range(-1, 101))
# ypmt = np.full(shape=len(list(range(newmin, newmax))), fill_value=200, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = list(range(newmin, newmax))
zpmt = list(range(-1, 101))
# xpmt = [0] * len(range(newmin, newmax))
xpmt = [0] * len(range(-1, 101))
# ypmt = np.full(shape=len(list(range(newmin, newmax))), fill_value=600, dtype=int)
ypmt = np.full(shape=len(list(range(-1, 101))), fill_value=600, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = list(range(newmin, newmax))
zpmt = list(range(-1, 101))
# xpmt = [scan] * len(range(newmin, 101))
xpmt = [71] * len(range(-1, 101))
# ypmt = np.full(shape=len(list(range(newmin, newmax))), fill_value=600, dtype=int)
ypmt = np.full(shape=len(list(range(-1, 101))), fill_value=600, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = [newmin] * len(range(0, scan + 1))
zpmt = [-1] * len(range(0, 71 + 1))
# xpmt = list(range(0, scan + 1))
xpmt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
# ypmt = np.full(shape=len(list(range(0, scan + 1))), fill_value=600, dtype=int)
ypmt = np.full(shape=len(list(range(0, 71 + 1))), fill_value=600, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = [newmin] * len(range(0, scan + 1))
zpmt = [-1] * len(range(0, 71 + 1))
# xpmt = list(range(0, scan + 1))
xpmt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
# ypmt = np.full(shape=len(list(range(0, scan + 1))), fill_value=200, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = [newmax] * len(range(0, scan + 1))
zpmt = [101] * len(range(0, 71 + 1))
# xpmt = list(range(0, scan + 1))
xpmt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
# ypmt = np.full(shape=len(list(range(0, scan + 1))), fill_value=200, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = [newmax] * len(range(0, scan + 1))
zpmt = [101] * len(range(0, 71 + 1))
# xpmt = list(range(0, scan + 1))
xpmt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
# ypmt = np.full(shape=len(list(range(0, scan + 1))), fill_value=600, dtype=int)
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = np.full(shape=len(list(range(200, 600))), fill_value=newmin, dtype=int)
zpmt = np.full(shape=len(list(range(200, 600))), fill_value=-1, dtype=int)
# xpmt = [scan] * len(range(200, 600))
xpmt = [71] * 400
ypmt = list(range(200, 600))
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = np.full(shape=len(list(range(200, 600))), fill_value=newmax, dtype=int)
zpmt = np.full(shape=len(list(range(200, 600))), fill_value=101, dtype=int)
# xpmt = [scan] * len(range(200, 600))
xpmt = [71] * len(range(200, 600))
ypmt = list(range(200, 600))
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = np.full(shape=len(list(range(200, 600))), fill_value=newmin, dtype=int)
zpmt = np.full(shape=len(list(range(200, 600))), fill_value=-1, dtype=int)
xpmt = [0] * len(range(200, 600))
ypmt = list(range(200, 600))
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

# zpmt = np.full(shape=len(list(range(200, 600))), fill_value=newmax, dtype=int)
zpmt = np.full(shape=len(list(range(200, 600))), fill_value=101, dtype=int)
xpmt = [0] * len(range(200, 600))
ypmt = list(range(200, 600))
ax.plot3D(xpmt, ypmt, zpmt, color='b', linewidth=3)

plt.show()
