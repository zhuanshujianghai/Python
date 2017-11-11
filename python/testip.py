import  urllib.request

def checkrealip(url,httptype,ip_port):
    proxy = { httptype:ip_port }
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    try:
        file = opener.open(url,timeout=10)
        if file.getcode()==200:
            return True
        print("垃圾IP（状态码："+file.getcode()+"）："+ip_port)
        return False
    except:
        print("垃圾IP："+ip_port)
        return False

def writerealip():
    fh = open("D:\git_Repertory\PythonFile\\20171111ip.txt","r")
    lines = fh.readlines()
    fh.close()
    file="pypi_python"
    url = "https://pypi.python.org"
    httptype="https"
    for line in lines:
        status = checkrealip(url,httptype,line.replace("\n",""))
        if status:
            print("*************************************" + line)
            fh = open("D:\git_Repertory\PythonFile\\20171111realip_"+file+".txt","a+")
            fh.write(line)
            fh.close()
    print("结束检测并写入")
writerealip()