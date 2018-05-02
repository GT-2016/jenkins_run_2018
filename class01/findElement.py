# -*- coding: utf8 -*-
'''
Created on 2018年4月18

@author: Administrator
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import time
from selenium.webdriver.support import expected_conditions as EC

class FindElement(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
        self.timeout = 30
        self.pool = 0.5
        
        
    def findElement(self, cal):
        
        ele = WebDriverWait(self.driver, self.timeout, self.pool).until(lambda x : x.find_element(*cal), "value---")
        return ele
        is_display = WebDriverWait(self.driver,self.timeout, self.pool,(ElementNotVisibleException)).\
        until_not(lambda x : x.find_element(*cal).is_displayed())
    
        
    def sendKeys(self,cals,str):
        elem = self.findElement(cals)
        elem.send_keys(str)
    
    def click(self,cals):
        ele = self.findElement(cals)
        ele.click()
        
    def logout(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(5)
        self.driver.close()
        self.driver.quit()
class find_elment():
    def __init__(self, by, val):
        self.by = by
        self.val = val
        
    def __call__(self, driver):
        element = WebDriverWait(driver, 20, 1).until(lambda x : x.find_element(self.by,self.val), "kkkk---")    
        return element
    
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    ele = find_elment("id","kw")    # 实例化
    ele(driver).send_keys('eeee')   # 实例化调用__call__变成函数
    """
    title_is()
    title_contains()
    presence_of_element_locater()
    visibility_of_element_located()
    
    """
    result = WebDriverWait(driver, 20, 1).until(EC.title_contains(u"百度"))       # python2.7中文需要转unicode
    print result
    

    
    