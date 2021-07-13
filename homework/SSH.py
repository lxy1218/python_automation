#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
#作业//Python基础 第九天作业-第一题
#制作SSH函数,安装paramiko,并创建SSH登录设备执行命令的函数
import paramiko
def ssh(ip,username,password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.0.137', port=22, username='root', password='root', timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command('ls')
    x = stdout.read().decode()
    print(x)
if __name__ == "__main__":
   ssh("192.168.0.137","root","root",)