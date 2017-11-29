import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="syl19930812", db="python3", charset="utf8")

cur = conn.cursor()

sql = "insert into students values (4,'王五',0,'1992-12-17 02:10:13',35)";
try:
    cur.execute(sql)
except Exception as e:
    print(e)
conn.commit()

rows = cur.fetchall()

for dr in rows:
    print(dr)