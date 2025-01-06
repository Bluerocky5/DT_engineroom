import os
import numpy as np
import pandas as pd


def import_data(file_path):
    """
    Imports and processes data from an Excel file.

    This function reads data from a specified Excel file, performs preprocessing
    such as stripping whitespace from column names, slicing rows and columns,
    and renaming specified columns. Additionally, it extracts the file name and
    assigns it as an attribute to the resulting DataFrame.

    Parameters:
    -----------
    file_path : str
        The path to the Excel file to import.

    Returns:
    --------
    pd.DataFrame
        A Pandas DataFrame containing the processed Bunker Delivery Notes Data
        - Only a small part is taken where there is engine activity (index 7846 to 13500)
    """
    # Read data from the specified Excel file and sheet
    data = pd.read_excel(file_path, sheet_name='Sheet1')

    # Strip leading and trailing whitespace from column names
    data.columns = data.columns.str.strip()

    # Slice the DataFrame for specified rows and columns
    data = data.loc[2:26490, :'SPEED_TRANSVERSE_TW_LOG']

    # Rename specific columns
    data = data.rename(columns={
        'Column1': 'Sampling_time', 
        'RPM DIFF': 'RPM_DIFF', 
        'MCR %': 'MCR_PERC'
    })

    #Convert time column to datetime
    data['DateTimeStamp'] = pd.to_datetime(data['DateTimeStamp'])

    # Extract the file name (without extension) and assign it as an attribute to the DataFrame
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    data.name = file_name

    return data




