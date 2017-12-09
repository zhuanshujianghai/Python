#从redis拉取代理
from redis import Redis
import telnetlib
import pymysql
import time
#检查代理ip是否可用
def checkip(ip,port):
    try:
        tn = telnetlib.Telnet(ip, port=port, timeout=1)
    except:
        return False
    else:
        return True

def insert(ip,port,ipport):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", db="httpip")
    sql = "insert into realip(ip,port,ipport) values('" + ip + "','" + port + "','" + ipport + "')"
    try:
        conn.query(sql)
    except:
        print("往mysql中插入数据出错")
    conn.close()

#查询realip中指定数据是否存在，返回条数
def queryCount(ip,port):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", db="httpip")
    try:
        cur = conn.cursor()
        sql = "select * from realip where ip='" + ip + "' and port='"+port+"'"
        cur.execute(sql)
        result = cur.fetchall()
    except:
        print("从mysql中查询数据出错")
    conn.close()
    return len(result)

def pull_check_ip_port():
    r = Redis(host="你的IP", port=6379, password="你的密码")
    while (r.llen("proxy")>0):
        try:
            proxy = r.lpop("proxy").decode("utf-8")
            ip = proxy.split(':')[0]
            port = proxy.split(':')[1]
            count = queryCount(ip, port)
            if (count > 0):
                print("数据库已存在该数据：" + proxy)
            else:
                bool = checkip(ip, port)
                if bool:
                    insert(ip, port, proxy)
                    print("***********成功的proxy" + proxy + "***************")
                else:
                    print("失败的proxy" + proxy)
        except:
            print("出现错误,等待2s后继续")
            time.sleep(2)

pull_check_ip_port()
