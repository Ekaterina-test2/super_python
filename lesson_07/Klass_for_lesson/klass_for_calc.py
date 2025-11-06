from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def TimerDriver(driver, sksek, vern_test):
    WebDriverWait(driver, sksek).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), vern_test))


class ForCalc:
    def __init__(self, driver):
        self.driver = driver

    def MadeDelay(self, sksek):
        delay_element = self.driver.find_element(By.ID, "delay")
        delay_element.clear()
        delay_element.send_keys(sksek)

    def EnterValue(self, chi_1, chi_2, sksek, vern_test):
        button = self.driver.find_element(By.XPATH, chi_1)
        button.click()
        button = self.driver.find_element(By.CLASS_NAME, "btn-outline-success")
        button.click()
        button = self.driver.find_element(By.XPATH, chi_2)
        button.click()
        button = self.driver.find_element(By.CLASS_NAME, "btn-outline-warning")
        button.click()
        TimerDriver(self.driver, sksek, vern_test)
        return self.driver.find_element(By.CLASS_NAME, "screen").text
