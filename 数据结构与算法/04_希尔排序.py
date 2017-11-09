# coding:utf-8
def shell_sort(list):
    n = len(list)
    gap = n // 2  # gap代表步长
    while (gap > 0):
        for i in range(gap, n):
            if (list[i] < list[i - gap]):
                list[i], list[i - gap] = list[i - gap], list[i]
        gap //= 2
    return list


if __name__ == "__main__":
    list = [23, 43, 53, 3, 52, 234, 65]
    print(list)
    shell_sort(list)
    print(list)
