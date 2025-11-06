from selenium.webdriver.common.by import By


class ForShop:
    def __init__(self, driver):
        self.driver = driver

    def madeWidthClick(self, element, s):
        for i in range(len(element)):
            if (s[i] == 0):
                dlya_clika = self.driver.find_element(By.ID, element[i])
            else:
                dlya_clika = self.driver.find_element(By.CLASS_NAME, element[i])
            dlya_clika.click()

    def MadeWithData(self, sammas, sammasd):
        for i in range(len(sammas)):
            kuda = self.driver.find_element(By.ID, sammas[i])
            kuda.send_keys(sammasd[i])

    def GetField(self, element):
        return self.driver.find_element(By.CLASS_NAME, element)
