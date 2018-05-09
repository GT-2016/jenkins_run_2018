# coding:utf-8
import unittest
import time
from common.HTMLTestRunner_yo import HTMLTestRunner

files_01 = unittest.defaultTestLoader.discover('D:\\Users\\liaga\\workspace\\unit01\\src\\case', 'test_login*.py')
# 先打印出来，看有没加载1231
# print(type(files_01))
files_02 = unittest.defaultTestLoader.discover('D:\\Users\\liaga\\workspace\\unit01\\src\\case', 'test_login*.py')
# all = unittest.TestSuite()
# all.addTests(files_01)
# print(all)
start_time = time.strftime("%Y_%m_%d_%H_%M_%S")
print(start_time)

report_path = ".\\report"+"\\report.html"#%start_time
fp = file(report_path, "wb")
desc = '1. test_01测试能否打开url及正确输入；'+'\n'+'2. test_02测试能否登录成功'+'\n'+'3. test_03测试错误登录'

runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title="使用Unittest模块打印html测试报告",
                        description=desc)       #retry=1失败重试，没通过

runner.run(files_01)
# stop_time = time.strftime("%Y_%m_%d_%H_%M_%S")
fp.close()
# report_path = "D:\\Users\\liaga\\workspace\\unit01\\src\\report"+"\\report%s-%s.html"%(start_time,stop_time)
# fp = open(report_path, "wb")

