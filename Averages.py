import pandas as pd

data = pd.read_csv("C:\\Users\\kwira\\OneDrive\\Documents\\GitHub\\Quartz-Irradiations-Code\\2.csv")
data =data.set_index('wavelength')
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

print(namelist)
print(fullname)

nameid = 0

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