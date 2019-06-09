# ###################### http概念
# 
# 1.0 http：超文本传输协议
# 2.0 HTTP基于TCP/IP通信协议来传递数据。
# 3.0 最新版本 HTTP/1.1
# 4.0 http 可以传送任意类型的数据对象 通过MIME-type 设置内容类型。
# 5.0 无连接：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。
# 6.0 无状态：HTTP协议是无状态协议。无状态是指协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，
#          这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快。
#          
# ####################### http模式        
# 支持B/S及C/S模式。 浏览器/服务器械 客户端/服务器
# 
# ####################### url
# http 通过url 来建立链接 和传输的
# url 包括七部分
# http://www.aspxfans.com:8080/news/index.asp?boardID=5&ID=24618&page=1#name
# 协议://域名部分        ：端口部分/虚拟目录部分/文件名部分?#锚点部分&参数部分
# 
# ####################### 客户端 请求requests 和 响应 response
# 
#
# --- 客户端的http request请求
# 请求行（request line）、请求头部（header）、空行和请求数据四个部分组成
# 
# --- 服务端响应的respones
# HTTP响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文。
# 
# --- HTTP消息头支持自定义， 自定义的专用消息头一般会添加'X-'前缀。
# 
# --- 常用的请求头
        # Accept    可接受的响应内容类型（Content-Types）。  Accept: text/plain  固定
        # Accept-Charset  可接受的字符集 Accept-Charset: utf-8   固定
        # Accept-Encoding 可接受的响应内容的编码方式。  Accept-Encoding: gzip, deflate  固定
        # Accept-Language 可接受的响应内容语言列表。   Accept-Language: en-US  固定
        # Accept-Datetime 可接受的按照时间来表示的响应内容版本  Accept-Datetime: Sat, 26 Dec 2015 17:30:00 GMT  临时
        # Authorization   用于表示HTTP协议中需要认证资源的认证信息  Authorization: Basic OSdjJGRpbjpvcGVuIANlc2SdDE==   固定
        # Cache-Control   用来指定当前的请求/回复中的，是否使用缓存机制。    Cache-Control: no-cache 固定
        # Connection  客户端（浏览器）想要优先使用的连接类型 Connection: keep-alive
        # Connection: Upgrade

        # 固定
        # Cookie  由之前服务器通过Set-Cookie（见下文）设置的一个HTTP协议Cookie    Cookie: $Version=1; Skin=new;   固定：标准
        # Content-Length  以8进制表示的请求体的长度   Content-Length: 348 固定
        # Content-MD5 请求体的内容的二进制 MD5 散列值（数字签名），以 Base64 编码的结果 Content-MD5: oD8dH2sgSW50ZWdyaIEd9D==   废弃
        # Content-Type    请求体的MIME类型 （用于POST和PUT请求中）  Content-Type: application/x-www-form-urlencoded 固定
        # Date    发送该消息的日期和时间（以RFC 7231中定义的"HTTP日期"格式来发送） Date: Dec, 26 Dec 2015 17:30:00 GMT 固定
        # Expect  表示客户端要求服务器做出特定的行为   Expect: 100-continue    固定
        # From    发起此请求的用户的邮件地址   From: user@itbilu.com   固定
        # Host    表示服务器的域名以及服务器所监听的端口号。如果所请求的端口是对应的服务的标准端口（80），则端口号可以省略。  Host: www.itbilu.com:80
        # Host: www.itbilu.com

        # 固定
        # If-Match    仅当客户端提供的实体与服务器上对应的实体相匹配时，才进行对应的操作。主要用于像 PUT 这样的方法中，仅当从用户上次更新某个资源后，该资源未被修改的情况下，才更新该资源。   If-Match: "9jd00cdj34pss9ejqiw39d82f20d0ikd"    固定
        # If-Modified-Since   允许在对应的资源未被修改的情况下返回304未修改    If-Modified-Since: Dec, 26 Dec 2015 17:30:00 GMT    固定
        # If-None-Match   允许在对应的内容未被修改的情况下返回304未修改（ 304 Not Modified ），参考 超文本传输协议 的实体标记   If-None-Match: "9jd00cdj34pss9ejqiw39d82f20d0ikd"   固定
        # If-Range    如果该实体未被修改过，则向返回所缺少的那一个或多个部分。否则，返回整个新的实体 If-Range: "9jd00cdj34pss9ejqiw39d82f20d0ikd"    固定
        # If-Unmodified-Since 仅当该实体自某个特定时间以来未被修改的情况下，才发送回应。   If-Unmodified-Since: Dec, 26 Dec 2015 17:30:00 GMT  固定
        # Max-Forwards    限制该消息可被代理及网关转发的次数。  Max-Forwards: 10    固定
        # Origin  发起一个针对跨域资源共享的请求（该请求要求服务器在响应中加入一个Access-Control-Allow-Origin的消息头，表示访问控制所允许的来源）。  Origin: http://www.itbilu.com   固定: 标准
        # Pragma  与具体的实现相关，这些字段可能在请求/回应链中的任何时候产生。 Pragma: no-cache    固定
        # Proxy-Authorization 用于向代理进行认证的认证信息。 Proxy-Authorization: Basic IOoDZRgDOi0vcGVuIHNlNidJi2== 固定
        # Range   表示请求某个实体的一部分，字节偏移以0开始。  Range: bytes=500-999    固定
        # Referer 表示浏览器所访问的前一个页面，可以认为是之前访问页面的链接将浏览器带到了当前页面。Referer其实是Referrer这个单词，但RFC制作标准时给拼错了，后来也就将错就错使用Referer了。   Referer: http://itbilu.com/nodejs   固定
        # TE  浏览器预期接受的传输时的编码方式：可使用回应协议头Transfer-Encoding中的值（还可以使用"trailers"表示数据传输时的分块方式）用来表示浏览器希望在最后一个大小为0的块之后还接收到一些额外的字段。    TE: trailers,deflate    固定
        # User-Agent  浏览器的身份标识字符串 User-Agent: Mozilla/……  固定
        # Upgrade 要求服务器升级到一个高版本协议。    Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11  固定
        # Via 告诉服务器，这个请求是由哪些代理发出的。    Via: 1.0 fred, 1.1 itbilu.com.com (Apache/1.1)  固定
        # Warning 一个一般性的警告，表示在实体内容体中可能存在错误。   Warning: 199 Miscellaneous warning  固定
        # 
        # 
        # 
