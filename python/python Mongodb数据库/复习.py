# import pymongo
# myclient = pymongo.MongoClient()
# mydb = myclient['test_d']
# dblist = myclient.list_database_names()
# if 'test_d' in dblist:
#     print("数据库已经存在")
# mycol = mydb['test_c']
# collist = mydb.list_collection_names()
# if 'test_c' in collist:
#     print("集合已经存在")

# ############# 添加数据
# import pymongo

# #1.0 连接数据库
# myclient = pymongo.MongoClient()
# # 2.0 创建数据库
# mydb = myclient['test_db']

# # 3.0 创建结合
# mycol = mydb["test_col"]

# # 4.0 数据预设
# # 4.1 单挑数据
# # mydict = {'name':"bruce lee",'age':32,'url':"http://www.baidu.com"}
# mydict = [
#     { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
#   { "_id": 2, "name": "Google", "address": "Google 搜索"},
#   { "_id": 3, "name": "Facebook", "address": "脸书"},
#   { "_id": 4, "name": "Taobao", "address": "淘宝"},
#   { "_id": 5, "name": "Zhihu", "address": "知乎"}
# ]
# # 5.0 插入数据
# x = mycol.insert_many(mydict) 

# # 6.0 返回插入的id字段
# print(x.inserted_ids)

############# 查询数据
# import pymongo
# myclient = pymongo.MongoClient()
# mydb = myclient["lagou"]
# mycol = mydb["上海"]
# mydata = mycol.find({"education":"本科"},{"workYear":1})
# print(mydata)

############# 修改数据

# import pymongo
# myclient = pymongo.MongoClient()
# mycol = myclient["test_db"]["test_col"]
# myquery = {"name":{"$regex":"^R"}}
# newvalues = {"$set":{"cn_name":"127.0.0.1"}}
# x = mycol.update_many(myquery,newvalues)
# print(x)
#
############# 删除数据
# import pymongo
# myclient = pymongo.MongoClient()
# mycol = myclient["test_db"]["test_col"]
# x = mycol.delete_many({})
# print(x)
