from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.implicitly_wait(1) # seconds
driver.implicitly_wait(10) # seconds
driver.get("https://www.bbc.com/")
myDynamicElement = driver.find_element(By.LINK_TEXT, "Culture")

print(myDynamicElement.accessible_name)
print(myDynamicElement.text)
print(driver.title)
print(driver.current_url)

myDynamicElement.click()

print(driver.title)
print(driver.current_url)

driver.quit()

################
#  An implicit wait tells WebDriver to poll the DOM for a certain amount of time
#  when trying to find any element (or elements) not immediately available.
#  The default setting is 0 (zero).
#  Once set, the implicit wait is set for the life of the WebDriver object.
#  see: https://selenium-python.readthedocs.io/waits.html#implicit-waits


#__next > div > nav > section > nav > ul > li:nth-child(6) > div > a