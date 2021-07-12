#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
#作业//Python基础 第八天作业-第一题
#写一个Python脚本，使用While循环，
# 每一秒查看一下TCP/80(一定要区分TCP或UDP,80或8000)是否被打开，这里使用FTP服务代替
# 如果打开就退出循环，并且打印告警信息，执行效果如下。
import os
import time
import  re
while True:
    result = os.popen("netstat -an").read()
    port = re.findall("TCP\s+\S+:(\S+)", result)[0]
    time.sleep(2)
    if port =="21":
        print("FTP服务已经打开")
        break
    if port != "21":
        print("FTP服务未打开、等待下一秒轮询")