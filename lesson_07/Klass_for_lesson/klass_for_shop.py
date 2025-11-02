from selenium.webdriver.common.by import By


class for_shop:
    def make_s_clikom(driver, element, s):
        for i in range(len(element)):
            if (s[i] == 0):
                dlya_clika = driver.find_element(By.ID, element[i])
            else:
                dlya_clika = driver.find_element(By.CLASS_NAME, element[i])
            dlya_clika.click()

    def make_s_vvodom(driver, sammas, sammasd):
        for i in range(len(sammas)):
            kuda = driver.find_element(By.ID, sammas[i])
            kuda.send_keys(sammasd[i])

    def get_pole_sum(driver, element):
        return driver.find_element(By.CLASS_NAME, element)
