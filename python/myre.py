import urllib.request
import re

url = "http://edu.csdn.net/huiyiCourse/detail/253"
data = urllib.request.urlopen(url).read().decode("utf-8")
pat = "<p>(\d*?)</p>"
result = re.compile(pat).findall(data)
print(result)
#print(data)


url = "https://read.douban.com/provider/all";
data = urllib.request.urlopen(url).read().decode("utf-8")
pat = "<div class=\"name\">([\u4e00-\u9fa5]*?)</div>"
result = re.compile(pat).findall(data)
print(result)
print(result[0])
fh = open("D:\English\Git_Repertory\Python\python\出版社.txt","a+")
for txt in result:
    fh.write(txt+'\n')
fh.close()