# coding:utf-8
'''
Created on 2018年4月9日

@author: liaga
'''
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
# help(unittest)

baidu_url = "https://www.baidu.com/"
baidu_btn = ('xpath', "//input[@type='submit']")
tj_mnavs = ('css selector', '.mnav')
input_baidu = ('id','kw')

class ElementOperate(object):
    """
    封装等待方法，定位元素单数和复数封装
    """
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.poll = 1 

    def findElement(self, args):
        # 定位元素单数
        ele = WebDriverWait(self.driver, self.timeout,self.poll).until(lambda x:x.find_element(*args), "Can't find!!")
        return ele
    
    def findElements(self, args):
        # 定位元素复数
        eles = WebDriverWait(self.driver, self.timeout,self.poll).until(lambda x:x.find_elements(*args), "Can't finds!!")
        return eles
    
    def click_btn(self, args):
        # 点击元素事件
        ele = self.findElement(args)
        ele.click()
    
    def send_text(self, args, text):
        # 发送文本事件
        ele = self.findElement(args)
        ele.send_keys(text)
        
    def logout(self):
        self.driver.quit()
        self.driver.close()
        
if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     driver.get(baidu_url)
#     element_operate = ElementOperate(driver)
#     sleep(3)
#     element_operate.send_text(input_baidu, u'百度')   # 输入框内容：百度
#     element_operate.click_btn(baidu_btn)      # 按钮：百度一下
#     element_operate.logout()
    path = "D:\\Users\\liaga\\workspace\\unit01\\src\\report\\*"
    import os
    print os.path.isfile(path)
#     print '百度一下：',baidu_btn_ele
#     tj_mnavs_eles = element_operate.findElements(tj_mnavs)
#     print '标签页：',tj_mnavs_eles
        
    