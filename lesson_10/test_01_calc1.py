from selenium import webdriver
from lesson_10.klass_for_calc1 import ForCalc
# from klass_for_calc1 import ForCalc
import lesson_10.config
import allure


@allure.title("Тестирование калькулятора: {chi_1} {chi_2} "
              "= {vern_test}")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с различными операциями и задержку вывода результата на опр. количество секунд")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_calc():
    """
    """
    vb = lesson_10.config
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    clc = ForCalc(driver)
    clc.MadeDelay(vb.sksek)
    actual_result = clc.EnterValue(vb.chi_1, vb.chi_2, vb.sksek, vb.vern_test)
    assert actual_result == vb.vern_test
    driver.quit()
