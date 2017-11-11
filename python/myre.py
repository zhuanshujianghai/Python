import urllib.request
import re
import urllib.parse
import urllib.error
import urllib
import os
import socket
import http.client

import telnetlib

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

#检查代理ip是否可用
def checkip(ip,port):
    try:
        tn = telnetlib.Telnet(ip, port=port, timeout=10)
    except:
        return False
    else:
        return True
# url = "http://edu.csdn.net/huiyiCourse/detail/253"
# data = urllib.request.urlopen(url).read().decode("utf-8")
# pat = "<p>(\d*?)</p>"
# result = re.compile(pat).findall(data)
# print(result)
# #print(data)
#
#
# url = "https://read.douban.com/provider/all";
# data = urllib.request.urlopen(url).read().decode("utf-8")
# pat = "<div class=\"name\">([\u4e00-\u9fa5]*?)</div>"
# result = re.compile(pat).findall(data)
# print(result)
# print(result[0])
# fh = open("D:\English\Git_Repertory\Python\python\出版社.txt","a+")
# for txt in result:
#     fh.write(txt+'\n')
# fh.close()

#urllib.request.urlretrieve("http://www.baidu.com","baidu.html")
# file = urllib.request.urlopen("https://read.douban.com/provider/all")
# print(file.info())
# print(file.getcode())
# print(file.geturl())

# for i in range(0,100):
#     try:
#         url = "http://www.135store.com"
#         file = urllib.request.urlopen(url, timeout=1)
#         print(str(len(file.read().decode("utf-8","ignore")))+"------------"+str(i))
#     except Exception as err:
#         print("出现异常"+str(err)+"------------"+str(i))

# url = "http://www.135store.com/api/shop/member!login.do?ajax=yes"
# username = "zhuanshujianghai"
# password ="123456"
# data = urllib.parse.urlencode({"username":username,"password":password}).encode("utf-8")
# req = urllib.request.Request(url,data)
# result = urllib.request.urlopen(req).read().decode("utf-8")
# print(result)

# try:
#     url = "http://blog.csdn.net";
#     result = urllib.request.urlopen(url)
#     print(result.read().decode("utf-8"))
# except urllib.error.URLError as err:
#     #判断是否存在状态码
#     if hasattr(err,"code"):
#         print(err.code)
#     #判断是否存在原因
#     if hasattr(err,"reason"):
#         print(err.reason)

