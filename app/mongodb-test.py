# -*- coding:utf-8 -*-

from pymongo import MongoClient

# https://www.cnblogs.com/melonjiang/p/6536876.html

# mongodb tutorial:
# http://www.runoob.com/mongodb/mongodb-tutorial.html

# open connection
conn = MongoClient('127.0.0.1', 27017)
db = conn.transaction
my_set = db.futures

# insert
users = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 20}]
my_set.insert(users)

# # 查询全部
# for i in my_set.find():
#     print(i)
# # 查询name=zhangsan的
# for i in my_set.find({"name": "zhangsan"}):
#     print(i)
# print(my_set.find_one({"name": "zhangsan"}))
#
# # update
# my_set.update({"name": "zhangsan"}, {'$set': {"age": 20}})
#
# # 删除name=lisi的全部记录
# my_set.remove({'name': 'zhangsan'})
#
# # 删除name=lisi的某个id的记录
# id = my_set.find_one({"name": "zhangsan"})["_id"]
# my_set.remove(id)
#
# # 删除集合里的所有记录
# db.users.remove()
#
# # 条件操作符
# #    (>)  大于 - $gt
# #    (<)  小于 - $lt
# #    (>=)  大于等于 - $gte
# #    (<= )  小于等于 - $lte
#
# for i in my_set.find({"age": {"$gt": 25}}):
#     print(i)
#
# # 找出name的类型是String的
# for i in my_set.find({'name': {'$type': 2}}):
#     print(i)
#
# # sort
# for i in my_set.find().sort([("age", 1)]):
#     print(i)
#
# # limit()方法用来读取指定数量的数据
# # skip()方法用来跳过指定数量的数据
# # 下面表示跳过两条数据后读取6条
# for i in my_set.find().skip(2).limit(6):
#     print(i)
#
# # 找出age是20、30、35的数据
# for i in my_set.find({"age": {"$in": (20, 30, 35)}}):
#     print(i)
#
# # 找出age是20或35的记录
# for i in my_set.find({"$or": [{"age": 20}, {"age": 35}]}):
#     print(i)
#
# '''
# dic = {"name":"lisi","age":18,"li":[1,2,3]}
# dic2 = {"name":"zhangsan","age":18,"li":[1,2,3,4,5,6]}
#
# my_set.insert(dic)
# my_set.insert(dic2)'''
# for i in my_set.find({'li': {'$all': [1, 2, 3, 4]}}):
#     print(i)
# # 查看是否包含全部条件
# # 输出：{'_id': ObjectId('58c503b94fc9d44624f7b108'), 'name': 'zhangsan', 'age': 18, 'li': [1, 2, 3, 4, 5, 6]}
#
#
# my_set.update({'name': "lisi"}, {'$push': {'li': 4}})
# for i in my_set.find({'name': "lisi"}):
#     print(i)
# # 输出：{'li': [1, 2, 3, 4], '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi'}
#
# my_set.update({'name': "lisi"}, {'$pushAll': {'li': [4, 5]}})
# for i in my_set.find({'name': "lisi"}):
#     print(i)
# # 输出：{'li': [1, 2, 3, 4, 4, 5], 'name': 'lisi', 'age': 18, '_id': ObjectId('58c50d784fc9d44ad8f2e803')}
#
# # pop
# # 移除最后一个元素(-1为移除第一个)
# my_set.update({'name': "lisi"}, {'$pop': {'li': 1}})
# for i in my_set.find({'name': "lisi"}):
#     print(i)
# # 输出：{'_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi', 'li': [1, 2, 3, 4, 4]}
#
# # pull （按值移除）
# # 移除3
# my_set.update({'name': "lisi"}, {'$pop': {'li': 3}})
#
# # pullAll （移除全部符合条件的）
# my_set.update({'name': "lisi"}, {'$pullAll': {'li': [1, 2, 3]}})
# for i in my_set.find({'name': "lisi"}):
#     print(i)
# # 输出：{'name': 'lisi', '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'li': [4, 4], 'age': 18}
