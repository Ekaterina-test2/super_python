from selenium import webdriver
from Klass_for_lesson.klass_for_calc import For_calc


def test_calc():
    sksek = 45
    chi_1 = "//span[text()='7']"
    chi_2 = "//span[text()='8']"
    vern_test = "15"
    driver = webdriver.Chrome()
    For_calc.open_calc(driver)
    For_calc.sdel_delay(driver, sksek)
    actual_result = For_calc.Vhod_zn(driver, chi_1, chi_2, sksek, vern_test)
    assert actual_result == vern_test
    driver.quit()
