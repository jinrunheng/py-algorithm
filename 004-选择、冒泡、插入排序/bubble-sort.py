# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 遍历所有数组元素，从0到n-i-1
        # 最后一次迭代，最大的数已经在正确的位置
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 测试冒泡排序函数
arr = [64, 34, 25, 12, 22, 11, 90]
print("排序前的数组:")
print(arr)
print("排序后的数组:")
bubble_sort(arr)
print(arr)
