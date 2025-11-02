from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def timerdriver(driver, sksek, vern_test):
    WebDriverWait(driver, sksek).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), vern_test))


class For_calc:
    def open_calc(driver):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def sdel_delay(driver, sksek):
        delay_element = driver.find_element(By.ID, "delay")
        delay_element.clear()
        delay_element.send_keys(sksek)

    def Vhod_zn(driver, chi_1, chi_2, sksek, vern_test):
        button = driver.find_element(By.XPATH, chi_1)
        button.click()
        button = driver.find_element(By.CLASS_NAME, "btn-outline-success")
        button.click()
        button = driver.find_element(By.XPATH, chi_2)
        button.click()
        button = driver.find_element(By.CLASS_NAME, "btn-outline-warning")
        button.click()
        timerdriver(driver, sksek, vern_test)
        return driver.find_element(By.CLASS_NAME, "screen").text
