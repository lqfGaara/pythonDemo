from MysqlHelper import MysqlHelper
from RedisTest import RedisHelper
from hashlib import sha1

sname = input("请输入用户名：")
spwd = input("请输入密码：")

# sha1加密，加密的文本必须要encode
#用户输入的密码
spwd = sha1(spwd.encode("utf-8")).hexdigest()

sqlHelper = MysqlHelper('127.0.0.1', 3306, 'root', 'syl19930812', 'python3', 'utf8')
sqlHelper.creatConect()
rhelper = RedisHelper("localhost", 6379)
#redis查询的密码,python
rpwd = rhelper.getValue(sname).decode()

parms = [sname]
sqlpwd = "select pwd from userinfo WHERE name=%s"
#mysql查询的密码
dbpwd = sqlHelper.query(sqlpwd, parms)

if (rpwd == None):
    # 查询结果不存在的时候说明用户名错误
    if (len(dbpwd) == 0):
        print("mysql登录失败！，用户名错误")
    else:
        # 保存用户名和密码到redis
        rhelper.setValue(sname, dbpwd[0][0])
        # 查询结果数据类型((a),)所以用dbpwd[0][0]
        if (dbpwd[0][0] == spwd):
            print("mysql登录成功！")
        else:
            print("mysql登录失败！密码错误")
else:
    if (spwd == rpwd):
        print("redis登录成功！")
    else:
        print("redis登录失败！密码错误")
sqlHelper.close()