# --- 常用的响应头
        
        # Access-Control-Allow-Origin 指定哪些网站可以跨域源资源共享 Access-Control-Allow-Origin: *  临时
        # Accept-Patch    指定服务器所支持的文档补丁格式 Accept-Patch: text/example;charset=utf-8    固定
        # Accept-Ranges   服务器所支持的内容范围 Accept-Ranges: bytes    固定
        # Age 响应对象在代理缓存中存在的时间，以秒为单位   Age: 12 固定
        # Allow   对于特定资源的有效动作;    Allow: GET, HEAD    固定
        # Cache-Control   通知从服务器到客户端内的所有缓存机制，表示它们是否可以缓存这个对象及缓存有效时间。其单位为秒  Cache-Control: max-age=3600 固定
        # Connection  针对该连接所预期的选项 Connection: close   固定
        # Content-Disposition 对已知MIME类型资源的描述，浏览器可以根据这个响应头决定是对返回资源的动作，如：将其下载或是打开。  Content-Disposition: attachment; filename="fname.ext"   固定
        # Content-Encoding    响应资源所使用的编码类型。   Content-Encoding: gzip  固定
        # Content-Language    响就内容所使用的语言  Content-Language: zh-cn 固定
        # Content-Length  响应消息体的长度，用8进制字节表示   Content-Length: 348 固定
        # Content-Location    所返回的数据的一个候选位置   Content-Location: /index.htm    固定
        # Content-MD5 响应内容的二进制 MD5 散列值，以 Base64 方式编码  Content-MD5: IDK0iSsgSW50ZWd0DiJUi==    已淘汰
        # Content-Range   如果是响应部分消息，表示属于完整消息的哪个部分 Content-Range: bytes 21010-47021/47022  固定
        # Content-Type    当前内容的MIME类型 Content-Type: text/html; charset=utf-8  固定
        # Date    此条消息被发送时的日期和时间(以RFC 7231中定义的"HTTP日期"格式来表示)  Date: Tue, 15 Nov 1994 08:12:31 GMT 固定
        # ETag    对于某个资源的某个特定版本的一个标识符，通常是一个 消息散列  ETag: "737060cd8c284d8af7ad3082f209582d"    固定
        # Expires 指定一个日期/时间，超过该时间则认为此回应已经过期   Expires: Thu, 01 Dec 1994 16:00:00 GMT  固定: 标准
        # Last-Modified   所请求的对象的最后修改日期(按照 RFC 7231 中定义的“超文本传输协议日期”格式来表示) Last-Modified: Dec, 26 Dec 2015 17:30:00 GMT    固定
        # Link    用来表示与另一个资源之间的类型关系，此类型关系是在RFC 5988中定义    Link: ; rel="alternate" 固定
        # Location    用于在进行重定向，或在创建了某个新资源时使用。 Location: http://www.itbilu.com/nodejs  固定
        # P3P P3P策略相关设置   P3P: CP="This is not a P3P policy!  固定
        # Pragma  与具体的实现相关，这些响应头可能在请求/回应链中的不同时候产生不同的效果    Pragma: no-cache    固定
        # Proxy-Authenticate  要求在访问代理时提供身份认证信息。   Proxy-Authenticate: Basic   固定
        # Public-Key-Pins 用于防止中间攻击，声明网站认证中传输层安全协议的证书散列值   Public-Key-Pins: max-age=2592000; pin-sha256="……";  固定
        # Refresh 用于重定向，或者当一个新的资源被创建时。默认会在5秒后刷新重定向。   Refresh: 5; url=http://itbilu.com    
        # Retry-After 如果某个实体临时不可用，那么此协议头用于告知客户端稍后重试。其值可以是一个特定的时间段(以秒为单位)或一个超文本传输协议日期。 
        # 示例1:Retry-After: 120
        # 示例2: Retry-After: Dec, 26 Dec 2015 17:30:00 GMT
        # 固定

        # Server  服务器的名称  Server: nginx/1.6.3 固定
        # Set-Cookie  设置HTTP cookie   Set-Cookie: UserID=itbilu; Max-Age=3600; Version=1  固定: 标准
        # Status  通用网关接口的响应头字段，用来说明当前HTTP连接的响应状态。 Status: 200 OK   
        # Trailer Trailer用户说明传输中分块编码的编码信息 Trailer: Max-Forwards   固定
        # Transfer-Encoding   用表示实体传输给用户的编码形式。包括：chunked、compress、 deflate、gzip、identity。 Transfer-Encoding: chunked  固定
        # Upgrade 要求客户端升级到另一个高版本协议。   Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11  固定
        # Vary    告知下游的代理服务器，应当如何对以后的请求协议头进行匹配，以决定是否可使用已缓存的响应内容而不是重新从原服务器请求新的内容。  Vary: * 固定
        # Via 告知代理服务器的客户端，当前响应是通过什么途径发送的。 Via: 1.0 fred, 1.1 itbilu.com (nginx/1.6.3) 固定
        # Warning 一般性警告，告知在实体内容体中可能存在错误。  Warning: 199 Miscellaneous warning  固定
        # WWW-Authenticate    表示在请求获取这个实体时应当使用的认证模式。  WWW-Authenticate: Basic
