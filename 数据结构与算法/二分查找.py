# coding :utf-8
# 对于有序数组，可以采用二分查找的方式提高查找效率
def Binaryearch(list, key):
    # 对于一个升序的列表
    n = len(list)
    if (n > 0):
        mid = n // 2
        if (key > list[mid]):
            return Binaryearch(list[mid + 1:], key)
        elif (key == list[mid]):
            return True
        else:
            return Binaryearch(list[:mid], key)
    return False


if __name__ == "__main__":
    list = [13, 23, 43, 52, 53, 65, 234]
    s = Binaryearch(list, 33)
    print(s)
