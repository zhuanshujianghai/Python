#coding=utf-8
import re
import time
import redis
import urllib

headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
job_redis = redis.Redis(host='192.168.1.5',port=6379)


class Clawer():
    identity = 'master'

    def __init__(self):
        if self.identity == 'master':
            for i in range(20):
                url = 'http://www.qiushibaike.com/hot/page/%d'%(i+1)
                job_redis.sadd('urls',url)
        #self.main()

    def get_content(self):
        stories = []
        content_pattern = re.compile('<div class="content">([\w\W]*?)</div>([\w\W]*?)class="stats"')
        pattern = re.compile('<.*?>')
        url = job_redis.spop('urls')
        while url:
            try:
                url = str(url,encoding="utf-8")
                opener = urllib.request.build_opener()
                opener.addheaders = [headers]
                text = opener.open(url).read().decode("utf-8", "ignore")

                content = re.findall(content_pattern, text)
                for x in content:
                    if "img" not in x[1]:
                        x = re.sub(pattern, '', x[0])
                        x = re.sub('\n', '', x)
                        stories.append(x)
            except urllib.request.URLError as err:
                if hasattr(err,"reason"):
                    print(err.reason)
            except Exception as err:
                print("exception err")

            url = job_redis.spop('urls')
            print(url)
        print(stories)
        return stories

    def main(self):
        self.get_content()

if __name__ == '__main__':
    Clawer()






