import json
import FlightAware

URL = "https://flightaware.com/live/flight/JBU677/history/20210624/1229Z/KJFK/KJAX"

default_Filename = f"A/{FlightAware.Convert_String_to_FlightAware(URL)}"

Data = FlightAware.Flight_Info(URL, default_Filename+"Image_1", default_Filename+"Image_2")

print(Data)

with open(f"{default_Filename}.json", 'w') as f:
	json.dump(obj=Data.Flight_Info, fp=f, indent=2)