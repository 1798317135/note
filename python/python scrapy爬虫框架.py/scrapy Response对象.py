# response 这通常是下载（由下载器）并馈送到蜘蛛进行处理
# response(
    # url（字符串） - 此响应的URL
    # status（整数） - 响应的HTTP状态。默认为200。
    # headers（dict） - 此响应的标头。dict值可以是字符串（对于单值标头）或列表（对于多值标头）。
    # body（字节） - 响应主体。要将解码后的文本作为str（Python 2中的unicode）访问，您可以使用response.text来自编码感知的 Response子类，例如TextResponse。
    # flags（列表） - 是包含Response.flags属性初始值的列表 。如果给定，列表将被浅层复制。
    # request（Requestobject） - Response.request属性的初始值。这表示Request生成此响应。
# )
# 
####################### Request对象的快捷键 Response.follw()
#
# 通常我们在spider中爬取的url需要重新包装成request对象，然后在传递给调度器
# 我们可以直接用 Rresponse.follow() 来节省这个步骤 他可以直接把他传递给下载器
# 可以还有几个快速的功能
# --- 快速的功能
# 1.0 他可以直接用相对路径，内部自动调用urljoin()方法将相对路径改为绝对路径
# 2.0 如果在他的url传递的是一个a标签，他会自动用a标签的href属性值 ，进一步节省代码

def parse(self,response):
    next = response.xpath("//a").extract_first()
    yield scripy.Response.follow(
        next,
        callback = self.parse1,
        meta = "item"
        )



