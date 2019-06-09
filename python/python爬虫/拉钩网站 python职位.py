import time
import requests
import json
# 设置请求头
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01', 
    'Accept-Encoding': 'gzip, deflate, br', 
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 
    'Cache-Control': 'no-cache', 
    'Connection': 'keep-alive', 
    'Content-Length': '26', 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
    'cookie':'JSESSIONID=ABAAABAABEEAAJA8DAEC604114BF306F303F1DB8C8755E6; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555259294; _ga=GA1.2.509022552.1555259294; _gat=1; user_trace_token=20190415002813-4c6fd4a9-5ed2-11e9-9373-5254005c3644; LGSID=20190415002813-4c6fd6e1-5ed2-11e9-9373-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190415002813-4c6fd8f2-5ed2-11e9-9373-5254005c3644; _gid=GA1.2.658702669.1555259294; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=7cecc84af077f0130039525551e1a4db8d8433a73c; LGRID=20190415002820-50b453f2-5ed2-11e9-8570-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555259301; SEARCH_ID=330dfd422f4f4074a7f0440bd009705f',
    'Host': 'www.lagou.com', 
    'Origin': 'https://www.lagou.com', 
    'Pragma': 'no-cache', 
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=', 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36', 'X-Anit-Forge-Code': '0', 'X-Anit-Forge-Token': 'None', 'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

url = "https://www.lagou.com/jobs/positionAjax.json"
def get_page(data):
    response = requests.post(url = url,data = data,headers=headers)
    response.encoding = "utf-8"
    get_data(response.json())
    # with open("lagou.json","w",encoding="utf-8") as f:
    #     f.write(response.text)

def get_data(data):
    
    data["content"]["hrInfoMap"].keys()[url]
        

if __name__ == "__main__":
    data = {
    "first":"true",
    "pn": "1",
    "kd":"python"
    }
    get_page(data)

