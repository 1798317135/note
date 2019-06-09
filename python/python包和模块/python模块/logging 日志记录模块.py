######################### 简介

# 
# 1.0 他可以跟踪程序运行时所发生的事件，在代码中调用日志的某些方法来记录发生的事情。
# 2.0 一个事件可以用一个包含可选变量数据的消息来描述
# 3.0 事件有自己的等机性
# 
# ####################### 作用
# 
# 1.0 可以通过对log的分析来 了解程序的运行状况
# 2.0 丰富的log可以分析用户的操作行为，喜好，地域分布等等有用的信息
# 3.0 在一个应用中对log 进行多级区分，可以分析应用的健康状况，并且可以快速定位问题，加以处理
# 
# ###################### 使用
import logging
from logging import handlers
# 设置日志格式
# %(levelno)s：打印日志级别的数值
# %(levelname)s：打印日志级别的名称
# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s：打印当前执行程序名
# %(funcName)s：打印日志的当前函数
# %(lineno)d：打印日志的当前行号
# %(asctime)s：打印日志的时间
# %(thread)d：打印线程ID
# %(threadName)s：打印线程名称
# %(process)d：打印进程ID
# %(message)s：打印日志信息
# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# --- 参数
# filename：指定日志文件名；
# filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
# format：指定输出的格式和内容，format可以输出很多有用的信息，
# datefmt：指定时间格式，同time.strftime()；
# level：设置日志级别，默认为logging.WARNNING；
# stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，
#         默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；

# ********** 初始化日志对象
logger = logging.getLogger(__name__)

# 控制台输入日志
# 日志等级以此为
# debug、info、warning、error以及critical
# ------------------------------------- addHandler
# logging 日志处理的对象 通过addHandler 添加
# logging中包含的handler主要有如下几种:
# 
# 
# handler名称：位置；作用
# StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
# FileHandler：logging.FileHandler；日志输出到文件
# BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
# RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
# TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
# SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
# DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
# SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
# SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
# NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
# MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
# HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器
# 
# ********* 把日志写入文件
# 1.0 创建一个文件句柄
handler = logging.FileHandler("./log.txt")
# 2.0 设置日志级别
handler.setLevel(level = logging.DEBUG)
# 3.0 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# 4.0 添加到logger对象里面
logger.addHandler(handler)

# ********* 把日同时输出屏幕
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)


# ********* 日志回滚
# 日志的回滚方式大致有两种:
# --- 1.0 
#       按照大小回滚RotatingFileHandler基于文件大小切分
#       handlers.RotatingFileHandler 
#       
# # 写入文件，如果文件超过1024KB，仅保留3个文件。 
# loger = handlers.RotatingFileHandler("./log.txt.1", mode = "a", maxBytes = 1024, backupCount = 3, encoding = "utf-8", delay = 1)

# --- 2.0 
#       按时间回滚
#       按照时间回滚（就是按时间分割日志，并且限制日志文件的个数，删除早期的日志）
#       使用TimedRotatingFileHandler
#       对log，通常有一种想要的效果：log按天切分，每天一个log文件，保留三天内的log，过期删除。
        # TimedRotatingFileHandler(filename [,when [,interval [,backupCount]]])
        # filename 是输出日志文件名的前缀，比如log/myapp.log
        # when 是一个字符串的定义如下：
        # “S”: Seconds
        # “M”: Minutes
        # “H”: Hours
        # “D”: Days
        # “W”: Week day (0=Monday)
        # “midnight”: Roll over at midnight
        # interval 是指等待多少个单位when的时间后，Logger会自动重建文件，当然，这个文件的创建
        # 取决于filename+suffix，若这个文件跟之前的文件有重名，则会自动覆盖掉以前的文件，所以
        # 有些情况suffix要定义的不能因为when而重复。
        # backupCount 是保留日志个数。默认的0是不会自动删除掉日志。若设3，则在文件的创建过程中
        # 库会判断是否有超过这个3，若超过，则会从最先创建的开始删除。
# timefilehandler = handlers.TimedRotatingFileHandler("./log.log", when = "S", interval = 30, backupCount = 3 , encoding = "utf-8")
# timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
# timefilehandler.setLevel(logging.INFO)
# timefilehandler.setFormatter(formatter)
# logger.addHandler(timefilehandler)
#    
# ********* 输出到邮件
# email = handlers.SMTPHandler(
#     mailhost=('smtp.163.com',25),
#     fromaddr = "y1798317135@163.com", 
#     toaddrs = "760008395@qq.com", 
#     subject = "你好", 
#     credentials = ("y1798317135@163.com","a123456"),
#     timeout = 5,
#     )
# logger.addHandler(email)

if __name__ == '__main__':

###############################  日志等级：使用范围

# FATAL：致命错误
# CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
# ERROR：发生错误时，如IO操作失败或者连接问题
# WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误
# INFO：处理请求或者状态变化等日常事务
# DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态
    # try:
    #     a = 1 / 0
    # except Exception as e:
    #     logger.error(e)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")


