# ######################## pipline 项目管道
# 
# 1.0 scripy 当中的pipline 用来处理提取的数据
# 2.0 pipline 可以负责数据的过滤和存储
#   
# ###################### pipline 的使用原理
# 
# 如果需要使用初始化的scripy项目需要使用pipline模块
# 我们需要到 setting.py 里面设置把他的注释打开
# 我们也可以自己创建多个piplne类
# myspider.pipelines.新定义的pipline名子 : 权重
# 当权重数值越小 权重越高 优先级越高 

 # ITEM_PIPELINES = {
 #   # 'myspider.pipelines.MyspiderPipeline': 300,
 #   # 'myspider.pipelines.MyspiderPipeline1': 299,
# }
#
#
######################pipline 详解
#
# 1.0 pipline在 spider 文件夹下的 piplines.py
# 2.0 爬取的数据通过 Request, BaseItem, dict ,None 这四种类型的数据返回时
#     这些数据会被pipline模块的MyspiderPipeline类的 process_iteme 接收
#     
#     --- item 代表接收的数据
#     --- spider 代表接收爬虫的类
#         我们可以通过这类的name 类属性来判断接收的是哪个爬虫的数据
#     --- return 然后把这个return下一个优先级的 pipine里面 处理以此类推




################### 自己编写item piplines
#
# 没个项目管道必须实现process_item这个方法 
# process_item（self,item,spider）

# 还可以实现下面三种方法
# 
# --- 打开蜘蛛会执行这个方法
# open_spider（self,spider）
# 
# --- 当蜘蛛关闭会执行这个方法
# close_spider(self,spider)
#
# ---
# from_crawler(cls,crawler)
# 
# 