# 
# 
# 
# 状态码--HTTP之状态码
# 状态代码有三位数字组成，第一个数字定义了响应的类别，共分五种类别:
# 1xx：指示信息--表示请求已接收，继续处理
# 2xx：成功--表示请求已被成功接收、理解、接受
# 3xx：重定向--要完成请求必须进行更进一步的操作
# 4xx：客户端错误--请求有语法错误或请求无法实现
# 5xx：服务器端错误--服务器未能实现合法的请求
# 
# 请求方法 -HTTP请求方法
# GET     请求指定的页面信息，并返回实体主体。
#         
# HEAD     类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
# POST     向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
# PUT     从客户端向服务器传送的数据取代指定的文档的内容。
# DELETE      请求服务器删除指定的页面。
# CONNECT     HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
# OPTIONS     允许客户端查看服务器的性能。
# TRACE     回显服务器收到的请求，主要用于测试或诊断。
# 
# HTTP属于应用层协议，在传输层使用TCP协议，在网络层使用IP协议。
#  IP协议主要解决网络路由和寻址问题，TCP协议主要解决如何在IP层之上可靠地
# 传递数据包，使得网络上接收端收到发送端所发出的所有包，并且顺序与发送顺序一致。TCP协议是可靠的、面向连接的。
# 
# 
def get_headers(header_raw):
    """
    通过原生请求头获取请求头字典
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    """
    header_raw = header_raw.strip()  # 处理可能的空字符
    header_raw = header_raw.split("\n")  # 分割每行
    header_raw = [line.split(":", 1) for line in header_raw]  # 分割冒号
    header_raw = dict((k.strip(), v.strip()) for k, v in header_raw)  # 处理可能的空字符
    return header_raw
def get_cookie(cookies):
    cookies = dict(i.split('=',1) for i in cookies.split(';'))
    return cookies

if __name__ == '__main__':
        headers = """
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Host: www.lagou.com
Pragma: no-cache
Referer: https://www.lagou.com/jobs/list_pyton?labelWords=&fromSearch=true&suginput=
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
        """
        cookies = """
        JSESSIONID=ABAAABAAAIAACBI10F140F5A45A752758D1AAD6AA8C96C9; _ga=GA1.2.502105547.1555305914; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555305914; user_trace_token=20190415132512-d8172284-5f3e-11e9-9374-5254005c3644; LGSID=20190415132512-d81723d8-5f3e-11e9-9374-5254005c3644; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190415132512-d8172540-5f3e-11e9-9374-5254005c3644; _gid=GA1.2.1234735050.1555305914; TG-TRACK-CODE=search_code; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a1f8b7cb8522-05d79e8cfffc5c-7a1437-1327104-16a1f8b7cb94ee%22%2C%22%24device_id%22%3A%2216a1f8b7cb8522-05d79e8cfffc5c-7a1437-1327104-16a1f8b7cb94ee%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LG_LOGIN_USER_ID=2e4b0dc3a3cbb85dcfe67641fbe78d7bee748d4f69726f027fdd8e21dc6cce9f; _putrc=F5CC2095643DBA46123F89F2B170EADC; login=true; unick=bruce+yang; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=7ce261d14321c5adf06ce33e0180d3d60bc7f13396764e5e773458a12d0fa937; SEARCH_ID=bd7667ab8a1744129c740c097dedf41f; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=1983d7812e9e503a5947035551954d717350e9d0bd; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555307496; _gat=1; LGRID=20190415135135-873db608-5f42-11e9-85ba-525400f775ce
        """
        cookie = get_cookie(cookies)
        header = get_headers(headers)
        # print(header)
        print("*"*20)
        print(cookie)