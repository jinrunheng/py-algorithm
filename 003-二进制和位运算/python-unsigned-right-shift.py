# 模拟无符号右移的函数
def unsigned_right_shift(n, shift):
    mask = (1 << 32) - 1  # 创建一个32位的掩码
    n_unsigned = n & mask  # 将数值视为无符号整数（32位）
    return (n_unsigned >> shift) & mask  # 右移并应用掩码以确保结果在32位范围内


# 无符号右移示例
x = -8  # 同样的数值 -8，但在无符号右移中，我们将其视为一个无符号整数
print(f"原始数值（十进制）: {x}")
y_unsigned = unsigned_right_shift(x, 2)  # 模拟无符号右移两位
print(f"无符号右移两位后（十进制）: {y_unsigned}")
