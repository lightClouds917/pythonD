'函数相关'

__author__ = 'momo'

import sys
import math

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
# 空函数
def my_a(a):
    if a < 5:
        print('a<5')
    else:
        pass


my_a(21)


# 自定义绝对值函数
def my_abs(x):
    if x >= 0:
        print('是正数：', x)
    else:
        print('是负数', -x)


my_abs(-1)
# my_abs('12')  TypeError: '>=' not supported between instances of 'str' and 'int'


print('----------自定义函数  检查参数类型------------')
def my_abs2(z):
    if not isinstance(z,(int,float)):
        raise TypeError("错误的数据类型")
    if z <= 0:
        return -z
    else:
        return z
print(my_abs2(-13))
# print(my_abs2("fs"))      TypeError: 错误的数据类型


print('----------函数返回多个值------------')
# 一个函数返回多个值，实质上是返回了一个tuple，在语法上，返回一个tuple可以省略括号，多个变量可以同时接收一个tuple,按照位置顺序对应赋值
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

a = move(100,100,60,math.pi/6)
print(a) # (151.96152422706632, 70.0)
x,y = move(100,100,60,math.pi/6)
print(x,y) # 151.96152422706632 70.0

# eg:返回list的长度
def testlist(a):
    if not isinstance(a,list):
        raise TypeError("参数类型错误")
    if len(a) < 3:
        return 'list太短了',len(a)
    else:
        return 'list太长了',len(a)

lista = [1,3,'aa','b']
mes,count = testlist(lista)
print(mes,count) # list太长了 4
print('--------------------')

# eg:定义函数，返回方程 ax2 + bx + c = 0 的根

print('----------求解ax2 + bx + c = 0 的根------------')

def my_quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number,please try again')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number,please try again')
    if not isinstance(c,(int,float)):
        raise TypeError('b is not a number,please try again')
    d = b*b - 4*a*c
    if d < 0:
        return 'b*b-4*a*c= ',d,'<0,方程无解'
    else:
        if a == 0:
            if b == 0:
                if c == 0:
                    return '方程解为全体实数'
                else:
                    return '方程无解'
            else:
                x1 = -c/b
                x2 = x1
                return x1,x2
        else:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            return x1,x2

print(my_quadratic(2,3,1))  #   (-0.5, -1.0)
print(my_quadratic(1,3,-4)) #   (1.0, -4.0)
print(my_quadratic(2,2,5))  #   ('b*b-4*a*c= ', -36, '<0,方程无解')

