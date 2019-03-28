import socket
import sys

def retbanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        ans=s.recv(1024)
        return ans
    except:
        return

def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print '[+] FreeFloat FTP Server is vulnerable.'
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print '[+] 3CDaemon FTP Server is vulnerable.'
    elif 'Ability Server 2.34' in banner:
        print '[+] Ability FTP Server is vulnerable.'
    elif 'Sami FTP Server 2.0.2' in banner:
        print '[+] Sami FTP Server is vulnerable.'
    else:
        print '[-] FTP Server is not vulnerable.'
    return

    

def main():
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]
    if argc == -1 or argc > 2:
        print "用法：python",sys.argv[0],"IP地址 端口号"
        print "例如：url为http://127.0.0.1:8080/，则IP地址应为127.0.0.1，端口号应为8080"
        sys.exit()
        
    ip1="192.168.109.147"
    port=21

    if argc >= 1:
        ip = argv[0]
    if argc == 2:
        port = argv[1]
        
    banner1=retbanner(ip1,port)
    if banner1:
        print '[+]' +ip1 + ':' +banner1.strip('\n')
        checkVulns(banner1)

if __name__ == '__main__':
    main()
