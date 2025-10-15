from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_element = driver.find_element(By.ID, "newButtonName")
input_element.send_keys("SkyPro")
element = driver.find_element(By.ID, "updatingButton")
element.click()
element_text = element.text
print(element_text)

driver.quit()
