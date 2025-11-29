from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


@allure.step("Открытие страницы калькулятора")
def TimerDriver(driver, sksek: int, vern_test: int):
    """
        Эта функция открывает браузер и ждёт определенное количество секунд, пока не загрузится
        экран калькулятора.
    """
    WebDriverWait(driver, sksek).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), vern_test))


class ForCalc:
    """
    Конструктор класса ForCalc.
    :param driver: WebDriver — объект драйвера Selenium.
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нахождение элемента по локатору, очищение экрана калькулятора, ввод значения")
    def MadeDelay(self, sksek: int):
        """
            Эта функция находит элемент по ID delay, очищает экран,
            вводит необходимое значение
        """
        delay_element = self.driver.find_element(By.ID, "delay")
        delay_element.clear()
        delay_element.send_keys(sksek)

    @allure.step("Ввод 1 числа, 2 числа, установка задержки и их сумма")
    def EnterValue(self, chi_1: str, chi_2: str, sksek: int, vern_test: str) -> str:
        """
            Эта функция берет два параметра, складывает их, устанавливает ожидание,
            возвращает результат
        """
        button = self.driver.find_element(By.XPATH, chi_1)
        button.click()
        button = self.driver.find_element(By.CLASS_NAME, "btn-outline-success")
        button.click()
        button = self.driver.find_element(By.XPATH, chi_2)
        button.click()
        button = self.driver.find_element(By.CLASS_NAME, "btn-outline-warning")
        button.click()
        TimerDriver(self.driver, sksek, vern_test)
        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str — текст результата на экране калькулятора.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text
