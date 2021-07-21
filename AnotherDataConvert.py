import pandas as pd
from Graph3D import plot_3d
from Graph2D import plot_2d

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



# Display total dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)


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
        col_names.append(d[0][1])
        for item in nan_rows:
            col_names.append(d[0][item+3]) 
        # print("First sliced column is \n", d.iloc[nan_rows[0]+4:nan_rows[1], 1].tolist())
        for i in range(len(nan_rows)):
            # Create new column, named i, which will be the number of new columns. Can just delete those later. 
            # nan_rows + 2 because you want to start from the second of the pair of NaNs. 
            # Convert sliced column from series to a list. 
            if nan_rows[i] != nan_rows[-1]:
                additional = pd.DataFrame({
                    i+2 : d.iloc[nan_rows[i]+4:nan_rows[i+1], 1].tolist()
                    })
            # If this is the last iteration of the for loop, go from the last item in nan-rows 
            else:
                additional = pd.DataFrame({
                    i+2: d.iloc[nan_rows[i]+4:, 1].tolist()
                })
            # Add the additional column to the dataframe. 
            d = pd.concat([d, additional], axis=1)
        # Drop the first three labels of the first 2 columns, and then shift the columns up by 2 rows.
        d[0] = d[0].drop(labels=[0, 1])
        d[0] = d[0].shift(-2)
        d[1] = d[1].drop(labels=[0, 1])
        d[1] = d[1].shift(-2)
        # Remove all of the dataframe after the first iteration of the 190-1100nm range after the data is shifted. 
        d = d.iloc[:nan_rows[0]]
        # Remove rows with missing values. 
        d = d.dropna()
        # Drop the first row, which has no useful values. 
        d.drop(index=0, inplace=True)
        # Rename first column as wavelength.
        d = d.rename(columns={0 : "wavelength"})
        # Set index as wavelength column.
        d = d.set_index("wavelength")
        # Set the column names stored in the col name list
        d.columns = col_names
        dfs_list.append(d)
    return dfs_list


# Get inputs for file to be opened and the names of the new absorbance and transmittance files. 
y = input(
     'Enter the name of the data sheet you want to convert. Must be .csv. Please omit file ending (ie, do no type .csv): ')

x = input('Name of new absorbance file: ')
z = input('Name of new transmittance file: ')

abs_title = input("Title of absorbance plot: ")
tra_title = input("Title of transmittance plot: ")

# --------- Finishing touches ----------
# Name the absorbance and transmittance dataframes accordingly
absorbance = data_shift(comma_remover(y))[0]
transmittance = data_shift(comma_remover(y))[1]


print(absorbance.head())

absorbance.to_csv(path_or_buf = x + ".csv")
transmittance.to_csv(path_or_buf = z + ".csv")

# Calling the functions from other scripts to plot the data in 2D or 3D. 
def plotting():
    plot_type = input("Would you like to plot in 2D or 3D? Input '2D', '3D' or 'Both': ")
    if plot_type == '2D':
        plot_2d(absorbance, 'Absorbance (AU)', abs_title)
        plot_2d(transmittance, 'Transmittance (%)', tra_title)
    elif plot_type == '3D':
        plot_3d(absorbance, 'Absorbance (AU)', abs_title)
        plot_3d(transmittance, 'Transmittance (%)', tra_title)
    elif plot_type == 'Both':
        plot_2d(absorbance, 'Absorbance (AU)', abs_title)
        plot_2d(transmittance, 'Transmittance (%)', tra_title)
        plot_3d(absorbance, 'Absorbance (AU)', abs_title)
        plot_3d(transmittance, 'Transmittance (%)', tra_title)
    else:
        print('Please input valid plot type.')
        plotting()

plotting()

# C:\Users\kdee2\Documents\GitHub\Quartz-Irradiations-Code\Sample 6 Raw Data.csv1