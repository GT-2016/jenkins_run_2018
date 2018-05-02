# coding:utf-8
'''
函数、类和方法
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
#Firefox 配置
prifile_directory = 'C://Users//Administrator//AppData//Roaming//Mozilla//Firefox//Profiles//ardla6e5.default'
profile = webdriver.FirefoxProfile(prifile_directory)
# driver = webdriver.Firefox(profile)
# driver.get('https://www.baidu.com')
def xpathLogin():
    driver = webdriver.Firefox(profile)
    # 1.绝对路径
    driver.find_element_by_xpath('/html/body/div/div/div/div/a[7]')
    # 2.相对路径:
    driver.find_element_by_xpath(".//*[@id='u1']/a[7]")
    # 3.根据ID加class
    driver.find_element_by_xpath(".//*[@id='u1']/a[@class='lb']")
    # 4.根据ID加name
    driver.find_element_by_xpath(".//*[@id='u1']/a[@name='tj_login']")
    # 5. 根据ID+href
    driver.find_element_by_xpath(".//*[@id='u1']/a[@href='https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5']")
    # 6. 根据text()
    driver.find_element_by_xpath(".//*[@id='u1']/a[text()='登录']")
    # 7. contains
    driver.find_element_by_xpath(".//*[@id='u1']/a[contains(@href,'login')]")
    # 8. start-with()
    driver.find_element_by_xpath(".//*[@id='u1']/a[starts-with(text(),'登')]")
    # 9. and
    driver.find_element_by_xpath(".//*[@id='u1']/a[@name='tj_login' and @class='lb']")
    # 10. following-sibling同级后
    driver.find_element_by_xpath(".//*[@name='tj_trxueshu']/following-sibling::a[1]")
    # 11. preceding-sibling同级前
    driver.find_element_by_xpath(".//*[@class='bri']/preceding-sibling::a[2]")
'''
    1、child  选取当前节点的所有子元素
    2、parent  选取当前节点的父节点
    3、descendant选取当前节点的所有后代元素（子、孙等）
    4、ancestor  选取当前节点的所有先辈（父、祖父等）
    5、descendant-or-self选取当前节点的所有后代元素（子、孙等）以及当前节点本身
    6、ancestor-or-self  选取当前节点的所有先辈（父、祖父等）以及当前节点本身
    7、preceding-sibling选取当前节点之前的所有同级节点
    8、following-sibling选取当前节点之后的所有同级节点
    9、preceding   选取文档中当前节点的开始标签之前的所有节点
    10、following   选取文档中当前节点的结束标签之后的所有节点
    11、self  选取当前节点
    12、attribute  选取当前节点的所有属性
    13、namespace选取当前节点的所有命名空间节点
'''
    
def alertClick(url):
    driver = webdriver.Firefox(profile)
    driver.get(url)
    '''第一步： 找到设置按钮'''
    setup = driver.find_element_by_link_text('设置')
    '''第二步： 鼠标悬停，点击搜索按钮'''
    ActionChains(driver).move_to_element(setup).perform()
    time.sleep(0.5)
    driver.find_element_by_link_text('搜索设置').click()
    # time.sleep(3)       # 页面跳转
    '''第三步： 设置界面，找到下拉框'''
    sel = driver.find_element(By.ID, 'nr')
    time.sleep(1)
    '''第四步： 设置下拉框选项'''
    Select(sel).select_by_index(2)
    sel.click()
    time.sleep(1)
    '''第五步： 点击保存设置按钮'''
    driver.find_element_by_css_selector('.prefpanelgo').click()
    time.sleep(1)
    '''第六步： 切换alert框，并点击确定'''
    alert = driver.switch_to_alert()
    alert.accept()
def logout(driver):
    driver.delete_all_cookies()
    driver.refresh()
    time.sleep(3)
    driver.close()
    driver.quit()
def add(*arg):
    print arg
def add02(a,b):
    print a+b 
if __name__ == '__main__':
    a = {"a":1,"b":4}
    b = [1,4,5,2,65]
    add(*b)
    add02(**a)
#     driver = webdriver.Firefox(profile)
#     driver.get('https://www.baidu.com')
#     alertClick('https://www.baidu.com')
