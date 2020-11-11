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
driver.get("https://www.techwithtim.net/")    
sleep(5) 
print(driver.title)

search= driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)   
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    #driver.find XX  it's main.find
    articles=main.find_elements_by_tag_name("article")
    #articles=main.find_element_by_tag_name("article") this line gives error -> The difference betwn "find_element" and "find_elements" is single item vs list
    for article in articles:
        header=article.find_element_by_class_name("entry-summary") 
        print(header.text)
        print("")
finally:
    #sleep(5)
    driver.quit()
