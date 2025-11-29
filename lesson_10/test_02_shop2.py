from selenium import webdriver
from lesson_10.klass_for_shop2 import ForShop
import lesson_10.config
import allure


@allure.title("Тестирование интернет-магазина")
@allure.description("Авторизации на сайте, работа кнопок, корректность подсчёта итоговой суммы в корзине")
@allure.feature("Интернет-магазин")
@allure.severity("critical")
def test_shop():
    driver = webdriver.Firefox()
    vb = lesson_10.config
    driver.get("https://www.saucedemo.com/")
    fsh = ForShop(driver)
    fsh.MadeWithData(vb.l_pp, vb.l_pd)
    fsh.madeWidthClick(vb.dann, vb.dann_f)
    fsh.MadeWithData(vb.user_pol, vb.user_dann)
    fsh.madeWidthClick(["continue"], [0])
    assert fsh.GetField("summary_total_label").text == "Total: $58.29"
    fsh.madeWidthClick(["finish"], [0])
    driver.quit()
