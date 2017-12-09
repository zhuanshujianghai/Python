#推送代理至redis
from redis import Redis

def push_ip_port():
    r = Redis(host="123.207.236.26", port=6379, password="jianghaidong123456")
    portshuzu = ["80","8080","808","8010","8118","8123","9000","3128","31475","54230","28264","53281"]
    for i in range(1,255):
        for j in range(1, 255):
            for k in range(1, 255):
                for l in range(1, 255):
                    for m in range(len(portshuzu)):
                        ip = str(i) + "." + str(j) + "." + str(k) + "." + str(l)
                        proxy = ip+":"+ portshuzu[m]
                        r.lpush('proxy', proxy)
                        print(ip+"-"+str(r.llen("proxy")))

push_ip_port()