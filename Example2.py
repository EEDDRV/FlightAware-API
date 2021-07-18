import json
import FlightAware
import os

Flight_Info_Object = FlightAware.Flight_Info(None)
URL = Flight_Info_Object.manual_page_navigation()

Folder_Name = f"{FlightAware.Convert_String_to_FlightAware(URL)}"
default_Filename = f"{Folder_Name}/{FlightAware.Convert_String_to_FlightAware(URL)}"

if not os.path.exists(Folder_Name):
    os.makedirs(Folder_Name)

Flight_Info_Object.get_manual_flight_info()



with open(f"{default_Filename}.json", 'w') as f:
	json.dump(obj=Flight_Info_Object.Flight_Info, fp=f, indent=2)