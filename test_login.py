from lib import SeleniumWrapper
from time import sleep
from homepage import HomePage
import pytest

headers="email,password"

data=[("malli123@gmail.com","password123"),
      ("kaali998@gmail.com","password576")]

@pytest.mark.parametrize(headers,data)
def test_log(setup_tear_down,email,password):
    sw=SeleniumWrapper(setup_tear_down)
    hp=HomePage(setup_tear_down)
    hp.click_log()
    sleep(2)
    sw.enter_text(("id","Email"),value=email)
    sleep(2)
    sw.enter_text(("id","Password"),value=password)
    sleep(2)
    sw.click_element(("xpath","//button[text()='Log in']"))
