# coding:utf-8
def bubble_sort(list):
    n = len(list)
    for j in range(0, n - 1):
        for i in range(0, n - j - 1):
            if (list[i] > list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]


if __name__ == "__main__":
    list = [123, 43, 453, 3, 52, 234, 65]
    print(list)
    bubble_sort(list)
    print(list)
