from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

#EDIT THIS BLOCK ONLY
url = <URL>
usn = <USERNAME>
pwd = <PASSWORD>

#UNIX TIMESTAMP
date_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
timestamp = int(time.mktime(date_time.timetuple()))

driver = webdriver.<BROWSER>
driver.get(url)

driver.implicitly_wait(3)

#USERNAME
worker = driver.find_element(by=By.ID, value="username")
worker.send_keys(usn)

#PASSWORD
worker = driver.find_element(by=By.ID, value="password")
worker.send_keys(pwd)

#LOG-IN
worker = driver.find_element(by=By.ID, value="loginbtn")
worker.click()
time.sleep(3)

#NEW URL(if?)
url = <URL>

#LIST OF SUBJECTS
dictionary = {'<SUBJECT_NAME>' : <SUBJECT_CODE>}


for name, ids in dictionary.items():
	url_1 = url + str(ids)
	driver.get(url_1)
	time.sleep(1)
	try:
		#OPEN ATTENDANCE(if?)
		EC.text_to_be_present_in_element( (By.CLASS_NAME,"statuscol"),"Submit attendance")
		worker = driver.find_element(by=By.CSS_SELECTOR, value='a[href*="attendance"]')
		worker.click()
		time.sleep(1)	
    
		#PRESENT
		worker = driver.find_element(by=By.CLASS_NAME, value="statusdesc")
		time.sleep(1)
		worker.click()
		worker.click()
    
		#SUBMIT
		worker = driver.find_element(by=By.ID, value="id_submitbutton")
		time.sleep(2)
		worker.click()
		print("Attendance Submitted for", name)
    
	except Exception:
		print("Attendance is closed in", name)
    
driver.quit()
