from selenium.webdriver import Chrome
from time import sleep
from pytest import fixture

@fixture
def setup_tear_down():
    driver=Chrome("C:\\chrome\\chromedriver-win32\\chromedriver.exe")
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    sleep(2)
    yield driver
    driver.close()




