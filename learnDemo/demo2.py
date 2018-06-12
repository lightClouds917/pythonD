# ==============>字符串相关
# #后内容为注释，或者是它下方打印语句的打印结果


# ''   ""  括起来的都是字符串，没有区别
print('aaaaa')
print("bbbb")
print('aa"b"')

# 转义’    aa'
print('aa\'')

# 转义\    aa\b
print('aa\\b')

# 不转义 r'' 内部的不转义    k\\   ！！！有疑问
print(r'k\\')

# 换行 \n
print('aaaaaa\nbbbbbb')

# 多行'''内容'''
print('''cccc
dddd
gggg''')

# ==============>布尔值\

# False
print(3>5)

# True
print(3<6)

# True
print(3>2 and 5>3)

# False
print(3>2 and 5<3)

# True
print(3>2 or 5<3)

# True
print(not False)

# 真的
if 3>2:
    print("真的")
else:
    print("假的")


# ===============

# 5
a=5
print(a)

# 杰哈德
a='杰哈德'
print(a)

# True
a=True
print(a)

a = 'ABC'
b = a
a = 'XYZ'

# ABC
print(b)

# XYZ
print(a)

ALI_ADDRESS='ALI_ADDRESS=www.alibaba.com'
print(ALI_ADDRESS)

# =================> 除法

# / 除法

# 3.7037037037037037  除不尽有小数
a=100/27
print(a)

# // 地板除

# 3  永远只保留整数部分
b=100//27
print(b)

# % 取余  获得两个数相除的余数

# 19  100/27=3...19
c=100%27
print(c)

