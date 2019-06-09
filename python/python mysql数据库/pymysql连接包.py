# import pymysql
#################### 连接数据库 
#
# # 1.0 打开数据库连接
# db = pymysql.connect("localhost","root","123456","test")

# # 2.0 使用cursor()创建一个游标对象
# cursor = db.cursor()

# # 3.0 使用execute()方法来执行sql查询

# sql = "select * from cou";

# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for i,v in results:
#         print(i,v)
# except Exception as e:
#     raise e


# cursor.close()
# db.close()


###################### 创建数据库
#
# 1.0 代开数据库连接

# db = pymysql.connect("localhost","root","123456","test")

# # 2.0 创建游标对象
# cursor = db.cursor()

# # 3.0 执行sql语句
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # 4.0 与处理语句

# sql = """create table EMPLOYEE (
#             id int primary key auto_increment,
#             name varchar(255) not null,
#             sex char(20),
#             age int
#             )"""

# try:
#     cursor.execute(sql)
# except Exception as e:
#     pass
# finally:
#     cursor.close()
#     db.close()


################# 数据库的插入操作

# sql = """ insert into t1(name,sex,age) values('') """

# try:
#     db = pymysql.connect("localhost","root","123456","test")
#     cursor = db.cursor()
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     raise e
#     db.rollback()
# finally:
#     cursor.close()
#     db.close()

############# 数据库查询
#
# 获取一条fetchone()
# db = pymysql.connect("localhost","root","123456","test")
# cursor = db.cursor()
# sql = """select * from t1 where name = '{}'""".format("bruce")
# try:
#     cursor.execute(sql)
#     # result = cursor.fetchone() #查询一条
#     result = cursor.fetchall() #c查询多条
#     print(cursor.rowcount) #影响的条数
#     
# except Exception as e:
#     raise e
# else:
#     # print(result)
#     for data in result:
#         print(data)
# finally:
#     cursor.close()
#     db.close()

############## 更新

# db = pymysql.connect("localhost","root","123456","test")
# cursor = db.cursor()
# sql = """update t1 set name = '{}' where id = {}""".format("朱旭路",13)

# try:
#     cursor.execute(sql)
# except Exception as e:
#     raise e
#     db.rollback()
# else:
#     db.commit()
# finally:
#     cursor.close()
#     db.close()
#     
# ############ 删除数据库
#
# db = pymysql.connect("localhost","root","123456","test")
# cursor = db.cursor()
# sql = """delete from t1 where name = '{}'""".format("朱旭路")
# try:
#     cursor.execute(sql)
# except Exception as e:
#     raise e
#     db.rollback()
# else:
#     db.commit()
# finally:
#     cursor.close()
#     db.close()

#################### 执行事务

# sql = """delete from t1 where name = '{}'""".format("bruce lee")
# db = pymysql.connect("localhost","root","123456","test")
# cursor = db.cursor()
# try:
#     cursor.execute(sql)
# except Exception as e:
#     raise e
#     db.rollback()
# else:
#     db.commit()
# finally:
#     cursor.close()
#     db.close()