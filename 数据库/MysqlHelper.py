# coding:utf-8
import pymysql


class MysqlHelper:
    # 初始化信息
    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

    # 建立连接
    def creatConect(self):
        self.connect = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db,
                                       charset=self.charset)
        self.cuor = self.connect.cursor();

    # 关闭连接
    def close(self):
        self.connect.close()
        self.cuor.close()

    # 更新、删除、增加数据
    def cur(self, sql, parm):
        try:
            self.cuor.execute(sql, parm)
            self.connect.commit()
        except Exception as e:
            print(e)

    # 查询数据
    def query(self, sql, parm):
        try:
            self.cuor.execute(sql, parm)
            return self.cuor.fetchall()
        except Exception as e:
            print(e)
