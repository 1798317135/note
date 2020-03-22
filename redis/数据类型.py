# redis 有五种基础类型
################# 键命令
# 键命令可以对任何数据类型进行操作
# ----- 查看所有键
# keys 表达式
#       * 代表所有
# 
# ---- 查看键是否存在
# 如果存在返回1
# 如果不存在返回0
# exists key
# 
# --- 查看值的类型
# type key
# 
# --- 删除键
# 如果删除成功返回1
# 如果删除的键不存在返回0
# del key1 key2 ....
# 
# --- 设置已经存在值建的过期时间
#   如果键存在返回1
#   如果键不存在返回0
# expire key 秒
# 
# --- 查看键的存在时间
# 如果这个key没有设置过期时间那么返回-1
# 如果这个key已经过期或者不存在 返回-2
# ttl key 
# 
################# 1.0 string 字符串
# 他是redsi 基本的类型，有键值对组成
# 他可以储存任何内容，一个键最大储存512M的值
#     
# ******* 设置 和 修改
# --- 设置单个键值对
# 
# 如果这个建不存在set 可以设置 
# 如果这个建存在 那么set 可以修改这个建的值
# set key value
# 
# --- 设置多个键值对
# mset key1 value key2 value key3 value ... 
# 
# --- 设置键的过期时间
# setex key 秒数 value
#
# ******* 获取值
# get key
# 
# --- 获取多个值
# mget key1 key2 ... 
# 
# 
############### 2.0 hash 哈希类型
# hash类型用于存储一个对象
# 值的类型为string
# 
# --- 设置单个属性值
# 可能会报错
# WRONGTYPE Operation against a key holding the wrong kind of value
# 原因是强制关闭redis快照导致不能持久化
# 解决方案是
# config set stop-writes-on-bgsave-error no
# 
# hset key 属性 值
# 
# --- 设置多个属性
# hmset key field value field1 value ....
# 
# --- 查看hash键的多有属性
# hkeys key
# 
# --- 查看hash键的所有值
# hvalues key
# 
# --- 获取单个hash属性的值
# 没有则返回nil空值
# hget key field 
# 
# --- 获取多个hash属性的值
# hmget key field1 field2 field3...
# 
# --- 删除hash键某一个属性的值
# hdel key field
# 
############## 3.0 list 列表
# 列表的元素也是string类型
# 
# ---从左侧插入数据
# lpush key 元素1 元素2..
# 
# --- 从右侧插入数据
# rpush key 元素1 元素2
# 
# --- 设置指定下标的值
# lset key index value
# 
# --- 在某个值之前或者之后插入元素
# linset key after|before 指定元素 插入元素
# 
# --- 返回列表的长度
# llen key
# 
# --- 获取指定下标的元素值
# lindex key index 
# 
# --- 删除列表左边第一个 或者右边第一个 并返回删除的元素
# lpop key 
# rpop key
# --- 删除列表指定元素 和 次数
#lrem key 元素 count 如果count设置为负数是用右边往左删
#                    如果count设置为0 那么删除全部
# 
# --- 查看列表
# lrange key 从下表几开始 到下表几结束 -1 代表最后一个

############## 4.0 set 集合
# set是无序集合
# 每个元素都是唯一的 不能重复
#
# --- 给集合添加元素
# sadd keys number1 number2
# 
# --- 查看集合 
# smembers key 
# 
# --- 删除集合元素
# srem key
# 
############## 5.0 zset 有序集合
# zset 是一个有序的集合
# zset的每个元素都有一个double类型的权重值 自动根据权重从小到大以此排序
# 
# --- 添加元素
# zadd key 权重 值 权重 值
# 
# --- 查看zset 
# zrange key 从几 到 几 
# 
#  --- 查看指定权值之间的元素
#  zrangebyscore key min max
#  
#  --- 查看指定元素的权值
#  zscore key number
#  
#  --- 删除某个元素
#  zrem key number
#  
#  --- 删除指定权值在多少之间的元素
#  zremrangebyscore key min max
#  
#  