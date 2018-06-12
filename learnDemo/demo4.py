# ==============>if else
if 4 > 5:
    print("aa")
else:
    print("bb")
# bb

# elif 是else if 的意思，和Java一样
a = 5
if a == 3:
    print('a是3')
elif a == 4:
    print('a是4')
elif a == 5:
    print('a是5')
else:
    print("爱多少多少")
# a是5

print('----------------------------')

# ==========>input 键盘输入

# age = input('请输入age：')
# age2 = int(age)
# print(age)
#
# if age2 < 33:
#     print("年龄小于33,输入值为："+age)
# else:
#     print("年龄大于33，输入值为："+age)

print('----------------------------')

# ===========>for循环

# 遍历输出
a = [1, 3, 4, 3, 42]
for ai in a:
    print(ai)

# 遍历求和
sum = 0
for ai in a:
    sum = sum + ai
print(sum)
# 53

# range()函数，生成整数序列，如 rang(1000) 生成0,1,2,3,4...1000之间的整数序列，不含1000
# 计算0到1000之间数字的和 不包含1000
sum2 = 0
list2 = range(1000)
for ai in list2:
    sum2 = sum2 + ai
print(sum2)
# 499500

# list()函数 将其转为list集合
list3 = list(range(14))
print(list3)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
