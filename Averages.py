import pandas as pd
from pandas.core.frame import DataFrame
import numbers
import matplotlib.pyplot as plt

# Make the parameter a list. This way can just call it once using the dfs_list from the other script. 
def averages(data: list):
    # data = pd.read_csv("C:\\Users\\kwira\\OneDrive\\Documents\\GitHub\\Quartz-Irradiations-Code\\2.csv")
    # data = data.set_index('wavelength')
    # print(data)
    # wavelength = data.index.tolist()
    averaged_dataframes = list()
    for d in data: 
        framenum = -1
        scan = 1
        minimum = []
        maximum = []
        namelist = []
        namedone = []
        fullname = []
        dflist = []
        nameid = 0

        # Make the values in the dataframes floats. 
        d = d.astype(float)
        pd.set_option("display.max_rows", None, "display.max_columns", None)


        def convert(s):
            # initialization of string to ""
            new = ""
            # traverse in the string
            for x in s:
                new += x
                # return string
            return new

        for (columnName, columnData) in d.iteritems():
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

        # namelist.insert(0, 'blank')
        # print("The list of new column names is", namelist)
        # print(fullname)

        # Creating a new dataframe using namelist as the columns
        samename_df = d.set_axis(namelist, axis=1)

        # Using groupby function to average the columns with the same names
        # From https://stackoverflow.com/questions/40311987/pandas-mean-of-columns-with-the-same-names
        averaged_df = samename_df.groupby(by=samename_df.columns, axis=1).mean()
        # Make sure to append this averaged dataframe to a list which can be returned from the function. 
        averaged_dataframes.append(averaged_df)
        # Another way of doing it apparently: 
        # averaged_df = samename_df.groupby(by=samename_df.columns, axis=1).apply(lambda g: g.mean(axis=1) if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[:,0])

    return averaged_dataframes



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
  """