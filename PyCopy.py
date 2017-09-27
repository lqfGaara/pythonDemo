import os
from multiprocessing import Pool, Manager


# 创建子进程拷贝文件
def copyFile(name, oldFileName, newFileName):
    fr = open(oldFileName + "/" + name)
    fw = open(newFileName + "/" + name, "w")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    # queue.put(name)


pool = Pool(3)
queue = Manager().Queue()
# 完成拷贝文件夹
# 创建文件夹接收文件
oldFileName = input("请输入要拷贝的文件名称：")
newFileName = oldFileName + "-副本"
os.mkdir(newFileName)
# 获取文件夹下的每个文件
filenamelist = os.listdir(oldFileName)
for name in filenamelist:
    pool.apply_async(copyFile, args=(name, oldFileName, newFileName))

# num = 0
# listnum = len(filenamelist)
# while num < listnum:
#     queue.get()
#     num += 1
#     print("\r复制进度：%.2f%%" % (num * 100 / listnum), end="")

pool.close()
pool.join()
