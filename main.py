import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
import numpy as np
from datetime import datetime

from engine import DieselEngine
from fuelcell import Fuelcell
from preprocess_data import import_data
from ships import get_unique_engine_models


#import data from Bunker delivery notes
file_path = r'C:\Uni\Master\Master Thesis\Data\BDN\VPM Data_Maharaj_2022_Q3.xlsx'
data = import_data(file_path)

#import data from Clarkson database
engine_path = r'C:\Uni\Master\Master Thesis\Data\Clarkson Data\Data_LOA300.xlsx'
unique_value = 'Main Engine Model'
unique_engines = get_unique_engine_models(engine_path, unique_value)

#Initialise Diesel 2-stroke characteristics

ratedpower = 16590000   #Maximum continous rated power of a 6G70ME-C9.2 engine (in W)
nengines= 1             #Amount of engines in the system
max_rpm = 97            #Maximum continuous rated rounds per minute (in RPM)


Diesel = DieselEngine(ratedpower,1, max_rpm)

# Initialise a value for the Base SFOC of 6G70ME-C9.2 engine dependant on engine load
def SFOCbase(engine_load):
    if 0 <= engine_load < 0.25:
        return 175.66
    elif 0.25 <= engine_load < 0.5:
        return 165.34
    elif 0.5 <= engine_load < 0.7:
        return 164.89
    elif 0.7 <= engine_load < 0.75:
        return 167.31
    elif 0.75 <= engine_load <= 1.0:
        return 171.75
    else:
        raise ValueError("Input value must be between 0 and 1.")
    
#Initialise Fuel Cell characteristics



#Define emission indexes to evaluate performance
#Energy Efficiency Design Index (EEDI)
#EEDI = (P_total * sfc * C_f) / (DWT * V_d)

#Energy Efficiency Existing Ship Index (EEXI)
#EEXI = EEDI

#Calculate the SFOC based on the Total power req from BDN
results = []

# Iterate through each row in the dataset
for index, row in data.iterrows():
    current_time = row['DateTimeStamp']
    power_req = row['DG_PWR_TOTAL'] * 1000  # Convert power requirement to watts

    # Calculate engine load
    engine_load = power_req / (nengines * ratedpower)

    # Calculate relative and absolute SFOC
    SFOC_rel = Diesel.fuel_efficiency(engine_load)
    SFOC_abs = SFOC_rel * SFOCbase(engine_load)

    # Append results
    results.append({
        'Time': current_time,
        'OptimizedValue': SFOC_abs
    })

results_df = pd.DataFrame(results)

plt.plot(results_df['Time'], results_df['OptimizedValue'], label='Optimized Output')
plt.xlabel('Time')
plt.ylabel('Relative Specific Fuel Consumption')
plt.title('Relative Specific Fuel Consumption over time')
plt.legend()
plt.show()

print('Unique engine models :', unique_engines)