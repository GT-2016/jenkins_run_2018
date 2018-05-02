#!/usr/local/bin/python2.7
# encoding: utf-8
from xlrd import open_workbook
import os
from xlwt import Workbook,XFStyle,Font

"""
读取excel内容
"""
class readExcel(object):
    def __init__(self, name):
        """获取当前路径"""
        curpath = os.path.dirname(__file__)
#         realpath = os.path.realpath(__file__)    # 文件路径，带文件名
        """获取excel文件【与当前脚本在同一级目录下】"""
        self.filename = os.path.join(curpath, name)
        try:
            self.excel_handle = open_workbook(self.filename)        # 路径不包含中文
        except IOError:
            print 'IOError: [Errno 2] No such file or directory'
        # sheet1 = self.excel_handle.sheet_names()[1]           # 获取第1个sheet的名字,可与获取name函数一起使用
        # sheet = self.excel_handle.sheet_by_name('Sheet1')     # 根据名字获取
        self.sheet = self.excel_handle.sheet_by_index(1)             # 根据索引获取第一个sheet
        # print sheet.name,sheet.nrows,sheet.ncols         # 获取sheet的表格名称、总行数、总列数
        self.row_num = self.sheet.nrows       # 行
        #  col_num = sheet.ncols       # 列
    def readDic(self):
        arr = []
        row1 = self.sheet.row_values(0)
        # 因为是Unicode编码格式，因此需要转成utf-8
        for i in range(1,self.row_num):
            dic = {}
#             print self.sheet.row_values(i)
            dic[row1[0].encode('utf-8')] = self.sheet.row_values(i)[0].encode('utf-8')
            dic[row1[1].encode('utf-8')] = self.sheet.row_values(i)[1].encode('utf-8')
            dic[row1[2].encode('utf-8')] = self.sheet.row_values(i)[2].encode('utf-8')
            arr.append(dic)
        return arr

class writeExcel(object):
    def __init__(self):
        self.excel_w = Workbook(encoding='utf-8')           # 设置编码格式
        self.excel_w_sheet = self.excel_w.add_sheet('MySheet1')       # 添加sheet表
        
    def writLabel(self):
        """向excel写入内容，内容自定义"""
        style = XFStyle()                              # 初始化样式
        font = Font()                                  # 为样式创建字体
        font.name = 'Times New Roman' 
        # font.bold = True                                  # 黑体
        # font.underline = True                             # 下划线
        # font.italic = True                                # 斜体字
        style.font = font                                   # 设定样式
        for i in range(10):
            for j in range(5):
                self.excel_w_sheet.write(i,j, label = 'admin%d%d'%(i,j))# 参数对应 行, 列, 值
        self.excel_w.save('Excelw.xls')
from xlutils.copy import copy
class rwExcel(object):
    def __init__(self,name):
        curpath = os.path.dirname(__file__)
        self.newpath = os.path.join(curpath,name)
        
    def _writeA(self):
        self.excelr = open_workbook(self.newpath)
        excelw = copy(self.excelr)      # 将r转为w
        sheetw = excelw.add_sheet('new Sheet')
        val = {
            'abc':111,
            'efg':222,
            'hij':333
            }
        i = 1
        for key in val:
            sheetw.write(1,i,key)
            sheetw.write(2,i,val[key])
            i+=1
            
        excelw.save(self.newpath)   
        
if __name__ == '__main__':
#     read_excel = readExcel('测试.xlsx'.decode('utf-8').encode('gbk'))
    read_excel = readExcel('excel.xlsx')
    print read_excel.readDic()
#     excel_w = writeExcel()
#     excel_w.writLabel()
#     print os.path.realpath(__file__)
    