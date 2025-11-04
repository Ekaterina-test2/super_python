from selenium import webdriver
from Klass_for_lesson.klass_for_shop import ForShop
import Klass_for_lesson.config


def test_shop():
    driver = webdriver.Firefox()
    vb = Klass_for_lesson.config
    driver.get("https://www.saucedemo.com/")
    fsh = ForShop(driver)
    fsh.MadeWithData(vb.l_pp, vb.l_pd)
    fsh.madeWidthClick(vb.dann, vb.dann_f)
    fsh.MadeWithData(vb.user_pol, vb.user_dann)
    fsh.madeWidthClick(["continue"], [0])
    assert fsh.GetField("summary_total_label").text == "Total: $58.29"
    fsh.madeWidthClick(["finish"], [0])
    driver.quit()
