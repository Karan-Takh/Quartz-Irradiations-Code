from numpy import add
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
    trans_df = sheetdf.iloc[:, 1:3]
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
        print("Og nanrows is", nan_rows)
        print(len(nan_rows))
        # After the loop, get rid of every other item in the list of indices. This is because I just want the index of the first NaN of the NaN pairs. 
        nan_rows = nan_rows[0::2]
        print(len(nan_rows))
        print("Nanrows after removing every other is", nan_rows)
        # Loop through numbers in nan_rows, which are the indices of the rows with NaNs, and add three to get the batch name (hopefully this works every time)
        for item in nan_rows:
            col_names.append(d[0][item+3]) 
        print("First sliced column is \n", d.iloc[nan_rows[0]+4:nan_rows[1], 1].tolist())
        for i in range(len(nan_rows)-1):
            # Create new column, named i, which will be the number of new columns. Can just delete those later. 
            # nan_rows + 2 because you want to start from the second of the pair of NaNs. 
            # Convert sliced column from series to a list. 
            additional = pd.DataFrame({
                i+2 : d.iloc[nan_rows[i]+4:nan_rows[i+1], 1].tolist()
                })
            original = d
            new = pd.concat([original, additional], axis=1)
            # Use head function to see how top of dataframe is looking. 
            print(new.head())
            dfs_list.append(new)
    return dfs_list


y = '210427 Sample 6 Raw Data'
# Print the first dataframe in the tuple of dataframes created by the data shift function. 
data_shift(comma_remover(y))




# 210427 Sample 6 Raw Data