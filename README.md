# FlightAware-API
The unoffical FlightAware API.
The FlightAware API is a simple, unoffical API for accessing FlightAware data.





# Basic Usage:
``` py
import json, os, sys
import FlightAware

URL = "https://flightaware.com/live/flight/AAL2465/history/20210424/1940Z/KJAX/KDFW" # An example url

Folder_Name = f"{FlightAware.Convert_String_to_FlightAware(URL)}"# Folder to save the data

default_Filename = f"{Folder_Name}/{FlightAware.Convert_String_to_FlightAware(URL)}"

if not os.path.exists(Folder_Name):
    os.makedirs(Folder_Name)

Data = FlightAware.Flight_Info(URL, default_Filename+"Image_1", default_Filename+"Image_2")

with open(f"{default_Filename}.json", 'w') as f:
	json.dump(obj=Data.Flight_Info, fp=f, indent=2) # Save the json data.
```
