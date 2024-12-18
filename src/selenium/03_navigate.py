from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.python.org")

# link = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
# link.send_keys(Keys.RETURN)
#
# time.sleep(2)
#
# print(driver.current_url)
# print(driver.title)
#
# driver.back()
#
# print("BACK:")
# print(driver.current_url)
# print(driver.title)

other_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[1]/p[2]/a')

print("OTHER LINK")
print(other_link)
print(other_link.get_attribute('href'))
print(other_link.get_attribute('text'))
other_link.click()

print("CLICK")
print(driver.current_url)
print(driver.title)

driver.close()



############################
# Quick Tutorial to XPATH: https://www.tutorialspoint.com/xpath/xpath_quick_guide.htm
# Finding elements: https://selenium-python.readthedocs.io/locating-elements.html
#

