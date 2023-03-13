from lib import SeleniumWrapper
from time import sleep
import pytest
from homepage import HomePage

headers="gender,fname,lname,day,month,year,email,cname,pwd,cpwd"

data=[("Male","kallesh","pillesh","19","July","1998","kallesh456@gmail.com","xyz","password123","password123"),
      ("Female","Mallesh","thillesh","18","June","1991","pilleslesh456@gmail.com","xkz","password321","password321")]

@pytest.mark.parametrize(headers,data)
def test_reg(setup_tear_down,gender,fname,lname,day,month,year,email,cname,pwd,cpwd):
    sw=SeleniumWrapper(setup_tear_down)
    hp=HomePage(setup_tear_down)
    hp.click_reg()
    sleep(2)     
    if gender=="Male":
        sw.click_element(("id","gender-male"))
    else:
        sw.click_element(("id","gender-female"))

    sw.enter_text(("id","FirstName"),value=fname)
    sleep(2)
    sw.enter_text(("id","LastName"),value=lname)
    sleep(2)
    sw.select_item(("name","DateOfBirthDay"),item=day)
    sleep(2)
    sw.select_item(("name","DateOfBirthMonth"),item=month)
    sleep(2)
    sw.select_item(("name","DateOfBirthYear"),item=year)                                                                                                                                                                                                                                                                                           
    sleep(2)
    sw.enter_text(("id","Email"),value=email)
    sleep(2)
    sw.enter_text(("id","Company"),value=cname)
    sleep(2)
    sw.enter_text(("id","Password"),value=pwd)
    sleep(2)
    sw.enter_text(("id","ConfirmPassword"),value=cpwd)
    sleep(2)
    sw.click_element(("id","register-button"))
    