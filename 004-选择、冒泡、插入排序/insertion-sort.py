# 插入排序
def insertion_sort(arr):
    # 遍历从1到数组长度的每个元素
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


# 测试数据
arr = [12, 11, 13, 5, 6]
print("未排序的数组:")
print(arr)
print("排序后的数组:")
insertion_sort(arr)
print(arr)
