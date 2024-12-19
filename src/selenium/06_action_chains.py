from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

driver.implicitly_wait(10)

py_docs = driver.find_element(By.XPATH, '//*[@id="documentation"]')
py_av = driver.find_element(By.XPATH, '//*[@id="documentation"]/ul/li[2]/a')

print(driver.title)

actions = ActionChains(driver)
actions.move_to_element(py_docs)
actions.click(py_av)
actions.perform()

print(driver.title)

########
# see: https://selenium-python.readthedocs.io/api.html#selenium.webdriver.common.action_chains.ActionChains