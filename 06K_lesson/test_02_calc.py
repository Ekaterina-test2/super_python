from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_calc():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_element = driver.find_element(By.ID, "delay")
    delay_element.clear()
    delay_element.send_keys("45")
    button7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button7.click()
    button_plus = driver.find_element(By.CLASS_NAME, "btn-outline-success")
    button_plus.click()
    button8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button8.click()
    button_eq = driver.find_element(By.CLASS_NAME, "btn-outline-warning")
    button_eq.click()
    WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    actual_result = driver.find_element(By.CLASS_NAME, "screen").text
    assert actual_result == "15"
    print(actual_result)
    driver.quit()
