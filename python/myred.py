# #coding=utf-8
# import re
# import time
# import redis
# import urllib
#
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
# job_redis = redis.Redis(host='196.168.1.5',port=6379)
#
#
# class Clawer(object):
#     identity = 'master'
#
#     def __init__(self):
#         if self.identity == 'master':
#             for i in range(20):
#                 url = 'http://www.quishibaike.com/hot/page/%d'%(i+1)
#                 job_redis.sadd('urls',url)
#         if __name__ == '__main__':
#             self()
#
#     def get_content(self):
#         stories = []
#         content_pattern = re.compile('<div class="content">([\w\W]*?)</div>([\w\W]*?)class="stats"')
#         pattern = re.compile('<.*?>')
#         url = job_redis.spop('urls')
#         while url:
#             try:
#                 request = urllib.request(url,headers=headers)
#                 response = urllib.urlopen(request)
#                 text = response.read().decode("utf-8", "ignore")
#             except urllib.request.URLError as err:
#                 if hasattr(err,"reason"):
#                     print(err.reason)
#             except Exception as err:
#                 print("exception err")
#             content = re.findall(content_pattern,text)
#             for x in content:
#                 if "img" not in x[1]:
#                     x = re.sub(pattern,'',x[0])
#                     x = re.sub('\n','',x)
#                     stories.append(x)
#             url = job_redis.spop('urls')
#             time.sleep(2)
#         return stories
#
#     def main(self):
#         self.get_content()
#
# if __name__ == '__main__':
#     Clawer()








import redis

pool = redis.ConnectionPool(host='192.168.1.5',port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name','jianghaidong')
print(r.get('name'))






