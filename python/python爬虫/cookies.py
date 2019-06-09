import requests
url = "https://www.douban.com/"
headers = {
    'Cookie': 'll="118240"; bid=LoO4Ktn3dvU; __utmc=30149280; __utmz=30149280.1544068210.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544074240%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DXJZM2vtBsUkt0V0z-iaP_wX_TKn1mgFcX6EOrwHpomKQ8XLtKv6JAv4oSICD2cOX%26wd%3D%26eqid%3Daa923e1c00012f94000000045c089c6c%22%5D; __utma=30149280.1643473203.1544068210.1544068210.1544074242.2; ps=y; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18832; __yadk_uid=VhwxSBZpRggViSjDcd68LLeKQtZShc3X; _ga=GA1.2.1643473203.1544068210; _gid=GA1.2.1954241726.1544074795; ue="760008395@qq.com"; dbcl2="188322688:4bRWPJvXtEk"; ck=CEX1; _pk_id.100001.8cb4=bce86cce6a0bbfff.1544068208.2.1544076812.1544068253.',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
with requests.Session() as s:
    s.headers = headers
    r = s.get(url)
    print(r.text)