from multiprocessing import Pool
import re,time
import requests

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}

# 爬虫函数
def get_info(url):
    r = requests.get(url,headers = headers)
    names = re.findall(r"<h2>(.*?)</h2>",r.text,re.S)
    contents = re.findall(r'<div class="content">.*?<span>(.*?)</span>',r.text,re.S|re.I)
    laughs = re.findall(r'<span class="stats-vote">.*?(\d+)</i> 好笑</span>',r.text,re.S|re.I)
    comments = re.findall(r'<i class="number">(\d+)</i> 评论',r.text,re.S|re.I)
    arr = []
    for name,content,laugh,comment in zip(names,contents,laughs,contents):
        data = {
            'name':name.strip(),
            'content':content.strip(),
            'laugh':laugh.strip(),
            'comment':comment.strip(),
        }
        # print(data)
        arr.append(data)
    return arr
# 主模块
if __name__ == "__main__":
    # 获取全部的url集合
    urls = ["https://www.qiushibaike.com/8hr/page/{}".format(str(i)) for i in range(3,8)]
    # 串行
    start_time1 = time.time()
    for url in urls:
        get_info(url)
    end1 = time.time()
    print("串行时间",end1 - start_time1)
    # 开两个进程
    start2 = time.time()
    pool = Pool(processes = 2)
    pool.map(get_info,urls)
    end2 = time.time()
    print("2进程时间",end2 - start2)

    # 开四进程
    start3 = time.time()
    pool = Pool(processes=4)
    pool.map(get_info,urls)
    end3 = time.time()
    print("4进程时间",end3 - start3)