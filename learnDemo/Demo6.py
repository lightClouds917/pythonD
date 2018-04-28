'函数相关'

__author__ = 'momo'

import sys

# 简单函数
print(abs(-12))
print(max(1,4,34,-23))
print(min(1,-3,-3,45,0))
print('----------------------')
print('----------------------')
print('----------------------')
# 数据类型转换
print(int('123'))
print(int(2.5435))
print(str(24))
print(str(34.33))
print('---------下面三个都是true-------------')
print(bool(1))
print(bool(-1))
print(bool('ss'))
print('----------下面三个都是false------------')
print(bool(0))
print(bool(''))
print(bool(None))
print('----------自定义函数------------')
# 自定义绝对值函数
def my_abs(x):
    if x >= 0:
        print('是正数：', x)
    else:
        print('是负数', -x)
my_abs(-1)




