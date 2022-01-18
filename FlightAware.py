import sys, json, csv, re
from bs4 import BeautifulSoup as BS
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

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
	},
	"Distance":
	{
		"Actual": "",
		"Planned": "",
		"Direct": ""
	}
}
"""

def Convert_String_to_FlightAware(String_Example):
	String_Example_2 = String_Example.replace("https://flightaware.com/live/flight/","FlightAware_").replace("/history/","_").replace("/","_")
	# Now remove the 1229Z without explcitly asking for it
	String_Example_3 = String_Example_2.replace(re.findall("[0-9]+Z_",String_Example_2)[0],"")
	# Now move the numbers to the last of the string
	Num_to_move = re.findall("_[0-9]+_", String_Example_3)[0]
	String_Example_4 = String_Example_3.replace(Num_to_move, "_") + Num_to_move[:-1]
	return String_Example_4




# Now convert the top into a class object
class Flight_Info:
	def Convert_String_to_FlightAware_KML(self, String_Example):
		String_Example_2 = String_Example.replace("https://flightaware.com/live/flight/","FlightAware_").replace("/history/","_").replace("/","_")
		# Now remove the 1229Z without explcitly asking for it
		String_Example_3 = String_Example_2.replace(re.findall("[0-9]+Z_",String_Example_2)[0],"")
		# Now move the numbers to the last of the string
		Num_to_move = re.findall("_[0-9]+_", String_Example_3)[0]
		String_Example_4 = String_Example_3.replace(Num_to_move, "_") + Num_to_move[:-1]+".kml"
		return String_Example_4

	def Get_Flight_Info(self, Url, screenshot_page=""):
		Flight_Json = json.loads(Example_Json)
		self.driver.get(Url)
		# Now store the data on the webpage to the json object
		# Now we input the airline
		Flight_Json["Airline"] = self.driver.find_element_by_class_name("flightPageFriendlyIdentLbl").text.split(" ")[0]
		# Now we input the Speed (MPH)
		Flight_Json["Speed"]["MPH"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[1]/div[2]").text.split(" ")[1]
		# Now we input the Altitude
		Flight_Json["Altitude"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[2]/div[2]").text.split(" ")[1]
		# Now we input the Flight Plan
		Flight_Json["Flight Plan"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[4]/div[2]").text
		# Now we input the Departure airport
		Flight_Json["Departure"]["Airport"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/span[1]/span").text
		# Now we input the Arrival airport gate
		Flight_Json["Arrival"]["Airport_Gate"]["Gate"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]/span/strong").text
		# Now we input the Arrival taxi time
		Flight_Json["Arrival"]["Taxi Time"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[2]/div[2]/div[1]/div").text
		# Now we input the Average_Delay
		Flight_Json["Arrival"]["Average_Delay"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[2]/div[2]/div/span").text
		# Now we input the Arival airport
		Flight_Json["Arrival"]["Airport"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/span[1]/span").text
		# Now we input the Departure terminalTouch
		#Flight_Json["Departure"]["Airport_Gate"]["Terminal"] = self.driver.find_element_by_xpath("").text
		# Now we input the Departure gateTouch
		Flight_Json["Departure"]["Airport_Gate"]["Gate"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/span[1]/strong").text
		# Now we input the Departure terminal Touch
		Flight_Json["Departure"]["Taxi Time"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[2]/div[1]").text
#                                                                                 
		# Now we input the Departure average delayTouch
		Flight_Json["Departure"]["Average_Delay"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[2]/div[2]/div/span").text
		# Now we input the Dept_Gate_Time.
		Flight_Json["Departure Times"]["Dept_Gate_Time"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[1]/div[1]/div[2]/div").text
		# Now we input the Dept_Takeoff_Time.
		Flight_Json["Departure Times"]["Dept_Takeoff_Time"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[1]/div[2]/div[2]/div/span").text
		# Now we input the Dept_Gate_Time_Scheduled.
		Flight_Json["Departure Times"]["Dept_Gate_Time_Scheduled"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[1]/div[1]/div[3]/div/span").text
		# Now we input the Dept_Takeoff_Time_Scheduled.
		Flight_Json["Departure Times"]["Dept_Takeoff_Time_Scheduled"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[1]/div[1]/div[2]/div[3]/div/span").text
		# Now we input the Arr_Gate_Time.
		Flight_Json["Arrival Times"]["Arr_Gate_Time"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[2]/div[1]/div[2]/div[2]/span").text
		# Now we input the Arr_Takeoff_Time.
		Flight_Json["Arrival Times"]["Arr_Landing_Time"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[2]/div[1]/div[1]/div[2]/span").text
		# Now we input the Arr_Gate_Time_Scheduled.
		Flight_Json["Arrival Times"]["Arr_Gate_Time_Scheduled"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[2]/div[1]/div[2]/div[3]/div/span").text
		# Now we input the Arr_Takeoff_Time_Scheduled.
		Flight_Json["Arrival Times"]["Arr_Landing_Time_Scheduled"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[5]/div[3]/div[2]/div[1]/div[1]/div[3]/div/span").text
		# Now we input the Departure Date
		Flight_Json["Departure"]["Date"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/span[2]").text
		# Now we input the Arrival Date
		Flight_Json["Arrival"]["Date"] = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/span[2]").text
		# First we input the Flight Number
		Flight_Json["Flight Number"] = self.driver.find_element_by_class_name("flightPageFriendlyIdentLbl").text.split(" ")[1]
		# Now we input the Actual Distance.
		Distance = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[3]/div[2]/span").text
		# Now we sort between the Distances, begining with the actual distance.
		# if regex findall of Actual:\s[0-9]+
		if len(re.findall(r'Actual:\s[0-9]+', Distance)):
			Flight_Json["Distance"]["Actual"] = re.findall(r'Actual:\s[0-9]+', Distance)[0].replace("Actual: ", "")
		else: Flight_Json["Distance"]["Actual"] = "N/A"
		# Now we input the Planned Distance.
		if len(re.findall(r'Planned:\s[0-9]+', Distance)):
			Flight_Json["Distance"]["Planned"] = re.findall(r'Planned:\s[0-9]+', Distance)[0].replace("Planned: ", "")
		else: Flight_Json["Distance"]["Planned"] = "N/A"
		# Now we input the Direct Distance.
		if len(re.findall(r'Direct:\s[0-9]+', Distance)):
			Flight_Json["Distance"]["Direct"] = re.findall(r'Direct:\s[0-9]+', Distance)[0].replace("Direct: ", "")
		else: Flight_Json["Distance"]["Direct"] = "N/A"




		#""" Screnshot entire page
		if screenshot_page != "":
			S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll'+X)
			self.driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
			self.driver.find_element_by_tag_name('body').screenshot(f"{screenshot_page}.png")
		#"""
		return Flight_Json

	def Get_Flight_Info_Table(self, URL, screenshot_page, Return=True):
		self.driver.get(URL + "/tracklog")
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "tracklogTable")))
		contents = self.driver.find_element_by_id("tracklogTable")
		
		records = []
		def To_Array(st):
			length_of_num = len(re.findall('[,0-9]+\s', st[0]))
			#print(length_of_num)
			#print(st)
			if length_of_num <= 2:
				return st
			else:
				try:
					b = re.findall(r'[A-z\s]+[0-9:]+\s[A-z]+', st[0]) + \
						[re.findall(r'-?[0-9.]+', st[0])[3]] + \
						[re.findall(r'-?[0-9.]+', st[0])[4]] + \
						[re.findall(r'\W\s[0-9]+\W', st[0])[0]] + \
						[re.findall(r'[0-9]+\s', st[0])[3].replace(" ", "")] + \
						[re.findall(r'[0-9]+\s', st[0])[4].replace(" ", "")]
					if length_of_num >= 6:
						b.append(re.findall(r'[,0-9]+\s', st[0])[5].replace(" ", ""))
					if  length_of_num == 7 :
						b.append(re.findall(r'[,0-9]+\s', st[0])[6].replace(" ", ""))
					#print(b)
					return b
				except:
					return st
		for index, line in enumerate(contents.text.splitlines()):
			#print line
			line = line.split("\n")
			if index == 0:
				line = line[0].split(" ")
				line = [line[0]+" "+line[1]] + line[2:]
				#print(line)#.split(" "))
				records.append(line)
			if index >= 6:
				line = To_Array(line)
				records.append(line)
			else:
				records.append(line)
		t = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/p[1]/a").get_attribute('href')
		urllib.request.urlretrieve(t, screenshot_page+".kml")
		if screenshot_page != "":
			S = lambda X: self.driver.execute_script('return document.body.parentNode.scroll'+X)
			self.driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
			self.driver.find_element_by_tag_name('body').screenshot(f"{screenshot_page}.png")
		if Return == False:
			# Now save the records into a .csv file.
			# if Filename variable has ".csv" at the end, the .csv file will be overwritten.
			# otherwise, a new file will be created named with ".csv" suffix.
			if screenshot_page.__contains__(".csv"):
				pass
			else:
				screenshot_page = screenshot_page+".csv"
			with open(screenshot_page, "w", newline="", encoding='utf-8-sig') as f:
				writer = csv.writer(f)
				writer.writerows(records)
		else:
			return records


	def __init__(self, URL, screenshot_Flight_Info="", screenshot_Flight_Info_Table_page=""):
		if URL != None:
			self.PATH = "C:\Program Files (x86)\chromedriver.exe"
			self.chrome_options = Options()
			self.chrome_options.headless = True
			self.chrome_options.add_argument('--log-level=3')
			self.driver = webdriver.Chrome(executable_path=self.PATH, chrome_options=self.chrome_options)
			sys.stdout.write("\033[F") #back to previous line
			sys.stdout.write("\033[K") #clear line
			sys.stdout.write("\033[F") #back to previous line
			sys.stdout.write("\033[K") #clear line

			self.Flight_Info = self.Get_Flight_Info(URL, screenshot_page=screenshot_Flight_Info)
			self.Flight_Info_Table = self.Get_Flight_Info_Table(URL, screenshot_Flight_Info_Table_page)
			self.File_Name= self.Convert_String_to_FlightAware_KML(URL)
			self.driver.quit()
	def manual_page_navigation(self):
		self.PATH = "C:\Program Files (x86)\chromedriver.exe"
		self.chrome_options = Options()
		#self.chrome_options.headless = True
		self.chrome_options.add_argument('--log-level=3')
		self.driver = webdriver.Chrome(executable_path=self.PATH, chrome_options=self.chrome_options)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line
		self.driver.get("https://flightaware.com/")
		input("Press enter when ready.")
		# Get the url from the self.driver
		return self.driver.current_url

	def get_manual_flight_info(self, screenshot_Flight_Info="", screenshot_Flight_Info_Table_page=""):
		URL = self.driver.current_url
		self.Flight_Info = self.Get_Flight_Info(URL, screenshot_page=screenshot_Flight_Info)
		self.Flight_Info_Table = self.Get_Flight_Info_Table(URL, screenshot_Flight_Info_Table_page)
		self.File_Name= self.Convert_String_to_FlightAware_KML(URL)
		self.driver.quit()