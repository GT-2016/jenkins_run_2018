# coding:utf-8
'''
Created on 2018年4月26

@author: Administrator
'''
from selenium import webdriver
from time import sleep
url_12306 = "https://kyfw.12306.cn/otn/leftTicket/init"
rich_txt_url = "http://www.layui.com/demo/layedit.html"

def calenderVal(driver,value):
    # 日历取出relayonly属性，修改时间
    js_remove_readonly = "$('#train_date').removeAttr('readonly').val('%s')"%value
    driver.execute_script(js_remove_readonly)

def richTxt(driver):
    # 通过js脚本执行，不过报错$未定义
    txt = raw_input("please input some text!!")
    js_rich_txt = "document.getElementById('LAY_layedit_1').contentWindow.document.body.innerHTML ='%s'"%txt
    driver.execute_script(js_rich_txt)

def rich_txt(driver,value):
    # 切换iframe窗口
    driver.switch_to_frame("LAY_layedit_1")
    ele = driver.find_element('xpath','.//html/body')
    ele.clear()
    ele.send_keys(value)

def logout(driver):
    print 'logout'
    driver.close()
    driver.quit() 
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get(rich_txt_url)
    sleep(3)
    text = """
    1111111111
    2222222222
    3333333333
    """
    rich_txt(driver, text)
    sleep(2)
    logout(driver)