import requests

headers = {
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Connection: keep-alive
    Content-Length: 25
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Cookie: WEBTJ-ID=20190123003921-168766e377150a-0f301852ea953e-b781636-1327104-168766e3773837; _ga=GA1.2.518328921.1548175161; _gid=GA1.2.904648461.1548175161; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1548175161; user_trace_token=20190123003934-4cc8e2b6-1e64-11e9-918d-525400f775ce; LGSID=20190123003934-4cc8e6a0-1e64-11e9-918d-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E9%2592%25A9%25E7%25BD%2591%26oq%3Dpython%252520%2525E9%252598%25259F%2525E5%252588%252597%2525E5%252592%25258C%2525E6%2525A0%252588%26rsv_pq%3D9ed6a2b300018311%26rsv_t%3D397222o9wRYpG%252F%252FZrwDY6zwwsExJpmuVjHvSAHweRNtkrxi6vjrzRFubQME%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug2%3D0%26inputT%3D11013%26rsv_sug4%3D11012; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20190123003934-4cc8ea52-1e64-11e9-918d-525400f775ce; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168766ecce9478-0ab90786ba3c93-b781636-1327104-168766eccea6e6%22%2C%22%24device_id%22%3A%22168766ecce9478-0ab90786ba3c93-b781636-1327104-168766eccea6e6%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; JSESSIONID=ABAAABAAAIAACBIDA1EBE81BE43B709E7F31F848600248A; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; _gat=1; LGRID=20190123004617-3cfae958-1e65-11e9-918e-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1548175564; SEARCH_ID=a613b87cf96941deba0b85cfa57083a5
    Host: www.lagou.com
    Origin: https://www.lagou.com
    Referer: https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
    X-Anit-Forge-Code: 0
    X-Anit-Forge-Token: None
    X-Requested-With: "XMLHttpRequest",
}
def get_page(url,params,Session):
    # s.headers.update(headers)
    r = s.post(url,data=params)
    print(s.get(url,))
    # 得到返回的json 数据
    # json_data = r.json()
    # #得到总条数 
    # totalCount = json_data["content"]["positionResult"]["totalCount"]
    # # 每页显示的条数
    # pageSize = json_data["content"]["pageSize"]
    # # 计算总抓取的页数
    # pages = math.ceil(totalCount / pageSize) if math.ceil(totalCount / pageSize) < 30 else 30
    # get_info(url,pages,r)
    # print(r)
    # print(json_data)
    # exit()

if __name__ == "__main__":
    url = "https://www.lagou.com/jobs/positionAjax.json"
    params = {
        'first': 'true',
        'pn': '1',
        'kd': 'python',
    } 
    with requests.Session() as s:
        get_page(url,params,s)