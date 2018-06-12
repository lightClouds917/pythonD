'函数的参数'
import math
# 二次方
def my_power2(x):
    return x*x
print(my_power2(5))

# 三次方
def my_power3(x):
    return x*x*x
print(my_power3(5))

# n次方 (n > 0)
def my_powern(x,n):
    if not isinstance(n,(int)):
        raise TypeError('参数类型错误')
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
print(my_powern(2,5))

# 默认参数使用
def my_powern2(x,n=2):
    if not isinstance(n,(int)):
        raise TypeError('参数类型错误')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 传入一个参数，默认参数n=2
print(my_powern2(3)) # 9
# 传入两个参数，n显性传入后，n=3
print(my_powern2(3,3)) # 27


# 默认参数的坑
# 打个断点很容易理解，内存中的这个l变量，每调用一次其实都发生变化了，所以再次调用时尽管参数还是默认的l，但l其实已经变了
print('---add_element---')
def add_element(l=[]):
    print(l)
    l.append('good')
    return l


print(add_element([1,2])) # [1, 2, 'good']
print('默认参数第一次---',add_element()) # ['good']
print('默认参数第二次---',add_element()) # ['good', 'good']
print('默认参数第三次---',add_element()) # ['good', 'good', 'good']

# 解决上面的默认参数的坑
print('---add_element2---')
def add_element2(l=None):
    print(l)
    l.append('good')
    return l
# 这样每次调用时，l都被重置为None了，就不会出现上面的问题了，但本例测试是不能再默认参数调用了，因为None没有append方法
print(add_element([1,2])) # [1, 2, 'good']

# 可变参数：*
# *listn表示：把listn这个list中的所有元素作为可变参传入函数，这些参数在调用时会自动封装为tuple


# 计算a²+b²+c²+d²...... 方法一
def sum_square(listn):
    sum1 = 0
    for n in listn:
        sum1 = sum1 + n*n
    return sum1
# 调用时先得封装list或者tuple作为参数
print(sum_square([1,2,3,4]))
print(sum_square((1,2,3)))

# 计算a²+b²+c²+d²...... 方法二 可变参数
def sum_square2(*listn):
    sum1 = 0
    for n in listn:
        sum1 = sum1 + n*n
    return sum1
# 直接传入任意多个参数即可，不需要封装list或者tuple
print(sum_square2(1,2,3,4))
print(sum_square2(1,2,3))
# 用已经构造好的list或者tuple掉用可变参 方式一
tuple1 = (0,1,3)
print(sum_square2(tuple1[0],tuple1[1],tuple1[2]))
# 上面的也是可以得，就是太麻烦，用*把已经构造好的list或者tuple转为可变参 方式二
print(sum_square2(*tuple1))

# 关键字参数

def person(name,age,**others):
    if others is None or len(others) == 0:
        print('name:',name,'age:',age)
    else:
        print('name:',name,'age:',age,'others:',others)


person('汪汪',23)
person('张三',24,province='浙江',city='杭州')
other1 = {'school':'浙江大学','major':'计算机'}



