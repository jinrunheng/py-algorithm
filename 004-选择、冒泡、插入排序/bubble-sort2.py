def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 标记是否有交换发生
        swapped = False
        # 遍历所有数组元素，从0到n-i-1
        # 最后一次迭代，最大的数已经在正确的位置
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # 标记发生了交换
                swapped = True
        # 如果没有发生交换，则数组已经是有序的
        if not swapped:
            break
