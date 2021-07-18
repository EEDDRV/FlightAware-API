import json
import FlightAware
import os, sys

# First check if there is a url in the command arguments
if len(sys.argv) > 1:
	URL = sys.argv[1]
else:
	URL = "https://flightaware.com/live/flight/AAL2465/history/20210424/1940Z/KJAX/KDFW"


Folder_Name = f"{FlightAware.Convert_String_to_FlightAware(URL)}"
default_Filename = f"{Folder_Name}/{FlightAware.Convert_String_to_FlightAware(URL)}"

if not os.path.exists(Folder_Name):
    os.makedirs(Folder_Name)

Data = FlightAware.Flight_Info(URL, default_Filename+"Image_1", default_Filename+"Image_2")

#print(Data)

with open(f"{default_Filename}.json", 'w') as f:
	json.dump(obj=Data.Flight_Info, fp=f, indent=2)