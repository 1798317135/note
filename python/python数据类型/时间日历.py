####################################### 时间常用的三大模块 ######################################
#
# ******************* time模块 *******************
# 
import time
# 
# --------------  时间戳 ----------------------

# 1.0 提供了处理事件和表示之间转换的功能
# 
# --- time()获取当前的时间戳
t = time.time()
print(time)
year = t / (24 * 60 * 60 * 365) + 1970
print(year)

# ----------------- 时间元组 --------------------
# 
#   
# --- time.localtime([seconds]) 默认是获取当前的事件元组,
# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
# 
local = time.localtime()
# --- 时间元组 格式
# 字段                属性             值
# 4位年数            tm_year         2018
# 月                 tm_mon          1到12
# 日                 tm_mday         1到31
# 小时                tm_hour        0到23
# 分钟                tm_min         0到59
# 秒                  tm_sec         0到61（60或61是润秒）
# 一周的第几日        tm_wday         0到6(0是周一)
# 一年的第几日        tm_yday         1到366,一年中的第几天
# 夏令时               tm_isdst       是否为夏令时，值为1时是夏令时，值为0时不是夏令时，默认为-1
# 
# 
# --- mktime(tuple_time)将时间元组转换为时间戳
print(time.mktime(local),"mktime()")

# -------------------- 格式化时间 -------------------------
# 
# --- time.ctime()时间戳转化为格式化事件
t = time.time()
result = time.ctime(t)
print(result,"ctime()")

# --- time.asctiome() 时间元组化为格式化事件
tuple_time = time.localtime()
result = time.asctime(tuple_time)
print(result,"asctime()")

# --------------------  格式化日期字符串 --------------------
# 
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
# 
# --- time.strftime(format[,tuple]) 把时间元组用格式字符 变为格式化字符串
#
tuple_time = time.localtime()
# --- %y 是表示后两位两个数的年  %Y 表示四个数的完整的年份
year = time.strftime("%Y",tuple_time)
# --- %m 月份（01-12）
mouth = time.strftime("%m",tuple_time)
# --- %d 月内中的一天 日（0-31）
day = time.strftime("%d",tuple_time)
# --- %k 星期
week = time.strftime("%w", tuple_time)
w = ["一","二","三","四","五","六","日"]
week = w[int(week)-1]
# %H 24小时制小时数（0-23）# %I 12小时制小时数（01-12）
hour = time.strftime("%H",tuple_time)
# %M 分钟数（00=59）
minute = time.strftime("%M",tuple_time)
# %S 秒（00-59）
second = time.strftime("%S", tuple_time)
print(year+"-"+mouth+"-"+day+"\t"+hour+":"+minute+":"+second+"\t星期"+week)

# =========================================================================
# # 
# # %a 本地简化星期名称
# week = time.strftime("%a", tuple_time)
# print(week)
# # %A 本地完整星期名称
# W = time.strftime("%A", tuple_time)
# print(W)
# # %b 本地简化的月份名称
# time.strftime("%b", tuple_time)
# # %B 本地完整的月份名称
# # %c 本地相应的日期表示和时间表示
# # %j 年内的一天（001-366）
# # %p 本地A.M.或P.M.的等价符
# # %U 一年中的星期数（00-53）星期天为星期的开始
# print(time.strftime("%U", tuple_time))
# # %w 星期（0-6），星期天为星期的开始
# print(time.strftime("%w", tuple_time))
# # %W 一年中的星期数（00-53）星期一为星期的开始
# # %x 本地相应的日期表示
# # %X 本地相应的时间表示
# # %Z 当前时区的名称
# # %% %号本身
# # 
# --------------------- 获取cpu时间  ------------------
# 
# 1.0 cpu 时间 可以知道程序的耗时时间
# 用结束的cpu时间 减去 开始的cpu时间 就得出 程序耗时时间
# 
start = time.clock()
# for x in range(1,2000):
#     print(x)
end = time.clock()
print(end - start,"运行时间")


# ----------------------- 休眠时间 --------------------
# 
# --- time.sleep(seconds) 推迟线程的运行时间 让程序暂停
# while True:
#     time.sleep(1)
#     print(time.ctime(time.time()))
#     

#
# ******************* calendar 模块 ******************
# 
import calendar

# 1.0 提供了与日历相关的功能 比如为给定的年份和月份打印文本日历功能
# 
# --- calendar.month(year,month)输出给定月份的 日历文本
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。
# 每行长度为21* W+18+2* C。l是每星期行数。
# 
# 
# print(calendar.month(2018,10))

#     October 2018
# Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31
# 
# --- calendar.calendar(theyear) 给定年份的全部日历文本
# print(calendar.calendar(2018))
#                                   2018

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
# 29 30 31                  26 27 28                  26 27 28 29 30 31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1          1  2  3  4  5  6                   1  2  3
#  2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
#  9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
# 16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
# 23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
# 30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                    1             1  2  3  4  5                      1  2
#  2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
#  9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
# 16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
# 23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
# 30 31

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                      1  2
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
# 29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
#                                                     31
#
# --- calendar.isleap()是闰年返回True，否则为false。
print(calendar.isleap(2018),"isleap()")

# --- calendar.leapdays()返回在两年之间的闰年总数，但不包括末年
print(calendar.leapdays(2016,2020),"leapdays()")
# 
# --- calendar.monthcalendar()返回一个整数的单层嵌套列表，每个子列表装载代表一个星期，月外的日期设为0
print(calendar.monthcalendar(2018,10))

# --- calendar.monthrange()返回两个整数，第一个为该月的首日的星期（0-6），第二个为该月的总天数
print(calendar.monthrange(2018,10),"monthrange()")

# --- calendar.weekday返回给定日期的星期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
print(calendar.weekday(2018,10,22))
#
# ******************* datetime模块 *****************
# 
import datetime

# 1.0 处理日期和时间的标准率

# 2.0 这个模块里面有datatime类 以及time类，可以做一些计算之类的操作
# 
# --- 获取当时的时间日期
# 
t = datetime.datetime.now()
print(t)
print(datetime.datetime.today())
print(t.year,"年")
print(t.month,"月")
print(t.day,"日")
print(t.weekday,"周")
print(t.hour,"时")
print(t.minute,"分钟")
print(t.second,"秒")

# --- datatime.timedelta() 时间增量 可以家计算给定时间增加后的时间
print(t + datetime.timedelta(days = 10))

# --- datetime.datetime(2014,9,1,0,0,0,0)
first = datetime.datetime(2014,9,1)
last = datetime.datetime(2018,10,22)
second = last - first
print(second,"天数")
print(second.total_seconds(),"秒数")
