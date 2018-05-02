# coding:utf-8

# from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from common.base import Base
from selenium import webdriver
# from excel.readExcel import readExcel

login_url = 'https://mail.qq.com/'
login_url_163 = "https://mail.163.com/"

# filename = "excel.xlsx"
# datafile = readExcel(filename)
# testdata = datafile.readDic()

class LoginPage(Base):
    '''登录QQ邮箱'''
    login_page_button = ('id','switcher_plogin')
    user_args = ('id','u')
    psd_args = ('id','p')
    login_args = ('id','login_button')
    login_after_name = ('css selector','#today_alias')
    iframe = 'login_frame'
    login_iframe = 'mainFrame'
    logout_args = ('link text','退出')
    login_again = ('link text','重新登录')
            
    def open_url(self):
        # 打开网页
        self.driver.get(login_url)
 
        # driver = webdriver.Firefox()
#         print self.driver.get_cookies()
#         self.driver.delete_cookie('pgv_pvi')  
    def click_logout(self):
        self.driver.switch_to.parent_frame()
        self.click(self.logout_args)
        sleep(2)
        self.click(self.login_again)
        
    def logout(self):
        '''登出'''
        
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()
        
    def input_user(self, user):
        self.clear(self.user_args)
        self.sendKeys(self.user_args, user)
    
    
    def input_psd(self, psd):
        self.clear(self.psd_args)
        self.sendKeys(self.psd_args, psd)
    
    def click_login(self):
        self.click(self.login_args)
    
    def login(self, username='2473649005',passwd ='liaga@2015'):
        # 输入的内容也可以采用raw_input的方式
        """登录流程"""
#         self.open_url()
#         sleep(2)
        # 比较特殊，登录是在iframe窗口，需要切换
        self.driver.switch_to_frame(self.iframe)
        self.click(self.login_page_button)
        sleep(1)
        # 1. 输入用户名
        self.input_user(username)
        sleep(1)
        # 2. 输入密码
        self.input_psd(passwd)
        sleep(1)
        # 3. 点击登录
        self.click_login()
        sleep(2)
        
    def login_result(self):
        # 获取登录结果
        print '-----------登录结果----------'
        
        self.driver.switch_to_frame(self.login_iframe)
        try:
            name = self.findElement(self.login_after_name).text
#             print 'name: ',name.encode('utf-8')
#             print  'result', name.encode('utf-8') == testdata[0]['result']
            return name.encode('utf-8')
        except:
            return False
    
    
    def is_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            print 'alert name:',alert.text
            alert.accept()
        except:
            pass
        
    def is_alert_exsits_base(self):
        try:
            alert = self.is_alert_exsit()
            alert.accept()
        except:
            pass

class LoginPage_163(Base):
    """登录 163邮箱"""
    login_iframe = "x-URS-iframe"
    login_user = ("css selector", ".j-inputtext.dlemail")
    login_psd = ("css selector", ".j-inputtext.dlpwd") 
    login_btn = ("id", "dologin")
    login_res = ("id", "spnUid")
#     write_btn= ("xpath", "//span[text()='写 信']")
#     recive_label = ("xpath", ".//*[@class='dG0']/div/div/div/input")
#     subject = ("xpath", ".//*[@class='bz0']/div/input[@class='nui-ipt-input']")
#     add_file = ("xpath", ".//input[@type='file']")
#     content_iframe = ('css selector','iframe.APP-editor-iframe')
#     content_body = ("css selector","html>body")
#     send_btn = ("xpath", "//span[text()='发送']")
    
    def input_user(self, user):
        self.sendKeys(self.login_user, user)
    
    def input_psd(self, psd):
        self.sendKeys(self.login_psd, psd)
        
    def login_163(self, user = "18767120498", psd ="liaga@2018"):
        
        self.driver.switch_to_frame(self.login_iframe)
#         sleep(2)
        self.input_user(user)
        self.input_psd(psd)
        self.click(self.login_btn)
    def login_result(self, res):
        return self.is_text_in_element(self.login_res, res)
        
    def logout(self):
        '''登出'''
        
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()

    
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get(login_url_163)
#     login_page = LoginPage(driver)
#     login_page.open_url()
#     sleep(2)
#     login_page.login()
#     sleep(2)
    login163 = LoginPage_163(driver)
    login163.login_163()
    login163.send_email()
        
        
    