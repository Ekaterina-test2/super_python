from selenium import webdriver
from Klass_for_lesson.klass_for_shop import for_shop


l_pp = ["user-name", "password"]
l_pd = ["standard_user", "secret_sauce"]
dann = ["login-button", "add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie", "shopping_cart_link", "checkout"]
dann_f = [0, 0, 0, 0, 1, 0]
user_pol = ["first-name", "last-name", "postal-code"]
user_dann = ["Ekaterina", "SH", "236000"]


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    for_shop.make_s_vvodom(driver, l_pp, l_pd)
    for_shop.make_s_clikom(driver, dann, dann_f)
    for_shop.make_s_vvodom(driver, user_pol, user_dann)
    for_shop.make_s_clikom(driver, ["continue"], [0])
    assert for_shop.get_pole_sum(driver, "summary_total_label").text == "Total: $58.29"
    for_shop.make_s_clikom(driver, ["finish"], [0])
    driver.quit()
