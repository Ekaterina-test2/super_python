from selenium.webdriver.common.by import By
import allure


class ForShop:
    """
    Конструктор класса ForShop
    :param driver: WebDriver — объект драйвера Selenium.
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элементов, их выбор (клик)")
    def madeWidthClick(self, element: list, s: list):
        """
        В эту функцию передается список элементов, на которые необходимо  кликнуть (выбрать).
        """
        for i in range(len(element)):
            if (s[i] == 0):
                dlya_clika = self.driver.find_element(By.ID, element[i])
            else:
                dlya_clika = self.driver.find_element(By.CLASS_NAME, element[i])
            dlya_clika.click()

    @allure.step("Ввод данных авторизации")
    def MadeWithData(self, sammas: list, sammasd: list):
        """
        Эта функция для ввода данных в несколько полей (авторизация, идентификация)
        """
        for i in range(len(sammas)):
            kuda = self.driver.find_element(By.ID, sammas[i])
            kuda.send_keys(sammasd[i])

    @allure.step("Возвращение значения поля")
    def GetField(self, element: list) -> str:
        """
        Данная функция возвращает значение поля, найденного по определенному параметру.
        """
        return self.driver.find_element(By.CLASS_NAME, element)
