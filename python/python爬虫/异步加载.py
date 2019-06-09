import requests,re
from bs4 import BeautifulSoup
headers = {
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01.2.588189374.1544018174; _fbp=fb.1.1544018183994.289803915; __cfduid=d35e35d1d713ff851a6dbf22d031c75011544018418",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    }
# https://images.pexels.com/photos/1298601/pexels-photo-1298601.jpeg?
def get_info(url):
    photos = list()
    r = requests.get(url,headers = headers)
    soup = BeautifulSoup(r.text,'lxml')
    imgs = soup.select("article.photo-item > a:nth-of-type(1) > img")
    srcs = []
    for img in imgs:
        src = img.get('src')
        srcs.append(src)
    return srcs

if __name__ == "__main__":
    urls = ["https://www.pexels.com/?page={}".format(i) for i in range(3,4)]
    for url in urls:
        srcs = get_info(url)
    path = 'c:/Users/17983/Desktop/img/'
    
    for src in srcs:
        fileName = re.findall(r'\d\/(.*?)\?',src)
        r = requests.get(src,headers = headers)
        with open(path+fileName[0],"wb") as p:
            p.write(r.content)
        # print(src,fileName[0])

