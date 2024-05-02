# 定义一个十进制数
decimal_number = 123
print(f"十进制表示：{decimal_number}")
# 转换为二进制
binary_number = bin(decimal_number)
print(f"二进制表示: {binary_number}")  # 输出类似 '0b1111011'

# 转换为八进制
octal_number = oct(decimal_number)
print(f"八进制表示: {octal_number}")  # 输出类似 '0o173'

# 转换为十六进制
hexadecimal_number = hex(decimal_number)
print(f"十六进制表示: {hexadecimal_number}")  # 输出类似 '0x7b'

# 去掉前缀
binary_number_clean = binary_number[2:]
octal_number_clean = octal_number[2:]
hexadecimal_number_clean = hexadecimal_number[2:]

print(f"无前缀二进制表示: {binary_number_clean}")
print(f"无前缀八进制表示: {octal_number_clean}")
print(f"无前缀十六进制表示: {hexadecimal_number_clean}")
