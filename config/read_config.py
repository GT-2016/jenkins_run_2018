# coding:utf-8
'''
Created on 2018年4月26

@author: Administrator
'''
import os
import ConfigParser

# cur_path = os.path.realpath(__file__)
cur_path = os.path.dirname(__file__)
ini_path = os.path.join(cur_path, 'config.ini')
conf = ConfigParser.ConfigParser()

conf.read(ini_path)

recv_server_read = conf.get('server', 'recv_server')
print recv_server_read