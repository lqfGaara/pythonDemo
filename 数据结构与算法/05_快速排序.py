# coding:utf-8
def quick_sort(list, left, right):
    while (left >= right):
        return list
    # 两个游标左右同时开始比较
    mid_vlues = list[left]
    low = left
    high = right
    while left < right:
        while left < right and list[right] >= mid_vlues:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] < mid_vlues:
            left += 1
        list[right] = list[left]
    list[left] = mid_vlues
    quick_sort(list, low, left - 1)
    quick_sort(list, left + 1, high)
    return list


def quick_sort1(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


if __name__ == "__main__":
    list = [23, 43, 53, 13, 52, 234, 65]
    print(list)
    quick_sort(list, 0, 6)
    print(list)
