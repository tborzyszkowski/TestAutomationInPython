from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://docs.python.org/3/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Global module index"))
    )
    print(driver.current_url)
    print(driver.title)

    element.click()

    print(driver.current_url)
    print(driver.title)
    print(len(driver.page_source))

finally:
    driver.quit()

##################################
# See other WebDriverWait conditions on https://selenium-python.readthedocs.io/waits.html
#

