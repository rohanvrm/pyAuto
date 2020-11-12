from time import sleep
from selenium import webdriver
# for loading chrome webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# gives access to enter,escape key etc 
import time

path=r"C:\Users\Rohan\.wdm\drivers\chromedriver\win32\86.0.4240.22\chromedriver"
# path of our chrome webdriver
driver = webdriver.Chrome(path)
# we named our driver as "driver"
driver.get("https://www.instagram.com/")
sleep(2)

#driver.find_element_by_class_name("f0n8F ").send_keys("USERNAME") ----> Cannot use this it is same for password too
#better use xpath, full xpath
#add \ before ""

driver.find_element_by_xpath(("//*[@id=\"loginForm\"]/div/div[1]/div/label")).send_keys("Username")
driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[2]/div/label").send_keys("password")
driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]/button").click()
sleep(5)
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

sleep(3)
#driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/section/div/div[2]/div/article[1]/header/div[2]/div[1]/div/span/a").click()



for i in range(10):
        #sleep(2)
        #driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
       # sleep(2)
        for j in range(5):
            
            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div["+str(j+1)+"]/div[3]/button/div").click()
           
        driver.refresh()
        sleep(5) 