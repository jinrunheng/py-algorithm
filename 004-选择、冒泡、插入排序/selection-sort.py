# 选择排序
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 测试排序
arr = [64, 34, 25, 12, 22, 11, 90]
print("排序前的数组：")
print(arr)
print("排序后的数组:")
selection_sort(arr)
print(arr)
