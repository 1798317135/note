# item时通过__getattr__ 和 __setattr__ 等魔法函数实现的
# 他主要时预先定义好数据结构和字段，然后我们在爬取过程中必须用到这些定义得字段 
# 这样就可以把所有字段统一在一个地方，方便管理
# 他可以格式化 输出更加美观
# 
# 语法是：
import scrapy
class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

# 可以通过Item.fields属性访问定义得字段
# 
# 但是需要注意得是 用Item定义得字段 返回储存得数据，并不是字典dict类型
# 如果需要，储存到mongo得话 需要转换成字典类型得数据