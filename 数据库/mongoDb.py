from pymongo import *

# 获取客户端，建立连接
client = MongoClient("localhost", 27017)
db = client.python3
stu = db.stu
# print(stu.find_one())
# 增加
# stu.insert({"title": "lqf123"})
# 删除
# stu.delete_one({"title": 'lqf123'})
#更新
# stu.update({"title": 'lqf123'},{"$set":{"title": "syl","count":25}})
# 查询
for cur in stu.find():
    print(cur)
