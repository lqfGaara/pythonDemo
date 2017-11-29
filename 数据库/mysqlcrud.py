# coding:utf-8
from  MysqlHelper import MysqlHelper

name = input("请输入学生姓名：")
# age = input("请输入学生年龄：")
id=input("请输入学生id:")

helper = MysqlHelper('127.0.0.1', 3306, 'root', 'syl19930812', 'python3', 'utf8')
helper.creatConect()

#查询数据
# sql="select * from students where id =%s"
# parm=[id]
# print(helper.query(sql,parm))

#添加数据
# sql1="insert into students VALUES (%s,%s,%s,%s,%s)"
# parm1=[6,"lqf",1,"1992-12-17 02:12:45",26]
# helper.cur(sql1,parm1)

#更新操作
# sql3="update students set sname=%s where id=%s"
# parm2=[name,id]
# helper.cur(sql3,parm2)

#删除数据
sql4="delete from students WHERE id=%s"
parm3=[id]
helper.cur(sql4,parm3)

helper.close()