import re
import asyncio
import aiohttp
import json

# 百度接口1
def baidu_API_1(r):
    data = {"source": "opendata.baidu.com"}
    status = 0
    msg = ""
    json_data = json.loads(r)
    if json_data['status'] == '0':
        res = {}
        for line in json_data['data']:
            res.update(line)
        status = 1
        data = {"source": "opendata.baidu.com","location": res['location']}
    return {"status": status,"msg": msg,"data": data}

# 百度接口2
def baidu_API_2(r):
    data = {"source": "sp0.baidu.com"}
    status = 0
    msg = ""
    json_data = json.loads(r)
    if json_data['status'] == '0':
        res = {}
        for line in json_data['data']:
            res.update(line)
        status = 1
        data = {"source": "sp0.baidu.com","location": res['location']}
    return {"status": status, "msg": msg, "data": data}

# ipip.net 接口1
def ipip_API_1(r):
    data = {"source": "freeapi.ipip.net"}
    status = 0
    msg = ""
    json_data = json.loads(r)
    if json_data != 'not found':
        str = json_data[0] + ' ' + json_data[1] + ' ' + json_data[2] + ' ' + \
            json_data[3] + ' ' + json_data[4]
        status = 1
        data = {"source": "freeapi.ipip.net", "location": str}
    return {"status": status, "msg": msg, "data": data}

# ipip.net 接口2
def ipip_API_2(r):
    data = {"source": "clientapi.ipip.net"}
    status = 0
    msg = ""
    json_data = json.loads(r)
    if json_data['ret'] == 'ok':
        str = json_data['data'][0] + ' ' + json_data['data'][1] + ' ' + json_data['data'][2] + ' ' + \
            json_data['data'][3] + ' ' + json_data['data'][4]
        status = 1
        data = {"source": "clientapi.ipip.net", "location": str}
    return {"status": status, "msg": msg, "data": data}

# ipip.net 接口3
def ipip_API_3(r):
    status = 1
    msg = ""
    json_data = json.loads(r)
    str = json_data['area'].replace('\t',' ')
    data = {"source": "btapi.ipip.net", "location": str}
    return {"status": status, "msg": msg, "data": data}

# 纯真IP数据库 接口
def chunzhen_API(r):
    status = 1
    msg = ""
    Str = r[11:-2]
    count = 0
    str = ''
    for ch in Str:
        if count == 3:
            str = str + ch
        if ch == "\'":
            count = count + 1
        elif count == 4:
            str = str[:-1]
            break
    data = {"source": "ip.cz88.net", "location": str}
    return {"status": status, "msg": msg, "data": data}

# ip138 网页版
def ip138_API(r):
    status = 1
    msg = ""
    text = r
    result_list = re.findall(r"(?<=<li>).*?(?=</li>)", text)
    str = result_list[0][5:]
    data = {"source": "www.ip138.com", "location": str}
    return {"status": status, "msg": msg, "data": data}

# 淘宝接口
def taobao_API(r):
    data = {"source": "ip.taobao.com"}
    status = 0
    msg = ""
    json_data = json.loads(r)
    if json_data['code'] == 0:
        res = json_data['data']
        status = 1
        str = res['country']+' '+ res['area']+' '+res['region']+' '+res['city']+' '+res['county']+' '+res['isp']
        data = {"source": "ip.taobao.com", "location": str}
    return {"status": status, "msg": msg, "data": data}

async def fetch_async(url,params,timeout,headers,API):
    async with aiohttp.ClientSession() as session:  #协程嵌套，只需要处理最外层协程即可fetch_async
        try:
            async with session.get(url,params=params,timeout=timeout,headers=headers) as resp:
                reponse = await resp.text()#因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async
                return API,reponse
        except:
            print(API)
            return API,"API访问错误"

def Query(ip_):
    URL = ['http://opendata.baidu.com/api.php?co=&resource_id=6006&t=1433920989928&ie=utf8&oe=utf-8&format=json',
           'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?co=&resource_id=6006&t=1433920989928&ie=utf8&oe=utf-8&format=json',
           'http://freeapi.ipip.net/' + ip_,
           'https://clientapi.ipip.net/free/ip?lang=CN',
           'https://btapi.ipip.net/host/info?host=Router&lang=CN',
           'http://ip.cz88.net/data.php',
           'http://www.ip138.com/ips138.asp?action=2',
           'http://ip.taobao.com/service/getIpInfo.php',
           ]
    API = ["baidu_1", "baidu_2", "ipip_1", "ipip_2", "ipip_3", "chunzhen", "ip138", "taobao"]
    API_funation = {"baidu_1": baidu_API_1, "baidu_2": baidu_API_2, "ipip_1": ipip_API_1, "ipip_2": ipip_API_2,
                    "ipip_3": ipip_API_3, "chunzhen": chunzhen_API, "ip138": ip138_API, "taobao": taobao_API}
    tasks = [fetch_async(URL[0], {"query": ip_}, 2, {}, API[0]),
             fetch_async(URL[1], {"query": ip_}, 2, {}, API[1]),
             fetch_async(URL[2], {}, 2, {}, API[2]),
             fetch_async(URL[3], {"ip": ip_}, 2, {'User-Agent': 'BestTrace/Windows V3.7.3'}, API[3]),
             fetch_async(URL[4], {"ip": ip_}, 2, {}, API[4]),
             fetch_async(URL[5], {"ip": ip_}, 2, {}, API[5]),
             fetch_async(URL[6], {"ip": ip_}, 2, {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3887.7 Safari/537.36'},API[6]),
             fetch_async(URL[7], {"ip": ip_}, 1, {}, API[7]),
             ]
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    #event_loop = asyncio.get_event_loop()
    results = event_loop.run_until_complete(asyncio.gather(*tasks))
    flag = 0
    data = []
    for num in results:
        if num[1] == "API访问错误":
            continue
        api_ = API_funation[num[0]](num[1])
        if api_['status'] == 0:
            continue
        flag = 1
        data.append(api_["data"])
        print(api_)
    if flag == 0:
        return {"source": -1, "msg": "访问API出错"}
    else:
        return {"source": 0, "msg": "", "data": data}