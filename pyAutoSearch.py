from time import sleep
from selenium import webdriver
# for loading chrome webdriver 
from selenium.webdriver.common.keys import Keys
# gives access to enter,escape key etc 
import time

path=r"C:\Users\Rohan\.wdm\drivers\chromedriver\win32\86.0.4240.22\chromedriver"
# path of our chrome webdriver
driver = webdriver.Chrome(path)
driver.get("https://www.techwithtim.net/")    
sleep(5) 
print(driver.title)
search= driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)   
time.sleep(5)
driver.close()
driver.quit()