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
        tn = telnetlib.Telnet(ip, port=port, timeout=1)
    except:
        print("这个代理IP(" + ip + ":" + port + ")竟然没用")
        return False
    else:
        return True

path = "D:/git_repertory/Python/python"
listip = ""
def pachong(url,ge,ceng,filder,addurl,charset):
    global listip
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
        data = opener.open(url).read().decode(charset, "ignore")
        patip = "<td>(\d+?\.\d+?\.\d+?.\d+?)</td>"
        patport = "<td>(\d+?)</td>"
        allip = re.compile(patip).findall(data)
        allport = re.compile(patport).findall(data)
        if len(allip)==len(allport):
            for i in range(len(allip)):
                if checkip(allip[i],allport[i]):
                    content = allip[i]+":" + allport[i]+"\n"
                    if content not in listip:
                        listip = listip + content
                    print(allip[i]+":"+ allport[i]+"***************************")
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
    pat2 = "<a class=\"false\" href=\"(.*?)\""
    alllink = re.compile(pat).findall(data)
    alllink1 = re.compile(pat1).findall(data)
    alllink2 = re.compile(pat2).findall(data)
    alllink.extend(alllink1)
    alllink.extend(alllink2)
    new_alllink = []
    for link in alllink:
        #if link not in new_alllink and ("html" in link or "http:" in link):
        if link not in new_alllink:
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
            data = opener.open(url).read().decode(charset, "ignore")
            patip = "<td>(\d*?\.\d*?\.\d*?.\d*?)</td>"
            patport = "<td>(\d*?)</td>"
            allip = re.compile(patip).findall(data)
            allport = re.compile(patport).findall(data)
            if len(allip) == len(allport):
                for i in range(len(allip)):
                    if checkip(allip[i], allport[i]):
                        content = allip[i] + ":" + allport[i] + "\n"
                        if content not in listip:
                            listip = listip + content
                        print(allip[i] + ":" + allport[i] + "***************************")
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
    fh = open("D:\git_Repertory\PythonFile\\20171111ip.txt", "w")
    fh.write(listip)
    fh.close()
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

# url = ["http://www.135store.com"]
# filder = "135store"
# addurl = "http://www.135store.com/"
#charset = "utf-8"

# url = ["http://bbs.fuling.com/"]
# filder = "fufeng"
# addurl = "http://bbs.fuling.com/"
# charset = "gbk"

# url = ["http://www.taobao.com/"]
# filder = "taobao"
# addurl = "http://www.taobao.com/"
# charset = "utf-8"

url = ["http://www.xicidaili.com"]
filder = "xicidaili"
addurl = "http://www.xicidaili.com/"
charset = "UTF-8"

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











