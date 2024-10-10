import pandas as pd
import numpy as np
import os

# Read the Excel file
def get_ship_names_diesel_engine(file_path, attribute, value):
    """
    Extract ship names from an Excel file based on a specific attribute.

    Parameters:
        file_path (str): Path to the Excel file.
        attribute (str): The column name representing the attribute.
        value: The value of the attribute to filter by.

    Returns:
        list: A list of ship names that match the specified attribute condition.
    """
    # Load excel file into the dataframe
    df = pd.read_excel(file_path, sheet_name='Listing')

    #filter the dataframe on specific attribute
    diesel_ships = df[df[attribute] == value]

    diesel_ship_names= diesel_ships['Name'].tolist()

    return diesel_ship_names

