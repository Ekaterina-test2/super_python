from selenium import webdriver
from Klass_for_lesson.klass_for_calc import ForCalc
import Klass_for_lesson.config


def test_calc():
    vb = Klass_for_lesson.config
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    clc = ForCalc(driver)
    clc.MadeDelay(vb.sksek)
    actual_result = clc.EnterValue(vb.chi_1, vb.chi_2, vb.sksek, vb.vern_test)
    assert actual_result == vb.vern_test
    driver.quit()
