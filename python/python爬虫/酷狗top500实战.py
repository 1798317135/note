import time,requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
mydb = MongoClient()
mycol = mydb.kugou.top500
payload = {
    "from":"rank",
}

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    }
def get_info(url):
    r = requests.get(url,params=payload,headers = headers)
    soup = BeautifulSoup(r.text,'lxml')
    ranks = soup.select(".pc_temp_num")
    titles = soup.select(".pc_temp_songlist > ul > li > a")
    times = soup.select(".pc_temp_time")
    for rank,title,time in zip(ranks,titles,times):
        data = {
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0].strip(),
            'song':title.get_text().split('-')[1].strip(),
            'time':time.get_text().strip(),
        }
        # song_id = mycol.insert(data)
        print(data)
if __name__ == "__main__":
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html".format(str(i)) for i in range(1,2)]
    for url in urls:
        get_info(url)
        time.sleep(1)