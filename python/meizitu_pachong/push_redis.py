from redis import Redis
import requests
import re

def push_redis_list():
    r = Redis(host="***填写自己的ip***",port=6379,password="****填写自己的密码***")
    print(r.keys('*'))
    url = "http://www.meizitu.com";
    num_result = requests.get(url,timeout=10)
    num = re.findall('http://www.meizitu.com/a/[0-9]*.html',num_result.text)
    maxnum = 0
    for item in num:
        itemnum = re.findall('[0-9]{4}',item)[0]
        if(int(itemnum)>maxnum):
            maxnum=int(itemnum)
    for i in range(1052,maxnum):
        print("循环次数："+str(i))
        url = 'http://www.meizitu.com/a/' + str(i) + '.html'
        try:
            img_url = requests.get(url, timeout=10)
            if(img_url.status_code==200):
                img_url_list = re.findall('http://mm.chinasareview.com/wp-content/uploads/201.*?.jpg', img_url.text)
                for temp_img_url in img_url_list:
                    l = len(re.findall('limg', temp_img_url))
                    if (l == 0):
                        print("url: ", temp_img_url)
                        r.lpush('meizitu', temp_img_url)
                print("队列总数："+str(r.llen('meizitu')))
            else:
                print("错误的状态码："+str(img_url.status_code))
                r.lpush('meizitu_error',str(i))
        except Exception as e:
            print(e)
        print("\n")
    return 0

push_redis_list()
