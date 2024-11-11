from ships import get_ship_names_diesel_engine
from ships import get_unique_engine_models

#define path of the excel file
file_path = 'D:\School\Master\Master Thesis\Data\Data_10_10.xlsx'

#Define what needs to be extracted from the file
attribute = 'Power Type'
value = 'Steam Turbine'
unique_value = 'Main Engine Model'

#Call the function to get the ship names based on the attribute
diesel_ship_names = get_ship_names_diesel_engine(file_path, attribute, value)

print('Ships with diesel engine:' , diesel_ship_names)

#Call the function to get unique engine models
unique_models = get_unique_engine_models(file_path, unique_value)

print('Unique engine models :', unique_models)
