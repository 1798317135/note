import pymongo
# 连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 查看数据库列表
dblist = myclient.list_database_names()
# 选择或者创建数据库
mydb = myclient['kugou']
# 选择或者创建集合
mycol = mydb['top500']
# 获取集合里列表
collist = mydb.list_collection_names()
# 查询数据
find = mycol.find()
print(list(find)[0])
# 插入收据
data = {
    'singer':"王力宏",
    'song':"唯一",
    'time':"03:45",
}
song_id = mycol.insert_one(data)
print(song_id)

# 
