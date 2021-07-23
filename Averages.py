import pandas as pd

data = pd.read_csv("C:\\Users\\kwira\\OneDrive\\Documents\\GitHub\\Quartz-Irradiations-Code\\2.csv")
data =data.set_index('wavelength')
print(data)
wavelength = data.index.tolist()

framenum = -1
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
            framenum[nameid] = columnData
            # colname = namelist[nameid]
            # dfname = namelist[nameid]
            # dfname[colname] = columnData
        else:
            framenum = framenum + 1
            dfname = framenum
            # dfname = pd.concat(data[columnName], axis=1, keys=nameid)
            dfname = data[[columnName]].copy()
            dflist.append(dfname)
            # dfempty = pd.DataFrame(index=wavelength, columns='test')
            # dfempty = df_.fillna(0)
            # namedone.append(namelist[nameid])
            # dfname = namelist[nameid]
            # exec("%s = %d" % (dfname, dfempty))
            # dfname[fullname[nameid]] = columnData
            # dflist.append(dfname)
        nameid = nameid + 1

print(dflist)

# for frame in dflist:
#     frame['mean'] = frame.apply(np.mean, axis=1)