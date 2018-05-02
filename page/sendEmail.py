# coding:utf-8
'''
Created on 2018年4月25

@author: Administrator
'''
from common.base import Base
from page.login import LoginPage
from time import sleep
from selenium import webdriver

class SendEmail(Base):
    '''
        登录成功后，发送邮件
    '''

    write_email = ('id','composebtn')    # '写信'按钮
    iframe_send = 'mainFrame'           # 切换iframe
    addr_text = ('css selector','#toAreaCtrl>div:nth-child(3)>input')    # 收件人
    subject = ('css selector', '#subject')      # 主题
    upload_file = ('name', 'UploadFile')        # 上传附件
    content = ('css selector','html>body')         # 正文
#     content = ('css selector', "[accesskey='q']")
    send = ('xpath',"//a[@name='sendbtn']")
    
    def click_send_email(self):
        # 点击写信，跳转到iframe_send 处
        self.click(self.write_email)
        sleep(3)
    
    def input_addr_text(self):
        self.driver.switch_to_frame(self.iframe_send)
        sleep(3)
        print self.is_element_exsits(self.addr_text)
        print self.is_visibility_element(self.addr_text)
        ele = self.driver.find_element_by_css_selector('#toAreaCtrl>div:nth-child(3)>input')
        # qq邮箱怎么都定位不了发件人，因为一开始不存在时，元素隐藏且输入后点击出现变动的div
        ele.send_keys('11111')
#         self.sendKeys(self.addr_text, 'ligg@qtec.cn')
        sleep(3)
    def input_sbuject(self):
        
        self.sendKeys(self.subject, u'测试selenium发送邮件是否成功')
        sleep(3)
    
    def input_file(self):
#         self.click(self.upload_file)
        self.sendKeys(self.upload_file, "D:\\test.csv")
        
    def input_main_body(self,text):
        # 添加正文
        iframe_main_body = self.driver.find_element("xpath", '//iframe')
        
        self.driver.switch_to_frame(iframe_main_body)
        sleep(2)
        self.sendKeys(self.content, text)
        
    def click_send(self):
        # 1. 点击写信
        self.click_send_email()
        sleep(5)
        # 2. 输入收件人
        self.input_addr_text()
        # 3. 输入主题
        self.input_sbuject()
        # 4. 添加附件
        self.input_file()
        sleep(5)
        # 5. 填写正文内容
        self.input_main_body(u"Just for test......\
        白日依山尽，黄河入海流。\
        欲穷千里目，更胜一层楼")
        # 6. 点击发送
        self.driver.switch_to.parent_frame()
        self.click(self.send)
        
if __name__ == '__main__':
    prifile_directory = 'C://Users//Administrator//AppData//Roaming//Mozilla//Firefox//Profiles//ardla6e5.default'
    profile = webdriver.FirefoxProfile(prifile_directory)
#     driverOptions = webdriver.ChromeOptions()
#     driverOptions.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
#     driver = webdriver.Chrome("chromedriver",0,driverOptions)
    driver = webdriver.Firefox(profile)
    driver.get('https://mail.qq.com/')
#     login_page = LoginPage(driver)
#     login_page.open_url()
#     sleep(2)
#     login_page.login()
    sleep(5)
    send_email = SendEmail(driver)
    send_email.click_send()
    sleep(3)
#     send_email.input_addr_text()
#     send_email.input_main_body('hhhhhhhhhhhhhhh')
#     login_page.logout()
    print 'end~'
        
    
    
        