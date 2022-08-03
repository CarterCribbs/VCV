from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import datetime as dt
from datetime import timedelta


start_date = 1 #put "1" for yesterday 
end_date = 11 #put "11" for ten days ago


s=Service('/Users/cartercribbs/Downloads/Driver/chromedriver')
driver = webdriver.Chrome(service=s)
url='http://www.energyonline.com/Data/GenericData.aspx?DataId=25&PJM___Day-Ahead_Price_For_Hubs'
driver.get(url)
driver.maximize_window()

'''
button1 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_1")
button1.click()
button2 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_2")
button2.click()
button3 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_3")
button3.click()
button4 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_4")
button4.click()
button5 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_5")
button5.click()
button6 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_6")
button6.click()
button7 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_7")
button7.click()
button8 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_8")
button8.click()
button9 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_9")
button9.click()
button10 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_10")
button10.click()
button11 = driver.find_element(By.ID, "ctl00_middleContent_chkSeriesList_11")
button11.click()
'''

#Edit start date to ten days ago
start_date_picker = driver.find_element(By.ID, "ctl00_middleContent_startDatePicker")
start_date_picker.click()
start_date_picker.send_keys(Keys.COMMAND + 'a')
start_date_picker.send_keys(Keys.DELETE)
ten_days_ago = dt.date.today() - timedelta(end_date) 
dateStrTEN = ten_days_ago.strftime("%m/%d/%Y")
start_date_picker.send_keys(dateStrTEN + " 00:00")
start_date_picker.send_keys(Keys.ENTER)

#Edit end date to yesterday at midnight
end_date_picker = driver.find_element(By.ID, "ctl00_middleContent_endDatePicker")
end_date_picker.click()
end_date_picker.send_keys(Keys.COMMAND + 'a')
end_date_picker.send_keys(Keys.DELETE)
yesterday = dt.date.today()- timedelta(start_date)
dateStrYES = yesterday.strftime("%m/%d/%Y")
end_date_picker.send_keys(dateStrYES + " 23:00")
end_date_picker.send_keys(Keys.ENTER)

refresh_button = driver.find_element(By.ID, "ctl00_middleContent_btnRefresh")
refresh_button.click()
time.sleep(2)

export_button = driver.find_element(By.ID, "ctl00_middleContent_LinkButton1")
export_button.click()








#driver.implicitly_wait(10)
#datepicker1 = driver.find_element(By.CLASS_NAME, 'xdsoft_prev')
#datepicker1.click()
#daypicker = driver.find_element(By.XPATH, "//td[@class='xdsoft_date xdsoft_day_of_week5 xdsoft_date xdsoft_weekend']")
#daypicker.click()










