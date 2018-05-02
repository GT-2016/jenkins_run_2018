# coding:utf-8
'''
Created on 2018年4月26

@author: Administrator
'''
from common.base import Base
from time import sleep
from selenium import webdriver

login_mantins_url = 'http://192.168.90.248/mantis/login_page.php'

class LoginMantins(Base):
    '''
    Mantins登录
    '''
    login_user = ('id','username')
    login_button = ('xpath',"//input[@type='submit']")
    login_psd = ('id','password')
    result_user = ('css selector','.user-info')
    
    def input_user(self, username):
        self.sendKeys(self.login_user,username)
    
    def input_psd(self,psd):
        self.sendKeys(self.login_psd, psd)
    
    def click_login(self):
        self.click(self.login_button)
        
    def login_mantins(self, username='liaga', psd = 'liaga@2017'):
        # 1. 输入用户名
        self.input_user(username)
        # 2. 点击登录
        self.click_login()
        # 3. 输入密码
        self.input_psd(psd)
        # 4. 点击登录
        self.click_login()
        
    def get_login_result(self):
        try:
            name = self.findElement(self.result_user).text
            print type(name)
            return name.encode('utf-8')
        except:
            return ''
    def logout_mantins(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
    def logout_quit(self):
        self.driver.close()
        self.driver.quit()
        
    
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get(login_mantins_url)
    loginMantins = LoginMantins(driver)
    loginMantins.login_mantins()
    loginMantins.logout_mantins()
    loginMantins.logout_quit()
    
    
    
    
        
        
    
        