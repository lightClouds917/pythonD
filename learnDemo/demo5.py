# ===============>调用函数

# abs 绝对值
print(abs(-2.34))
# 2.34

# 把函数赋值给变量
my = abs
print(my(-343))
# 343

# 最大值
print(max([23,23,54,255]))
# 255

print(hex(32))
# 0x20

# ===============>类型转换

print(str(1.23))
# 1.23

print(int('14'))
# 14

print(bool(1))
# True

print(bool(0))
# False

print(bool(-123))
# True

print('-------------------------')
# ===============>定义函数

# 自定义绝对值函数
def my_abs(a):
    if a <= 0:
        return -a
    else:
        return a

print(my_abs(-45))
print(my_abs(33))

# print(abs('as'))     会报错： TypeError: bad operand type for abs(): 'str'

# print(my_abs('af'))  会报错： TypeError: '<=' not supported between instances of 'str' and 'int'

# 对自定义函数做个参数类型限制

def my_abn_new(a):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand')
    if a <= 0:
        return -a
    else:
        return a

print(my_abn_new(-7238))


def my_len(str):
    if len(str)>5:
        return '长度大于5'
    else:
        return '长度小于5'

print(my_len('aa'))

# =================>pass语句