# url = "https://mp.weixin.qq.com/s/67sk-uKz9Ct4niT-f4u1KA"
# params = {"phone":"iphone","name":"jiang"}
# params = urllib.parse.urlencode(params)
#
# req_header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255"}
# req = urllib.request.Request(url)
# req.add_header("User-Agent","Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255")
# res = urllib.request.urlopen(req).read().decode("GBK","ignore")
# print(res)
path = "D:/git_repertory/Python/python"
def pachong(url,ge,ceng,filder,addurl,charset):
    try:
        if url.index("//", 0, 2) == 0:
            url = url[2:]
    except Exception as err:
        pass
    if url.find("login") >= 0:
        return []
    if "www" in url or "http" in url or "https" in url:
        b = b'/:?=&'
        link = urllib.parse.quote(url, b)
        url = link
        print(url)
    else:
        url = addurl + url
        url = url.replace(".com//", ".com/")
        b = b'/:?=&'
        url = urllib.parse.quote(url, b)
        print(url)
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    try:
        file = urllib.request.urlopen(url)
        print(file.info())
        data = opener.open(url).read().decode(charset, "ignore")
    except urllib.request.URLError as err:
        print("*************************************" + url)
        return []
    except socket.timeout as err:
        print("*************************************" + url)
        return []
    except http.client.IncompleteRead as err:
        print("*************************************" + url)
        return []
    except Exception as err:
        print("*************************************" + url)
        return []
    pat = "<a target=\"_blank\" href=\"(.*?)\""
    pat1 = "<a href=\"(.*?)\""
    alllink = re.compile(pat).findall(data)
    alllink1 = re.compile(pat1).findall(data)
    alllink.extend(alllink1)
    new_alllink = []
    for link in alllink:
        if link not in new_alllink and ("html" in link or "http:" in link):
            new_alllink.append(link)
    i = 0
    thisurl=""
    for link in new_alllink:
        try:
            if link.index("//",0,2)==0:
                link = link[2:]
        except Exception as err:
            pass
        if link.find("login")>=0:
            continue
        if "www" in link or "http" in link or "https" in link:
            b = b'/:?=&'
            link = urllib.parse.quote(link, b)
            thisurl=link
        else:
            url = addurl + link
            url = url.replace(".com//", ".com/")
            b = b'/:?=&'
            url = urllib.parse.quote(url, b)
            thisurl=url
        try:
            file = urllib.request.urlopen(thisurl)
            print(str(file.getcode()) + "--------" + thisurl)
            thispath = path+"/"+filder+"/"+ str(ceng)+"/"+str(ge)
            if os.path.exists(thispath)==False:
                os.makedirs(thispath)
            socket.setdefaulttimeout(2)
            urllib.request.urlretrieve(thisurl, thispath +"/" + str(i) + ".html")
            fh = open(thispath + "/list.txt", "a+")
            fh.write(str(file.getcode()) + "--------" + thisurl + "\n")
            fh.close()
        except urllib.request.URLError as err:
            print("*************************************"+thisurl)
            fh = open("D:\git_Repertory\Python\python\\"+filder+"\\"+filder+"_error.txt","a+")
            fh.write(thisurl+"\nURLError\n")
            fh.close()
            # 判断是否存在状态码
            if hasattr(err, "code"):
                print(err.code)
            # 判断是否存在原因
            if hasattr(err, "reason"):
                print(err.reason)
        except socket.timeout as err:
            print("*************************************" + thisurl)
            fh = open("D:\git_Repertory\Python\python\\" + filder + "\\" + filder + "_error.txt", "a+")
            fh.write(thisurl + "\ntimeout\n")
            fh.close()
        except http.client.IncompleteRead as e:
            print("*************************************" + thisurl)
            fh = open("D:\git_Repertory\Python\python\\" + filder + "\\" + filder + "_error.txt", "a+")
            fh.write(thisurl + "\nIncompleteRead\n")
            fh.close()
        except Exception as err:
            print("*************************************" + thisurl)
            fh = open("D:\git_Repertory\Python\python\\" + filder + "\\" + filder + "_error.txt", "a+")
            fh.write(thisurl + "\nException\n")
            fh.close()
        i = i + 1
    return new_alllink
def digui(alllink,ge,ceng,filder,addurl,charset):
    thisalllink=[]
    for link in alllink:
        templink = pachong(link,ge,ceng,filder,addurl,charset)
        if templink!=[]:
            thisalllink.extend(templink)
            ge = ge + 1
    if(len(thisalllink)>0):
        ceng = ceng +1
        ge=1
        print("开始爬取第" + str(ceng) + "层")
        digui(thisalllink,ge,ceng,filder,addurl,charset)
    else:
        print("爬取完毕")


url = ["https://www.baidu.com/s?wd=%E4%BB%A3%E7%90%86ip&tn=94155026_hao_pg"]
filder = "baidu"
addurl = "http://www.baidu.com/"
charset = "utf-8"

digui(url,1,1,filder,addurl,charset)

# url = "http://www.135store.com"
# file = urllib.request.urlopen(url)
# print(file.info())
# headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read().decode("utf-8","ignore")
# pat = "<a target=\"_blank\" href=\"(.*?)\""
# pat1 = "<a href=\"(.*?)\""
# alllink = re.compile(pat).findall(data)
# alllink1 = re.compile(pat1).findall(data)
# alllink.extend(alllink1)
# new_alllink = []
# for link in alllink:
#     if link not in new_alllink and "html" in link:
#         new_alllink.append(link)
# i=0
#
# for link in new_alllink:
#     if "www" in  link or "http" in link or "https" in link:
#         b = b'/:?='
#         link = urllib.parse.quote(link, b)
#         file = urllib.request.urlopen(link)
#         print(str(file.getcode()) + "--------" + link)
#         urllib.request.urlretrieve(link, "135store/"+str(i) + ".html")
#     else:
#         url = "http://www.135store.com" + link
#         b = b'/:?='
#         url = urllib.parse.quote(url,b)
#         print(url)
#         file = urllib.request.urlopen(url)
#         print(str(file.getcode()) + "--------" + link)
#         urllib.request.urlretrieve(url, "135store/"+str(i) + ".html")
#     i=i+1











