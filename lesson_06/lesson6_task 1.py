from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(18)
driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()

element = driver.find_element(By.ID, "content")
tekst = element.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(tekst)

driver.quit()
