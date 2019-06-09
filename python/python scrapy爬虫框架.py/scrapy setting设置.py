############################### 设置的优先级
# scrapy的优先级，
# 优先级高的设置会覆盖优先级低的设置参数
# 1.0 命令行的设置
# 2.0 每个蜘蛛内部单独的设置
# 3.0 项目设置的模块
# 4.0 每个命令的默认设置
# 5.0 默认的全局设置
# 
# 
# ************* 命令行的设置
# 优先级最高 用-s 或者 --set 选项来覆盖一个或者多个设置 -s 后面岱庙设置的选项
#  scrapy crawl myspider -s LOG_FILE = scrapy.log 
#  
#
#************** 每个蜘蛛单独的设置
# 
# 每个蜘蛛可以单独自定义设置
# 通过custom_settings 设个属性来设置
# class Myspider(scrapy.spider):
#     name = "myspider"
#     custom_settings = {
#         "LOG_LEVEL":"WARNING",
#     }
# 
# 
#************** 项目的设置模块
# 每个scrapy项目都有一个标准的setting.py 模块
# 他是标准的设置模块，通常就在设个模块当中设置
# 
# 
# ************ 默认的全局设置
# 默认的全局设置位于scrapy.setting.defaul_settings模块中
# 
#  
#   
#    
# 
# ###################################### 访问设置
# 
# 通过 self.settings 来获得
# 
# ##################################### 常用的设置
# 
# 
# ************* log日志设置
#  可以荣logging模块来设置日志格式和触发相应级别的日志
 import logging
 # 1.0 设置日志格式
 logging.basicConfig()

 # 2.0 创建日志对象
 logger = logging.getLogger(__name__)

 # 3.0 触发日志 先要设置scrapy的日志触发级别
 logger.debug("debug")
 logger.info("info")
 logger.warning("warning")
 logger.error("error")
 logger.critical("critical")

#  设置日志级别，只要大于等于设置日志的级别，才会触发日志
# "LOG_LEVEL" = "DEBUG" 
# 
# 把触发的日志储存到本地文件的路径
# "LOG_FILE" = "./log.log"
# 
