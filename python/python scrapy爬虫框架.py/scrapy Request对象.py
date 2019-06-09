# 当scheduler 调度器传给 引擎的并不是url 
# 而是经过包装的Request对象
# 所以我们在spider提取得url 传给 引擎之前 需要包装成Request对象
 scrapy.Request(
    url,        # 传递得url
    callback,   # 指定一个回调函数，该回调函数以这个request是的response作为第一个参数。如果未指定callback,默认用parse()方法。
    method,     # HTTP请求的方法，默认为GET
    headers,    # 设置请求头
    body,       # 设置请求体
    cookies,    # (dict or dicts list):cookie有两种格式设置cookie
                # 当网站在response中返回cookie时，这些cookie将被保存以便未来的访问请求。这是常规浏览器的行为。如果你想避免合并当前
                # 正在使用的cookie,你可以通过设置Request.meta中的dont_merge_cookies为True来实现。
    meta,       # 设个方法可以将这个解析方得item爬取得数据字典，浅拷贝传递给下一个方法
    encoding,   # 请求编码 默认为utf-8
    priority,   # 请求的优先级 默认为0 优先级更高则会更早得执行，也可以使用复数 来表示 优先级很低得 request 对象
    dont_filter,# 设置是调度器是否过滤已经请求过得request 默认是过滤重复请求
    errback,    # 处理异常的回调函数。
    flags       # 发送到请求的标志，可用于日志记录或类似目的。
)
 ######################## 属性
 #
 # 这些属性大部分是只读，不能修改，如果要修改用replace()方法
 # 
 # --- url 返回请求得url地址，此属性包含转义的URL，因此它可能与构造函数中传递的URL不同。
 # 
 # --- method 返回请求方法
 # 
 # --- headers 字典类型得请求头
 # 
 # --- body 请求体
 # 
 # --- meta 包含此请求的任意元数据的字典。Request.meta默认情况下复制replace 得形参和值 
 # 
 # --- copy() 返回一个新请求副本
 # 
 # --- replace() 返回一个 形参相得request对象 ，可以指定哪个形参 可以覆盖原来得值
 # 
 # 
 # 
 # ####################### 子类 FormRequest post请求
 # 他可以发送post 请求 参数 通过 formdata 传递
 # 