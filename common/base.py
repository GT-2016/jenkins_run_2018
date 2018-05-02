#-*- coding:utf-8 -*-
'''
Created on 2018年4月24

@author: Administrator
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver

class Base(object):
    '''
            基类
    
    '''

    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
        self.timeout = 10
        self.poll = 0.5
    
    def findElement(self, args):
        """
        args: 传元祖 （'id','xx'）
        """
#         args:
#         (by, value)
#         driver.find_element("id", "kw")
#         driver.find_element("xpath", "//*[@id='kw']")
#         driver.find_element("css selector", "#kw")
#         driver.find_element("class name", "xxx")
#         driver.find_element("tag name","xxxxxx")
#         """
        
        # 查找某个元素
        ele = WebDriverWait(self.driver, self.timeout,self.poll).until(lambda x:x.find_element(*args))
        return ele
    
#     def findElementNew(self, args):
#         """
#         element 是否存在在 dom,不要求可见
#         """
#         ele = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(args))
#         return ele
    
    def findElements(self, args):
        # 查找某些元素
        ele = WebDriverWait(self.driver, self.timeout,self.poll).until(lambda x:x.find_elements(*args))
        return ele
    
    def clickEle(self, args, n=0):
        # 点击 n=?的元素
        ele = self.findElement(args)
        print ele
        length = len(ele)
        if length < 1:
            print "Don't find the element"
        elif length > n:
            print '越界了！！！！，最大值 %d'%length
        else:
            ele[n].click()
            
    
    def sendKeys(self, args, text):
        # 向某个找到的元素发送文本
        ele = self.findElement(args)
        ele.send_keys(text)
        
    def click(self,args):
        # 点击某个找到的元素按钮
        ele = self.findElement(args)
        ele.click()
        
    def clear(self,args):
        # 清空某个找到元素的文本
        ele = self.findElement(args)
        ele.clear()
    
    def moveToEle(self, args):
        """
                鼠标悬停事件
        """    
        ele = self.findElement(args)
        ActionChains(self.driver).move_to_element(ele).perform()
    
    def is_text_in_element(self, args, text):
        # 判断text是否在这个元素的文本上
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(args, text))
            return result
        except:
            return False
        
    def is_value_in_element(self, args, value):
        # 判断给定的value在这个元素的文本上
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(args,value))
            return result
        except:
            return False
    def is_present_in_dom(self,args):
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(args))
            return ele
        except:
            return False
    def is_visibility_element(self, args):
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.visibility_of_element_located(args))
            return ele
        except:
            return False
    def is_element_exsits(self, args):
        '''查找元素的时候，存在返回element，不存在的时候Timeout异常了'''
        try:
            self.is_present_in_dom(args)
            return True
        except:
            return False
    
    def is_alert_exsit(self, timeout=5):
        # 判断alert框是否存在
        alert = WebDriverWait(self.driver, timeout, self.poll).until(EC.alert_is_present())
        return alert
    
    
    def js_scroll_end(self):
        '''滚动到底部'''
        
        js_heigh = "window.scrollTo(0, document.body.scrollHeight)"
        
        self.driver.execute_script(js_heigh)
        
    def js_focus(self, args):
        '''聚焦元素'''
        targe = self.findElement(args)
        self.driver.execute_script("arguments[0].scrollIntoView();", targe)
    
    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)
    
if __name__ == '__main__':
    browsers = ['Firefox()','Chrome()']
    driver = webdriver.Chrome()
    driver.get('http://www.w3school.com.cn/')
    base = Base(driver)
#     base.js_scroll_end()
#     base.js_scroll_top()
    base.js_focus(('css selector','#d4>h3'))
    
    
        