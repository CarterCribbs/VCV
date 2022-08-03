from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime as dt
from datetime import timedelta


#Select day range for LMP Graph
days_ago_start = 365 #put "10" for ten days ago
days_ago_end = 1 #put "1" for yesterday 


s=Service('/Users/cartercribbs/Downloads/Driver/chromedriver')
driver = webdriver.Chrome(service=s)
url='http://www.energyonline.com/Data/GenericData.aspx?DataId=25&PJM___Day-Ahead_Price_For_Hubs'
driver.get(url)
driver.maximize_window()

#Edit start date to desired date
start_date_picker = driver.find_element(By.ID, "ctl00_middleContent_startDatePicker")
start_date_picker.click()
start_date_picker.send_keys(Keys.COMMAND + 'a')
start_date_picker.send_keys(Keys.DELETE)
start_date = dt.date.today() - timedelta(days_ago_start) 
dateStrAGO = start_date.strftime("%m/%d/%Y")
start_date_picker.send_keys(dateStrAGO + " 00:00")
start_date_picker.send_keys(Keys.ENTER)

#Edit end date to desired date
end_date_picker = driver.find_element(By.ID, "ctl00_middleContent_endDatePicker")
end_date_picker.click()
end_date_picker.send_keys(Keys.COMMAND + 'a')
end_date_picker.send_keys(Keys.DELETE)
end_date = dt.date.today()- timedelta(days_ago_end)
dateStrYES = end_date.strftime("%m/%d/%Y")
end_date_picker.send_keys(dateStrYES + " 23:00")
end_date_picker.send_keys(Keys.ENTER)

#Refesh content to desired day range
refresh_button = driver.find_element(By.ID, "ctl00_middleContent_btnRefresh")
refresh_button.click()
time.sleep(2)

#Export CSV to downloads folder
export_button = driver.find_element(By.ID, "ctl00_middleContent_LinkButton1")
export_button.click()







