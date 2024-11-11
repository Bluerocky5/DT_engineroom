from engine import DieselEngine
from fuelcell import Fuelcell

#Initialise Diesel 2-stroke characteristics
ratedpower = 16000000   #Maximum continous rated power of a 6G60ME-C9.5 engine (in W)
nengines= 1             #Amount of engines in the system
max_rpm = 97            #Maximum continuous rated rounds per minute (in RPM)

#Initialise Fuel Cell characteristics



#Define indexes that define the control
#Energy Efficiency Design Index (EEDI)
EEDI = (P_total * sfc * C_f) / (DWT * V_d)

#Energy Efficiency Existing Ship Index (EEXI)
EEXI = EEDI