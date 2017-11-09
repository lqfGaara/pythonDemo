# coding:utf-8
# 选择排序，相当于分成两个部分，前面一部分是后面一部分中最小的取出来放在前面
def select_sort(list):
    n = len(list)
    # 外层循环控制最小索引
    for j in range(n - 1):
        # 选择最小的放在最前面
        min_index = j
        for i in range(j + 1, n):
            if (list[min_index] > list[i]):
                list[min_index], list[i] = list[i], list[min_index]
    return list


if __name__ == "__main__":
    list = [123, 43, 453, 3, 52, 234, 65]
    print(list)
    select_sort(list)
    print(list)
