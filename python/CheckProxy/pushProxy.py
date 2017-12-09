#推送代理至redis
from redis import Redis
import time

def push_ip_port():
    r = Redis(host="123.207.236.26", port=6379, password="jianghaidong123456")
    portshuzu = ["80","8080","808","8010","8118","8123","9000","3128","31475","54230","28264","53281"]
    #每次运行前先获取之前的ip记录
    starti = int(r.get("ip1"))
    startj = int(r.get("ip2"))
    startk = int(r.get("ip3"))
    startl = int(r.get("ip4"))
    for i in range(starti,255):
        for j in range(startj, 255):
            for k in range(startk, 255):
                for l in range(startl, 255):
                    for m in range(len(portshuzu)):
                        if int(r.llen("proxy"))>5000000:
                            print("list集合中当前长度为："+str(r.llen("proxy")))
                            print("长度太过惊人，内存消耗过大，将休息30s后再战")
                            time.sleep(30)
                        else:
                            try:
                                ip = str(i) + "." + str(j) + "." + str(k) + "." + str(l)
                                proxy = ip+":"+ portshuzu[m]
                                r.lpush('proxy', proxy)
                                print(ip+"-"+str(r.llen("proxy")))
                            except Exception as e:
                                print(e)
                                print("push到redis发生异常,3600s后继续")
                                time.sleep(3600)
                                #睡眠完成后，再给这货一次机会，不行就抛错退出程序
                                ip = str(i) + "." + str(j) + "." + str(k) + "." + str(l)
                                proxy = ip + ":" + portshuzu[m]
                                r.lpush('proxy', proxy)
                                print(ip + "-" + str(r.llen("proxy")))
                    try:
                        # 记录当前的ip4
                        r.set("ip4", l)
                    except:
                        print("记录ip4出错，3600s后继续")
                        time.sleep(3600)
                        # 同样，睡眠完成后，再给这货一次机会，不行就抛错退出程序
                        r.set("ip4", l)
                try:
                    # 记录当前的ip3
                    r.set("ip3", k)
                except:
                    print("记录ip3出错，3600s后继续")
                    time.sleep(3600)
                    # 同样，睡眠完成后，再给这货一次机会，不行就抛错退出程序
                    r.set("ip3", k)
                startl=1
            try:
                # 记录当前的ip2
                r.set("ip2", j)
            except:
                print("记录ip2出错，3600s后继续")
                time.sleep(3600)
                # 同样，睡眠完成后，再给这货一次机会，不行就抛错退出程序
                r.set("ip2", j)
            startk=1
        try:
            # 记录当前的ip1
            r.set("ip1", i)
        except:
            print("记录ip1出错，3600s后继续")
            time.sleep(3600)
            # 同样，睡眠完成后，再给这货一次机会，不行就抛错退出程序
            r.set("ip1", i)
        startj=1


push_ip_port()