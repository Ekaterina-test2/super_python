from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    dann = ["first-name", "last-name", "address", "e-mail", "phone", "zip-code", "city", "country", "job-position", "company"]
    input_element1 = driver.find_element(By.NAME, dann[0])
    input_element1.send_keys("Иван")
    input_element2 = driver.find_element(By.NAME, dann[1])
    input_element2.send_keys("Петров")
    input_element3 = driver.find_element(By.NAME, dann[2])
    input_element3.send_keys("Ленина, 55-3")
    input_element4 = driver.find_element(By.NAME, dann[3])
    input_element4.send_keys("test@skypro.com")
    input_element5 = driver.find_element(By.NAME, dann[4])
    input_element5.send_keys("+7985899998787")
    input_element6 = driver.find_element(By.NAME, dann[5])
    input_element6.send_keys("")
    input_element7 = driver.find_element(By.NAME, dann[6])
    input_element7.send_keys("Москва")
    input_element8 = driver.find_element(By.NAME, dann[7])
    input_element8.send_keys("Россия")
    input_element9 = driver.find_element(By.NAME, dann[8])
    input_element9.send_keys("QA")
    input_element10 = driver.find_element(By.NAME, dann[9])
    input_element10.send_keys("SkyPro")
    button_s = driver.find_element(By.CLASS_NAME, "btn-outline-primary")
    button_s.submit()

    for i in range(len(dann)):
        tm = driver.find_element(By.ID, dann[i])
        if dann[i] == "zip-code":
            krit = "danger"
        else: krit = "success"# noqa
        assert krit in tm.get_attribute("class")
    driver.quit()
