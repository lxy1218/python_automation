#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
#作业//Python基础 第九天作业-第一题
#制作SSH函数,安装paramiko,并创建SSH登录设备执行命令的函数
#SSH登录设备查看到网关、并且查看到了路由
import paramiko
import  re
import os
def ssh(ip,username,password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.0.137', port=22, username='root', password='root', timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command('ls')
    x = stdout.read().decode()
    print(x)
    return x
def get_route(ip, username, password):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.0.137', port=22, username='root', password='root', timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command('route')
        x = stdout.read().decode()
        #print(x)
        Gateway = re.findall("gateway\s+(\S+)",x)[0]
        print("网关是"+Gateway)
if __name__ == "__main__":
    ssh("192.168.0.137","root","root",)
    get_route("192.168.0.137","root","root",)

