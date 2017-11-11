import telnetlib
#检查代理ip是否可用
def checkip(ip,port):
    try:
        tn = telnetlib.Telnet(ip, port=port, timeout=10)
    except:
        return False
    else:
        return True