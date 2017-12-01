from MysqlHelper import MysqlHelper
from hashlib import sha1

sname = input("请输入用户名：")
spwd = input("请输入密码：")

# sha1加密，加密的文本必须要encode
spwd = sha1(spwd.encode("utf-8")).hexdigest()

sqlHelper = MysqlHelper('127.0.0.1', 3306, 'root', 'syl19930812', 'python3', 'utf8')
sqlHelper.creatConect()

parms = [sname]
sqlpwd = "select pwd from userinfo WHERE name=%s"
dbpwd = sqlHelper.query(sqlpwd, parms)
# 查询结果不存在的时候说明用户名错误
if (len(dbpwd) == 0):
    print("登录失败！，用户名错误")
# 查询结果数据类型((a),)所以用dbpwd[0][0]
elif (dbpwd[0][0] == spwd):
    print("登录成功！")
else:
    print("登录失败！密码错误")

sqlHelper.close()
