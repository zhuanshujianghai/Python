from redis import Redis
import requests
import time
import os
import sys
import random

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1'}

def get_big_img_url():
    r = Redis(host="***填写自己的ip***",port=6379,password="****填写自己的密码***")
    print(r.keys('*'))
    while(1):
        try:
            url =  r.lpop('meizitu')
            if url:
                download(url)
            else:
                print("队列请求完毕!等待10S后重新请求!")
                time.sleep(10)
        except:
            print("请求失败")
            time.sleep(10)
    return 0

def download(url):
    try:
        r = requests.get(url,headers=headers,timeout=10)
        name = time.time()
        path = sys.path[0]+'/pic'
        if not os.path.exists(path):
            os.makedirs(path)
        file = path+'/'+str(name).replace('.','')+str(random.randint(0,999))+'.jpg'
        f = open(file,'wb')
        f.write(r.content)
        print(file)
        f.close()
    except Exception as e:
        print(e)

get_big_img_url()
