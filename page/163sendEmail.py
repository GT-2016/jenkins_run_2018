# coding:utf-8
'''
Created on 2018��4��27��

@author: Administrator
'''
from common.base import Base
from page.login import LoginPage_163
from selenium import webdriver
from time import sleep

class SendEmail_163(Base):
    '''
    163邮箱登录，并发送邮件
    '''
    write_btn= ("xpath", "//span[text()='写 信']")
    recive_label = ("xpath", ".//*[@class='dG0']/div/div/div/input")
    subject = ("xpath", ".//*[@class='bz0']/div/input[@class='nui-ipt-input']")
    add_file = ("xpath", ".//input[@type='file']")
    content_iframe = ('css selector','iframe.APP-editor-iframe')
    content_body = ("css selector","html>body")
    send_btn = ("xpath", "//span[text()='发送']")
    reslut_text = ("css selector", "[role='tooltip']")
    
    def write_btn_click(self):
        self.click(self.write_btn)
        
    def input_addr(self, addr):
        self.sendKeys(self.recive_label, addr)
        
    def input_subject(self):
        self.sendKeys(self.subject, u"selenium test for是否正常")
    
    def add_files(self):
        self.sendKeys(self.add_file, "D:\\Users\\liaga\\workspace\\unit01\\src\\report\\report2018_04_27_20_41_12.html")
        
    def input_main_body(self):
        
        self.driver.switch_to.frame(self.findElement(self.content_iframe))
        # 6.
        self.sendKeys(self.content_body, u"百日依山郡\
        黄河如海浪\
        欲穷千里目\
        更加已成楼。1\
        2222222222222222222222\
        33333333333333333")
    def send_btn_click(self):
        sleep(2)
        self.driver.switch_to.parent_frame()
        self.click(self.send_btn)
    def send_email(self, addr="liq03@qtec.cn"):
        login163 = LoginPage_163(self.driver)
        login163.login_163()
        sleep(5)
        #1.
        self.write_btn_click()
        #2.
        self.input_addr(addr)
        #3.
        self.input_subject()
        #4.
        self.add_files()
        #5.
        self.input_main_body()
        #6.
        self.send_btn_click()
        
    def result_send(self):
        
        return self.is_text_in_element(self.reslut_text, u"发送成功")
    
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://mail.163.com/")
    log163 = SendEmail_163(driver)
    log163.send_email()
    print log163.result_send()
    
    