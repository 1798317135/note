# ###########################  创建一个新的Scrapy项目 ###########################
# 
# --- 1.0 在开始抓取之前，您必须设置一个新的Scrapy项目
scrapy startproject projectName

# --- 2.0 项目文件目录
tutorial/
    scrapy.cfg            # 部署配置文件

    tutorial/             # 项目的Python模块，您将从这里导入您的代码
        __init__.py

        items.py          # 项目配置文件

        middlewares.py    # 项目中间文件

        pipelines.py      # 项目管道文件

        settings.py       # 项目设置文件

        spiders/          # 爬行器械目录
            __init__.py

# --- 3.0 生成一个爬虫

scrapy genspider 名称 "地址"
# 
# ########################### 编写蜘蛛来抓取网站并提取数据 #######################
# 
import scrapy
class QuotesSpider(scrapy.Spider):
    # name 识别蜘蛛。它在项目中必须是唯一的，也就是说，您不能为不同的Spiders设置相同的名称。
    name = "quotes"
    # start_requests()：必须返回Spider将开始爬行的可迭代请求（您可以返回请求列表或编写生成器函数）。
    # 后续请求将从这些初始请求中连续生成。
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # parse将调用一个方法来处理为每个请求下载的响应。响应参数是TextResponse保存页面内容的实例，
    # 并具有处理它的其他有用方法。
    # 该parse()方法通常解析响应，将抽取的数据提取为dicts，
    # 并查找要遵循的新URL并Request从中创建新的request（）。
    def parse(self, response):
        page = response.url
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        self.log(page)
# 
# ########################### 使用命令行导出已删除的数据 #######################
# 
# --- 运行爬虫
#     scrapy crawl 爬虫名称
#     
# --- scrapy shell 可以更方便数据提取
scrapy shell 'url'

# --- 然后得到一个响应对象response对象，我们可以从这个对象中提取数据
# --- css()选择器
#     返回一个列表，我们可以对这个列表进一步的筛选
#     extract()可以获得指定的全部元素
#     如果只想取里列表当中的第一个就使用extract_frist()
#     元素::text 可以获取这个标签里面的文字
#     元素::Attr("属性") 可以获取标签属性
response.css("css元素::text").extract()
response.css("css元素::arrt('id')").extract_first()
# --- re()可以使用正则
response.css("title::text").re(r"正则表达式")

# --- 储存爬取的内容
#     第二种格式可以累加
#     第一种如果第二次储存会返回一个错误的json文档
        scrapy crawl quotes -o quotes.json
        scrapy crawl quotes -o test1.jl
        scrapy crawl quotes -o test1.jl -a 传递参数


# ###########################改变蜘蛛以递归方式跟随链接 ########################
# 
# 
# 
# ########################## 使用蜘蛛参数 ####################################