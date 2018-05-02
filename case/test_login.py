# coding=utf-8
'''
Created on 2018年4月9日

@author: liaga
'''
from page.login import LoginPage,LoginPage_163
from selenium import webdriver
from excel.readExcel import readExcel
import unittest
import time
import ddt
url_163 = "https://www.mail.163.com"
filename = "excel.xlsx"
datafile = readExcel(filename)
testdata = datafile.readDic()
# print testdata
# 参数和代码分离
# testdata = [{'user': 'hello', 'psd': 'hello', 'result': 'hello'}, 
# {'user': 'hello', 'psd': 'hello', 'result': 'hello'}, 
# {'user': 'hello', 'psd': 'hello', 'result': 'hello'}, 
# {'user': 'hello', 'psd': 'hello', 'result': 'hello'}, 
# {'user': 'hello', 'psd': 'hello', 'result': 'hello'}]
#==================QQ=======================
# @ddt.ddt
# class TestLogin(unittest.TestCase):
#     u'''测试登录功能点
#     '''
#     @classmethod
#     def setUpClass(cls):
#         '''只在开头执行一次'''
#         print('setUpClass--------------')
#         super(TestLogin, cls).setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.loginpage = LoginPage(cls.driver)
#         cls.loginpage.open_url()
#     
#     def login_case(self,username, psd):
#         # 登录
#         self.loginpage.login(username,psd)
#         # 判断是否有弹窗
# #         self.loginpage.is_alert_exsit()
#         # 获取结果
#         result = self.loginpage.login_result()
#         return result
#     
#     @ddt.data(*testdata)
#     def test_login_01(self, canshu):
#         res = self.login_case(canshu['user'], canshu['psd'])
#         print 'result except: ',canshu['result']
#         print 'res:',res
#         print res == canshu['result']
#         self.assertTrue(canshu['result'] == res)
#         
#     
#     def tearDown(self):
#         print('tearDown--------------------')
# #         self.driver.delete_all_cookies()
# #         self.driver.refresh()
#         self.loginpage.click_logout()
#         time.sleep(3)
# #         alert = self.driver.switch_to_alert()
# #         alert.accept()
# #         time.sleep(5)
# #         self.driver.quit()
#     
#     @classmethod
#     def tearDownClass(cls):
# #         super(TestLogin, cls).tearDownClass()
#         print('tearDownClass-----------------')
#         cls.driver.close()
#         cls.driver.quit()
#==================QQ=======================
@ddt.ddt
class TestLogin_163(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
    def setUp(self):
        '''只在开头执行一次'''
        print('setUpClass--------------')
        self.driver = webdriver.Firefox()
        self.driver.get(url_163)
        self.loginpage163 = LoginPage_163(self.driver)
    
    def login_case(self,username, psd, result):
        # 登录
        self.loginpage163.login_163(username,psd)
        # 判断是否有弹窗
#         self.loginpage.is_alert_exsit()
        # 获取结果
        result = self.loginpage163.login_result(result)
        return result
    
    @ddt.data(*testdata)
    def test_login_01(self, canshu):
        res = self.login_case(canshu['user'], canshu['psd'],canshu['result'])
#         print 'result except: ',canshu['result']
#         print 'res:',res
#         print res == canshu['result']
        self.assertTrue(res == True)
        
    
    def tearDown(self):
        print('tearDown--------------------')
#         self.driver.delete_all_cookies()
#         self.driver.refresh()
#         self.loginpage163.logout()
#         time.sleep(3)
#         alert = self.driver.switch_to_alert()
#         alert.accept()
#         time.sleep(5)
        self.driver.close()
        self.driver.quit()
    
#     @classmethod
#     def tearDownClass(cls):
# #         super(TestLogin, cls).tearDownClass()
#         print('tearDownClass-----------------')
#         cls.driver.close()
#         cls.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)
#     pass