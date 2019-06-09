########################### 爬虫的五部曲
# 
# 第一步 
#    url队列
# 
# 第二部
#     访问url队列，请求responese 数据
# 
# 第三步
#       从response提取数据
#       
#       他提取的数据分为两种
#       第一种：提取数据，把这些数据写入数据队列
#       第二种：提取url，然后把这些url 放入第一步的url队列当中
# 
# 第四部
#       数据队列的 管理
#  
# 第五步
#       把数据队列种的数据储存起来
#
#
#
################################### scripy爬虫工作流程
#
# requsets 加上 selenium 可以完成百分之九十 网页的爬取
# 但是效率低,多线程爬虫的话比较复杂，许多代码需要自己实现,效率比较低
# 而scrapy框架就为我们提供 高效率 简单的爬虫框架，他基本实现了 大部分功能
# 我们只需要写少量代码就可以完成 复杂数据的爬取,所以在项目种 一般使用scrapy框架
# 来爬取网页数据
#   
# ******************** scrapy的构成
# scrapy框架由 
# --- Scheduler(调度器)
#    相当于url队列用于储存url
#    他返回一个requests对象
#    他由scrapy已经实现
#    
# --- Scrapy Engine(引擎)
#    它负责调度这几个模块的数据的调度
#    他由scrapy已经实现
#    
# --- Downloader Middleware(下载器中间件)
#    由于他的位置
#    他可以对引擎提交给Downloader的request对象进行过滤和处理
#    也可以对Downloader交给引擎的response对象进行过滤和处理
#    他一般不需要自己写 ，除非我们过滤某些特殊的数据
#    
# ----Downloader(下载器) 
#    用于请求url生成response 对象
#    他由scrapy已经实现
#    
# --- Spider Middleware(爬虫中间件)
#     由于他的位置
#     他可以对引擎交给spider的response对象进行过滤和处理
#     他也可以对spider提取的url后包装的requests对象进行过滤和处理
#     他一般不需要自己写，除非我们过滤某些特殊的数据
#     
# --- Spiders(爬虫)
#      他用户提取数据 和 url
#      提取的数据直接交给item Pipeline管道提取到的数据也会通过Spider Middleware 
#      但是他的过滤和处理不会在这里进行 Item Pipeline是专门处理这些数据的
#      提取的url包装 会通过 Spider Middleware 提交给引擎 然后 让引擎体提交给 Scheduler 调度器
#      他需要我们自己实现
#      
# --- item Pipeline(项目管道)
#     他相当于 数据队列
#     他用于处理 提取到的数据，然后顾虑和储存
#     他需要我们自己实现
#     
# 这七个部分组成，我们需要自己写的有 spider爬虫  和 Item Pipeline 项目管道 所以很简单
# 
# ********************** 大致流程
  # scrapy机几个模块都不是相互关联的  他们都是由 Engine引擎 来调度 他们的执行顺序
  # 
# 第一步由 Scheduler调度器 把 url队列包装成 requests 对象 发送给 引擎
# 第二部 由Engine 引擎 把request对象 通过 Downloader Middleware 下载器中间件 然后交给 Downloader 下载器
#第三步 由 Downloader下载器把返回的responese 对象在通过 Downloader Middleware 下载器中间件提交给引擎
# 第四部 由 引擎通过 Spider Middleware 爬虫中间件把 response对象提交给 Spider爬虫 模块
# 第五步 Spider模块提取 response对象的url 用scrapy.Request() 包装成 request对象 通过 Spider Middleware爬虫中间件提交给 引擎 再有引擎提交给Schedulerd调度器
#       把提取的数据 提交给 引擎然后在提交给 item Pipeline项目管道 
#       
# 第六步 由项目管道 处理数据和储存数据
# 
# 
# 
# ##################################### scrapy的使用流程
#
# 1.0 创建一个scrapy 项目
    scrapy startproject xxx

# 2.0 生成一个爬虫

    scrapy genspider 爬虫名字 "url地址"


     