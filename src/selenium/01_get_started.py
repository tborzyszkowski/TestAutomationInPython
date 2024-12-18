from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title

# search = driver.find_element(By.NAME, "q")
# search.clear()
# search.send_keys("pycon")
# search.send_keys(Keys.RETURN)
#
# time.sleep(2)
#
# assert "No results found." not in driver.page_source

driver.close()


###################
# 1. Selenium instalation see:
#   https://selenium-python.readthedocs.io/installation.html
# 2. See chapter: Getting Started
# 3. Go to python org and see the page structure: More tools -> Developer tools (Ctrl-Shift-I)
#