from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
sleep(3)
button = driver.find_element(By.CLASS_NAME, 'btn-primary')
button.click()
alert = driver.switch_to.alert
alert.accept()
sleep(5)
button.click()
alert = driver.switch_to.alert
alert.accept()
sleep(5)
button.click()
alert = driver.switch_to.alert
alert.accept()
sleep(5)
driver.quit()
