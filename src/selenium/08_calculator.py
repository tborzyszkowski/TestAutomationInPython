from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://www.calculator.net/basic-calculator.html")

one = driver.find_element(By.XPATH, '//*[@id="sciout"]/div[2]/div[3]/span[1]')
two = driver.find_element(By.XPATH, '//*[@id="sciout"]/div[2]/div[3]/span[2]')


actions = ActionChains(driver)
actions.click(one)
actions.click(two)
actions.perform()

time.sleep(10)

output = driver.find_element(By.XPATH, '//*[@id="sciOutPut"]')
print(output.text)