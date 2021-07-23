import pandas as pd
from pandas.core.frame import DataFrame
import numbers

data = pd.read_csv("C:\\Users\kdee2\Documents\GitHub\Quartz-Irradiations-Code\\2.csv")
data = data.set_index('wavelength')
print(data)
wavelength = data.index.tolist()

scan = 1
minimum = []
maximum = []
namelist = []
namedone = []
fullname = []
dflist = []
nameid = 0

pd.set_option("display.max_rows", None, "display.max_columns", None)


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
        newname = name[:-2]
        fullname.append(convert(name))
        namelist.append(convert(newname))

namelist.insert(0, 'blank')
print(namelist)
# print(fullname)

# Creating a new dataframe using namelist as the columns
samename_df = data.set_axis(namelist, axis=1)

# Using groupby function to average the columns with the same names
# From https://stackoverflow.com/questions/40311987/pandas-mean-of-columns-with-the-same-names
averaged_df = samename_df.groupby(by=samename_df.columns, axis=1).mean()

# Another way of doing it apparently: 
# averaged_df = samename_df.groupby(by=samename_df.columns, axis=1).apply(lambda g: g.mean(axis=1) if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[:,0])


print(averaged_df.head())





""" nameid = 0

for (columnName, columnData) in data.iteritems():
    if columnName == 'wavelength':
        continue
    elif columnName == 'standard':
        continue
    elif columnName == 'blank':
        continue
    else:
        if namelist[nameid] in namedone:
            dfname = namelist[nameid]
            dfname[f"{fullname[nameid]}"] = columnData
        else:
            namedone.append(namelist[nameid])
            dfname = namelist[nameid]
            dfname[f"{fullname[nameid]}"] = columnData
            dflist.append(dfname)
        nameid = nameid + 1
 """
