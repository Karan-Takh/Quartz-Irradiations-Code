import pandas as pd

# Create function to remove commas from data values in csv file and create dataframes for the absorbance and transmittance values separately.  
def comma_remover(sheet):
    # read the inputted data sheet into a pandas dataframe
    sheetdf = pd.read_csv(sheet+'.csv')
    # create a list of the column names and remove all the commas in the data values in the first column. --- the list may actually not be necessary.
    cols = list(sheetdf.columns)
    sheetdf[cols[0]] = sheetdf[cols[0]].str.replace(',', '')
    # sheetdf = sheetdf.set_index(cols[0])

    # Create two new dataframes, one for absorbance and one for transmittance. Set the index as the first column, wavelength, for both.
    # Absorbance should always be the second column
    abs_df = sheetdf.iloc[:, 0:2]
    # Transmittance will always be the third column. 
    trans_df = sheetdf.iloc[:, 1:3]
    return abs_df, trans_df


y = input(
    'Enter the name of the data sheet you want to convert. Must be .csv. Please omit file ending (ie, do no type .csv): ')

# Call comma remover function to remove the commas from the first column of the file. 
pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(comma_remover(y)[0])




# Find NaN rows and shift data accordingly. 
nan_rows = list()
col_names = list()

def data_shift(df_tuple):
    # Loop through each dataframe d, absorbance and transmittance
    for d in df_tuple:
        # Loop through every index. 
        index_list = d.index.tolist()
        for index in index_list:
            # Check if NaN value exists in the wavelength column (0th column) at each index. This will indicate a line break. 
            if d[0][index].isnull():
                nan_rows.append(index)
        # After the loop, get rid of every other item in the list of indices. This is because I just want the index of the first NaN of the NaN pairs. 
        nan_rows = nan_rows[0::2]
        # Loop through numbers in nan_rows, which are the indices of the rows with NaNs, and add three to get the batch name (hopefully this works every time)
        for item in nan_rows:
            col_names.append(d[0][item+3])
        # Not sure if -1 is necessary. 
        for i in range(len(nan_rows)-1):
            # Create new column, named i, which will be the number of new columns. Can just delete those later. 
            # nan_rows + 2 because you want to start from the second of the pair of NaNs. 
            d[i] = d.iloc[nan_rows[i]+4:nan_rows[i+2], 1]
    return df_tuple




# Print the first dataframe in the tuple of dataframes created by the data shift function. 
print(data_shift(comma_remover(y))[0])




# 210427 Sample 6 Raw Data