from numpy import NaN, add
import pandas as pd

# Create function to remove commas from data values in csv file and create dataframes for the absorbance and transmittance values separately.  
def comma_remover(sheet):
    # read the inputted data sheet into a pandas dataframe. Header = int to make the headers integer values 0, 1, 2, 3 ... 
    sheetdf = pd.read_csv(sheet+'.csv', header=None)
    # create a list of the column names and remove all the commas in the data values in the first column. --- the list may actually not be necessary.
    sheetdf[0] = sheetdf[0].str.replace(',', '')

    # Create two new dataframes, one for absorbance and one for transmittance. Set the index as the first column, wavelength, for both.
    # Absorbance should always be the second column
    abs_df = sheetdf.iloc[:, 0:2]
    # Transmittance will always be the third column. 
    trans_df = sheetdf.drop(columns=[1], axis=1)
    trans_df.rename(columns = {2: 1}, inplace=True)
    # print(trans_df.head())
    return abs_df, trans_df


# y = input(
    # 'Enter the name of the data sheet you want to convert. Must be .csv. Please omit file ending (ie, do no type .csv): ')

# Call comma remover function to remove the commas from the first column of the file. 
pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(comma_remover(y)[0])




# Find NaN rows and shift data accordingly. 



def data_shift(df_tuple: tuple):
    dfs_list = list()
    # Loop through each dataframe d, absorbance and transmittance
    # print(df_tuple)
    for d in df_tuple:
        col_names = list()
        # Loop through every index. 
        # index_list = d.index.tolist()
        nan_rows = d[d[0].isnull()].index.tolist()
        # print("Og nanrows is", nan_rows)
        # print(len(nan_rows))
        # After the loop, get rid of every other item in the list of indices. This is because I just want the index of the first NaN of the NaN pairs. 
        nan_rows = nan_rows[0::2]
        # print(len(nan_rows))
        # print("Nanrows after removing every other is", nan_rows)
        # Loop through numbers in nan_rows, which are the indices of the rows with NaNs, and add three to get the batch name (hopefully this works every time)
        for item in nan_rows:
            col_names.append(d[0][item+3]) 
        # print("First sliced column is \n", d.iloc[nan_rows[0]+4:nan_rows[1], 1].tolist())
        for i in range(len(nan_rows)-1):
            # Create new column, named i, which will be the number of new columns. Can just delete those later. 
            # nan_rows + 2 because you want to start from the second of the pair of NaNs. 
            # Convert sliced column from series to a list. 
            additional = pd.DataFrame({
                i+2 : d.iloc[nan_rows[i]+4:nan_rows[i+1], 1].tolist()
                })
            # original = d
            d = pd.concat([d, additional], axis=1)
        # Drop the first row, which has no useful values. 
        d.drop(index=0, inplace=True)

        d[0] = d[0].drop(labels=[1,2])
        d.drop(d.iloc[1][0])
        # d.drop(d.index[d[0] == 'NaN'], inplace=True)
        d[1] = d[1].drop(labels=[1,2])
        # for c in d.columns.tolist():
          #  d[c] = d[c].dropna()
        dfs_list.append(d)
    return dfs_list


y = '210427 Sample 6 Raw Data'
# Print the first dataframe in the tuple of dataframes created by the data shift function. 
# data_shift(comma_remover(y))



# --------- Finishing touches ----------
absorbance = data_shift(comma_remover(y))[0]
transmittance = data_shift(comma_remover(y))[1]

# print(absorbance.head())
# Make lists of absorbance and transmittance lists
abs_col_list = absorbance.columns.tolist()
tra_col_list = transmittance.columns.tolist()



""" toremove = ["NaN"]


for c in abs_col_list:
    # Define empty list for every iteration through the column names. 
    filtered_list = []
    # Iterate through each value in each column. Must change column from series to list to accomplish this. 
    for e in absorbance[c].tolist():
        # Check if e is not in the list of values to remove for the absorbance dataframe. If it isn't, append it to the filtered list. 
        if e not in toremove:
            filtered_list.append(e)
    # Replace the c column with filtered list, which will have the values without the unwanted stuff.
    absorbance[c] = filtered_list

for c in tra_col_list:
    # Define empty list for every iteration through the column names. 
    filtered_list = []
    # Iterate through each value in each column. Must change column from series to list to accomplish this. 
    for e in transmittance[c].tolist():
        # Check if e is not in the list of values to remove for the transmittance dataframe. If it isn't, append it to the filtered list. 
        if e not in toremove:
            filtered_list.append(e)
    # Replace the c column with filtered list, which will have the values without the unwanted stuff.
    transmittance[c] = filtered_list
            
  """

""" absorbance[c].tolist().remove("NaN")
        absorbance[c].tolist().remove("Abs")
 """

""" for c in tra_col_list:
    transmittance[c].tolist().remove("NaN")
    transmittance[c].tolist().remove("%T")
    # transmittance[c] = 
     """
print(absorbance.head())




""" for data in data_shift(comma_remover(y)):
    data.drop(index=[0,1,2], columns=[0,1])
    print(data.head()) 
 """




# 210427 Sample 6 Raw Data