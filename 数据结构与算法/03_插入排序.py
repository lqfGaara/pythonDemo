# coding:utf-8
# 插入排序的原理就是从后面随便选择一个数据插入到前面的有序列表中
def insert_sort(list):
    # 先对内层排序，随便取出一个放在最前面
    n = len(list)
    min_index = 0
    for j in range(min_index, n):
        for i in range(min_index):
            if (list[j] < list[i]):
                list[i], list[j] = list[j], list[i]
        min_index += 1
    return list


if __name__ == "__main__":
    list = [23, 43, 53, 3, 52, 234, 65]
    print(list)
    insert_sort(list)
    print(list)
