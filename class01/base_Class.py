# coding:utf-8
'''
Created on 2018��4��15��

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import ddt
import demjson
data = (
    {'sum_a':2,'sum_b':3, 'result':5},
    {'sum_a':2,'sum_b':3, 'result':5},
    {'sum_a':5, 'sum_b': 10, 'result':15}
    )
def sum(a,b):
    return a+b
@ddt.ddt
class TestDDT(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
#         cls.data = data
        print '验证a+b,a-b结果'
    @ddt.data(*data)
#     @ddt.unpack           
    def test_01(self, args):
        self.assertTrue(sum(args['sum_a'], args['sum_b']) == args['result'])
        
    @ddt.file_data('test_data.json')
    def test_02(self,value):
        self.assertEqual(len(value), 3)  
#              
    @classmethod
    def tearDownClass(cls):
        print '验证结束'
            
if __name__ == '__main__':
    unittest.main(verbosity=2)

        
        