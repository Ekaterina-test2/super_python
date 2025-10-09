from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
input_element = driver.find_element(By.ID, "username")
input_element.send_keys("tomsmith")
input_element = driver.find_element(By.ID, "password")
input_element.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CLASS_NAME, 'fa')
button.click()

element = driver.find_element(By.ID, "flash")
element_text = element.text
print(element_text)
driver.quit()
