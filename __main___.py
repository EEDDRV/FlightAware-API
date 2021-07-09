import pandas, sys, json
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
#chrome_options.headless = True
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_options)
sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line
sys.stdout.write("\033[F") #back to previous line
sys.stdout.write("\033[K") #clear line

Example_Json ="""
{
	"Airline": "",
	"Speed":
	{
		"MPH": "",
		"Mach": "" 
	},
	"Altitude": "",
	"Flight Plan": "",
	"Departure": 
	{
		"Airport": "",
		"Airport_Gate": 
		{
			"Terminal": "",
			"Gate": ""
		},
		"Taxi Time": "",
		"Average_Delay": "",
		"Date": ""
	},

	"Arrival":
	{
		"Airport": "",
		"Airport_Gate":
		{
			"Terminal": "",
			"Gate": ""
		},
		"Taxi Time": "",
		"Average_Delay": "",
		"Date": ""
	},
	"Flight Number": "",
	"Departure Times":
	{
		"Dept_Gate_Time": "",
		"Dept_Takeoff_Time": "",
		"Dept_Gate_Time_Scheduled": "",
		"Dept_Takeoff_Time_Scheduled": ""
	},
	"Arrival Times":
	{
		"Arr_Gate_Time": "",
		"Arr_Landing_Time": "",
		"Arr_Gate_Time_Scheduled": "",
		"Arr_Landing_Time_Scheduled": ""
	}
}
"""

Flight_Json = json.loads(Example_Json)


Url = "https://flightaware.com/live/flight/JBU677/history/20210624/1229Z/KJFK/KJAX"
driver.get(Url)
# Now store the data on the webpage to the json object


# Now we input the airline
Flight_Json["Airline"] = driver.find_element_by_class_name("flightPageFriendlyIdentLbl").text.split(" ")[0]
# Now we input the Speed (MPH)
Flight_Json["Speed"]["MPH"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[8]/div[3]/div/div/div[1]/div[2]").text.split(" ")[1]
# Now we input the Altitude
Flight_Json["Altitude"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[8]/div[3]/div/div/div[2]/div[2]").text.split(" ")[1]
# Now we input the Flight Plan
Flight_Json["Flight Plan"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[8]/div[3]/div/div/div[4]/div[2]").text
# Now we input the Departure airport
Flight_Json["Departure"]["Airport"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/span[1]/span").text
# Now we input the Arrival airport gate
Flight_Json["Arrival"]["Airport_Gate"]["Gate"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]/span/strong").text
# Now we input the Arrival taxi time
Flight_Json["Arrival"]["Taxi Time"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[2]/div[1]/div").text
# Now we input the Average_Delay
Flight_Json["Arrival"]["Average_Delay"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[2]/div[2]/div/span").text
# Now we input the Arival airport
Flight_Json["Arrival"]["Airport"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/span[1]/span").text
# Now we input the Departure terminalTouch
#Flight_Json["Departure"]["Airport_Gate"]["Terminal"] = driver.find_element_by_xpath("").text
# Now we input the Departure gateTouch
Flight_Json["Departure"]["Airport_Gate"]["Gate"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/span[1]/strong").text
# Now we input the Departure terminal Touch
Flight_Json["Departure"]["Taxi Time"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[2]/div[1]/div/span").text
# Now we input the Departure average delayTouch
Flight_Json["Departure"]["Average_Delay"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[2]/div[2]/div/span").text

# Now we input the Dept_Gate_Time.
Flight_Json["Departure Times"]["Dept_Gate_Time"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div").text
# Now we input the Dept_Takeoff_Time.
Flight_Json["Departure Times"]["Dept_Takeoff_Time"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span").text
# Now we input the Dept_Gate_Time_Scheduled.
Flight_Json["Departure Times"]["Dept_Gate_Time_Scheduled"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[1]/div[1]/div[3]/div/span").text
# Now we input the Dept_Takeoff_Time_Scheduled.
Flight_Json["Departure Times"]["Dept_Takeoff_Time_Scheduled"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[1]/div[1]/div[2]/div[3]/div/span").text
# Now we input the Arr_Gate_Time.
Flight_Json["Arrival Times"]["Arr_Gate_Time"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[1]/div[2]/div[2]/span").text
# Now we input the Arr_Takeoff_Time.
Flight_Json["Arrival Times"]["Arr_Landing_Time"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/span").text
# Now we input the Arr_Gate_Time_Scheduled.
Flight_Json["Arrival Times"]["Arr_Gate_Time_Scheduled"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[1]/div[2]/div[3]/div/span").text
# Now we input the Arr_Takeoff_Time_Scheduled.
Flight_Json["Arrival Times"]["Arr_Landing_Time_Scheduled"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[2]/div[2]/div[1]/div[1]/div[3]/div/span").text


# Now we input the Departure Date
Flight_Json["Departure"]["Date"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/span[1]").text
# Now we input the Arrival Date
Flight_Json["Arrival"]["Date"] = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/span[1]").text




# First we input the Flight Number
Flight_Json["Flight Number"] = driver.find_element_by_class_name("flightPageFriendlyIdentLbl").text.split(" ")[1]

print(json.dumps(Flight_Json, indent=4, sort_keys=True))


#""" Screnshot entire page
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
#"""


#print(Flight_Json["Flight Number"])


driver.quit()