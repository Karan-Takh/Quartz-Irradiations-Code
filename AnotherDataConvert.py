import pandas as pd

# Create function to remove commas from data values in csv file and create dataframes for the absorbance and transmittance values separately.  
def comma_remover(sheet):
    # read the inputted data sheet into a pandas dataframe
    sheetdf = pd.read_csv(sheet+'.csv')
    # create a list of the column names and remove all the commas in the data values in the first column. --- the list may actually not be necessary.
    cols = list(sheetdf.columns)
    sheetdf[cols[0]] = sheetdf[cols[0]].str.replace(',', '')
    sheetdf = sheetdf.set_index(cols[0])
    # Create two new dataframes, one for absorbance and one for transmittance. Set the index as the first column, wavelength, for both.
    # Absorbance should always be the second column
    data = sheetdf[cols[1]]
    print("Data is \n", data)
    abs_df = sheetdf.iloc[:, 0]
    # abs_df = pd.DataFrame(data=data, index=sheetdf[cols[0]])
    # Transmittance will always be the third column. 
    # trans_df = pd.DataFrame(index=sheetdf[cols[0]], columns=sheetdf)
    return abs_df, # trans_df


y = input(
    'Enter the name of the data sheet you want to convert. Must be .csv. Please omit file ending (ie, do no type .csv): ')

# Call comma remover function to remove the commas from the first column of the file. 
print(comma_remover(y))












# 210427 Sample 6 Raw Data