# ###requests版本API调用
#
# import requests
# import re
#
# # 百度接口1
# def baidu_API_1(ip_):
#     data = {"source": "opendata.baidu.com"}
#     status = 0
#     msg = ""
#     timeout = 2
#     URL = "http://opendata.baidu.com/api.php?query=" + ip_ + "&co=&resource_id=6006&t=1433920989928&ie=utf8&oe=utf-8&format=json"
#     try:
#         r = requests.get(URL, timeout=timeout)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         try:
#             json_data = r.json()
#         except:
#             msg = "返回格式错误"
#         else:
#             if json_data['status'] == '0':
#                 res = {}
#                 for line in json_data['data']:
#                     res.update(line)
#                 status = 1
#                 data = {"source": "opendata.baidu.com","location": res['location']}
#     return {"status": status,"msg": msg,"data": data}
#
# # 百度接口2
# def baidu_API_2(ip_):
#     data = {"source": "sp0.baidu.com"}
#     status = 0
#     msg = ""
#     timeout = 2
#     URL = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=' + ip_ + '&co=&resource_id=6006&t=1433920989928&ie=utf8&oe=utf-8&format=json'
#     try:
#         r = requests.get(URL, timeout=timeout)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         try:
#             json_data = r.json()
#         except:
#             msg = "返回格式错误"
#         else:
#             if json_data['status'] == '0':
#                 res = {}
#                 for line in json_data['data']:
#                     res.update(line)
#                 status = 1
#                 data = {"source": "sp0.baidu.com","location": res['location']}
#     return {"status": status, "msg": msg, "data": data}
#
# # ipip.net 接口1
# def ipip_API_1(ip_):
#     data = {"source": "freeapi.ipip.net"}
#     status = 0
#     msg = ""
#     timeout = 2
#     URL = 'http://freeapi.ipip.net/' + ip_
#     try:
#         r = requests.get(URL, timeout=timeout)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         try:
#             json_data = r.json()
#         except:
#             msg = "返回格式错误"
#         else:
#             if json_data != 'not found':
#                 str = json_data[0] + ' ' + json_data[1] + ' ' + json_data[2] + ' ' + \
#                       json_data[3] + ' ' + json_data[4]
#                 status = 1
#                 data = {"source": "freeapi.ipip.net", "location": str}
#     return {"status": status, "msg": msg, "data": data}
#
# # ipip.net 接口2
# def ipip_API_2(ip_):
#     data = {"source": "clientapi.ipip.net"}
#     status = 0
#     msg = ""
#     timeout = 2
#     headers = {'user-agent': 'BestTrace/Windows V3.7.3'}
#     URL = 'https://clientapi.ipip.net/free/ip?ip=' + ip_ + '&lang=CN'
#     try:
#         r = requests.get(URL, timeout=timeout, headers=headers)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         try:
#             json_data = r.json()
#         except:
#             msg = "返回格式错误"
#         else:
#             if json_data['ret'] == 'ok':
#                 str = json_data['data'][0] + ' ' + json_data['data'][1] + ' ' + json_data['data'][2] + ' ' + \
#                       json_data['data'][3] + ' ' + json_data['data'][4]
#                 status = 1
#                 data = {"source": "clientapi.ipip.net", "location": str}
#     return {"status": status, "msg": msg, "data": data}
#
# # ipip.net 接口3
# def ipip_API_3(ip_):
#     data = {"source": "btapi.ipip.net"}
#     status = 0
#     msg = ""
#     timeout = 2
#     URL = 'https://btapi.ipip.net/host/info?ip=' + ip_ + '&host=Router&lang=CN'
#     try:
#         r = requests.get(URL, timeout=timeout)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         try:
#             json_data = r.json()
#         except:
#             msg = "返回格式错误"
#         else:
#             str = json_data['area'].replace('\t',' ')
#             status = 1
#             data = {"source": "btapi.ipip.net", "location": str}
#     return {"status": status, "msg": msg, "data": data}
#
# # 纯真IP数据库 接口
# def chunzhen_API(ip_):
#     data = {"source": "ip.cz88.net"}
#     status = 0
#     msg = ""
#     timeout = 2
#     URL = 'http://ip.cz88.net/data.php?ip=' + ip_
#     try:
#         r = requests.get(URL, timeout=timeout)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         Str = r.text
#         Str = Str[11:-2]
#         count = 0
#         str = ''
#         for ch in Str:
#             if count == 3:
#                 str = str + ch
#             if ch == "\'":
#                 count = count + 1
#             elif count == 4:
#                 str = str[:-1]
#                 break
#         status = 1
#         data = {"source": "ip.cz88.net", "location": str}
#     return {"status": status, "msg": msg, "data": data}
#
# # ip138 网页版
# def ip138_API(ip_):
#     data = {"source": "www.ip138.com"}
#     status = 0
#     msg = ""
#     timeout = 2
#     URL = 'http://www.ip138.com/ips138.asp?ip=' + ip_ + '&action=2'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3887.7 Safari/537.36'
#     }
#     try:
#         r = requests.get(URL, timeout=timeout,headers = headers)
#         r.encoding = 'gb2312'
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         text = r.text
#         result_list = re.findall(r"(?<=<li>).*?(?=</li>)", text)
#         str = result_list[0][5:]
#         status = 1
#         data = {"source": "www.ip138.com", "location": str}
#     return {"status": status, "msg": msg, "data": data}
#
# # 淘宝接口
# def taobao_API(ip_):
#     data = {"source": "ip.taobao.com"}
#     status = 0
#     msg = ""
#     timeout = 1
#     URL = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip_
#     try:
#         r = requests.get(URL, timeout=timeout)
#     except requests.RequestException as E:
#         msg = "访问超时"
#     else:
#         try:
#             json_data = r.json()
#         except:
#             msg = "返回格式错误"
#         else:
#             try:
#                 json_data = r.json()
#             except:
#                 msg = "返回格式错误"
#             else:
#                 if json_data['code'] == 0:
#                     res = json_data['data']
#                     status = 1
#                     str = res['country']+' '+ res['area']+' '+res['region']+' '+res['city']+' '+res['county']+' '+res['isp']
#                     data = {"source": "ip.taobao.com", "location": str}
#         return {"status": status, "msg": msg, "data": data}
#
# def Query(ip_):
#     flag = 0
#     data = []
#     API = {"baidu_1","baidu_2","ipip_1","ipip_2","ipip_3","chunzhen","ip138","taobao"}
#     API_funation = {"baidu_1": baidu_API_1,"baidu_2": baidu_API_2,"ipip_1": ipip_API_1,"ipip_2": ipip_API_2,
#            "ipip_3": ipip_API_3,"chunzhen": chunzhen_API,"ip138": ip138_API,"taobao": taobao_API}
#     for num in API:
#         api_ = API_funation[num](ip_)
#         if api_["status"] == 1:
#             flag = 1
#             data.append(api_["data"])
#         else:
#             print(api_)
#
#     if flag == 0:
#         return {"source": -1,"msg": "访问API出错"}
#     else:
#         return {"source": 0, "msg": "", "data": data}