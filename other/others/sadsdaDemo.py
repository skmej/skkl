# from selenium.webdriver.common.by import By
# dic = {"username":"zhangsan","age":18}
# name = [By.ID,"username","abc"]
#
# print(name)
# print(type(name))
#
# # *args 函数定义的时候 *args 不定长参数
# def add(a,*args,**kwargs):
#     print("a的值是:",a)
#     # print("b的值是:",b)
#     print(*args)
#     print(kwargs)
#     # print(kwargs)
#
# # 参数前面加个*  解包
# # 解包 如果不解包 会把集合当作一个整体传入到函数中
# # 参数前面加上 * 代表解包  把集合里面每个参数都当作单独的参数 传递给函数
# add(*name,username='zhangsan',age=18)

# file = open("aaa.txt","r",encoding='utf8')

# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# import csv
# file = open("aaa.csv","r",encoding="utf8")
# c = csv.reader(file)
# print(c)
# for cs in c:
#     print(cs)
    # for css in cs:
    #     print(css)

# import xlrd
#
# xlsx = xlrd.open_workbook("aaa.xlsx")
# sheet = xlsx.sheet_by_index(0)
#
# print(sheet.ncols)
# print(sheet.nrows)
# # print(sheet.row_values(0))
# # print(sheet.col_values(0))
#
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))

file = open("aaa.json", "r", encoding="utf8")

# import json
# json_str = file.read()
# print(json_str)
# print(type(json_str))
# print(json_str[0])
#
# py_json = json.loads(json_str)
# print(py_json)
# print(type(py_json))
# print(py_json[0])
# new_json = json.dumps(py_json,ensure_ascii=False)
#
# print(new_json)
# print(type(new_json))
# print(new_json[0])
#
# try:
#   import xml.etree.cElementTree as ET
# except ImportError:
#   import xml.etree.ElementTree as ET
#
# tree = ET.parse("./book.xml")
# root = tree.getroot()
# print(root.tag)
# print(root.attrib)
#
# for book in root:
#     print(book.tag)
#     print(book.attrib)
#     for child in book:
#         print(child.tag)
#         print(child.attrib)
#         print(child.text)

import yaml

# file = open("aaa.yml","r",encoding='utf8')
# yaml_str = file.read()
yaml_str='''
 - Ruby
 - Perl
 - Python
'''

py_yaml = yaml.load(yaml_str,Loader=yaml.FullLoader)
print(py_yaml)

