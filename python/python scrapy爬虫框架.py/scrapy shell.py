 # ######################## 命令参数
#  --- 创建一个项目
# scrapy startobject object
# 
#  --- 创建一个爬虫
#  scrapy genspider test "baidu.com"
#  
 # --- 将结果导出
 # scrapy crawl quotes -o quotes.json
 # 
 # --- 传递参数
 # scrapy crawl test -a search=python
 # 然后我们在爬虫中接收设个参数,运用在爬虫中
 # search = getattr(self,"search",None)
 # 
 # ######################### shell
 # 配置shell解释器
 # 
 # scrapy.cfg 
 # setting
 # shell = ipython #默认是ipyton 
 # 
 # --- 启动shell
 # scrapy shell <url>
 # 
 # --- shleip() 查看命令
 # 
 # --- fetch(url) fetch(requset) 可以重新请求新的地址 更新所有对象
 # 
 # --- view(response) 打开浏览器
 # 
 # 
 # ######################## 用shell 检查蜘蛛respons
 for "aa" in respons.url:
    from scrapy.shell import inspect_response
    inspect_response(response,self)
 # 原理是我们把每个url的 response传递给 from scrapy.shell import inspect_response 这个方法
 # 然后 当这个蜘蛛爬行的时候 会进入shell 
 # 我们可以在shell 中 调试 和 检测以下 或者 在浏览器打开看一下 view(respons) 如果没有问题的话
 # ctrl + z 退出shell 继续爬行
 # 