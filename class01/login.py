# coding:utf-8
'''
Created on 2018��4��17��

@author: Administrator
'''
import time
# from class01.alert import driver
# from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
def login(driver,user='liaga',passwd='liaga@2017'):
    '''登录Mantis'''
    driver.get("http://192.168.90.248/mantis/login_page.php")
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_xpath(".//*[@type='submit']").click()
    time.sleep(3)
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_xpath(".//*[@type='submit']").click()
    time.sleep(3)
    try:
        name = driver.find_element_by_css_selector(".user-info").text
        return name
    except:
        print '登录失败，返回空值'
        return ""
    if name == user:
        print 'Login Success!!'
        
def logout(driver):
    '''logout'''
    driver.delete_all_cookies()
    driver.refresh()
    time.sleep(5)
    driver.close()
    driver.quit()
#----------------------------------------------------------
# 华为荣耀10
#----------------------------------------------------------
def hw_login(driver, user='18767120498', passwd='huawei@22'):
    driver.find_element_by_link_text("立即申购").click()
    time.sleep(3)
    driver.find_element_by_id("login_userName").send_keys(user)
    driver.find_element_by_id("login_password").send_keys(passwd)
    time.sleep(1)
    driver.find_element_by_id("btnLogin").click()
    time.sleep(5)
#     driver.find_element_by_id('skuGroupTagText-34731').click()
#     time.sleep(1)
    driver.find_element_by_link_text("立即申购").click()
    time.sleep(5)
    while True:
        try:
            ele = WebDriverWait(driver, 30000, 1,ignored_exceptions=('ElementNotVisibleException')).until(lambda x : x.find_element('css selector','.honor-box-btn-go'))
            time.sleep(3)
            ele.click()
        except:
            continue

# def add(d):
#     return str(*d)
# if __name__ == '__main__':
#     a = [1,2]
#     b = ["a","b"]
#     for i in zip(b,a):
#         print i
    