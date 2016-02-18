__author__ = 'Administrator'

import heapq

nums = [12, 4, 2, 5, 6, 1, 3, 5, 7]
# 第一个参数是个数
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(2, nums))

persons = [
    {'name': 'Jack', 'age': 22},
    {'name': 'Jones1', 'age': 88},
    {'name': 'Jones2', 'age': 7},
    {'name': 'Jones3', 'age': 66},
    {'name': 'Jones4', 'age': 2},
    {'name': 'Jones5', 'age': 99},
    {'name': 'Jones6', 'age': 32},
    {'name': 'Jones7', 'age': 51},
    {'name': 'Jones8', 'age': 12},
    {'name': 'Jones9', 'age': 82}

]

print(heapq.nsmallest(2, persons, key=lambda s: s['age']))

# 如果最大最小N的值比总数小很多，那么下面这些函数提供更好的性能，函数底层将数据转化为列表，元素以堆的形式排序
l = list(nums)
heapq.heapify(l)
# 最小堆,l[0]始终是最小的
print(l)
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))
