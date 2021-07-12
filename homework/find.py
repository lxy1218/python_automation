#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
#作业//Python基础 第八天作业-第二题(不用函数解决)
#找到两个清单中相同的内容
#方案一:不用函数解决
#方案二:修改为函数的更加通用的方案
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
for a in list2:
    #print(a)
    for b in list1:
        #print(b)
        if a == b:
            print(str(b) +" in list1 and list2")
            list1.remove(b)

for c in list1:
    print(str(c) +" only in list1")


