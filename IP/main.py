import legitimacy
import IP_query
import config
import web
import json
import time

urls = (
    #今日查询数量接口
    "/api/todaynum", "todaynum",
    #IP查询文档
    "/api/ip", "ip",
)
app = web.application(urls, globals())

class todaynum:
    def GET(self):
        Time = time.strftime("%D")
        JSONDATA = config.config_QUERY(Time)
        return json.dumps(JSONDATA)

class ip:
    def POST(self):
        data = web.data()
        ip_ = json.loads(data)
        print(ip_)
        if legitimacy.check_ip(ip_["ip"]) == False:
            JSONDATA = {"status": -1, "msg": "ip不合法"}
            return json.dumps(JSONDATA)
        else:
            Time = time.strftime("%D")
            config_Data = config.config_ADD(Time)
            if  config_Data == True:
                JSONDATA = IP_query.Query(ip_["ip"])
                return json.dumps(JSONDATA)
            else:
                return config_Data

if __name__ == "__main__":
    app.run()
