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
print(comma_remover(y)[0])




# Find NaN rows and shift data accordingly. 
nan_rows = list()
# Loop through each dataframe d, absorbance and transmittance
for d in comma_remover(y):
    for index, row in d.iterrows():
        is_nan_series = row.isnull()
        if is_nan_series.any():
            nan_rows.append(index)
    # Loop through numbers in nan_rows, which are the indices of the rows with 
    for item in nan_rows:
        








# 210427 Sample 6 Raw Data