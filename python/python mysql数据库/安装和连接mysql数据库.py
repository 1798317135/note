# ##################  安装 ############################
# 
# --- mysql-connector-python
#     ptyon 需要安装这个三方包
import mysql.connector  
# 
# 
# ################### 连接 ############################

# # -- connect() 方法连接 数据库 返回个 MySQLConnection对象
# cnx = mysql.connector.connect(
#     user = 'root',
#     password = 'a123456',
#     host = 'localhost',
#     database = 'test1' 
# )
# cnx.close()

# -- 也可以将这个mysql数据库对象 转换为一个上下文管理器
#     然后用with 语句进行操作
# 
# -- 转换成上下文管理器 有三种方法 
#    用 三方包contextlib.closing(thing) 这个方法 可以将 拥有close()方法的 类
#    快速创建成 上下文管理器 
import contextlib

mydb = mysql.connector.connect(
    user = 'root',
    password = '123456',
    host = 'localhost',
    database = 'test1',
    charset = 'utf8'
)

with contextlib.closing(mydb) as db:
    # 如果要操作 数据库
    # 第一步要 使用cursor()方法获取操作游标
    cursor = db.cursor();

    #第二步使用execute方法执行SQL语句
    tables = cursor.execute("show tables")

    #第三步 使用 fetchone() 方法获取一条数据
    # data = cursor.fetchone()
    # print(data)



