# ===========>list
# #后内容为注释，或者是它下方打印语句的打印结果


# 1.新建list
names = ['张三','李四','王五','赵六']
list2 = ['张三',True,4]
list3 = ['张三',55,list2]

# 打印结果如下，发现，list集合可以随便玩儿，类型不同可以，嵌套也可以

# ['张三', '李四', '王五', '赵六']
print(names)
# ['张三', True, 4]
print(list2)
# ['张三', 55, ['张三', True, 4]]
print(list3)

# len() 获取集合长度
print(len(names))

# 索引获取第几个元素(从0开始)
print(names[2])

# 获取最后一个元素可以用 [-1]
print(names[-1])

# 获取倒数第二个[-2],倒数第三个[-3]......
print(names[-2])

# 插入到末尾
names.append('末尾啊')
print(names)

# 插入到索引为2的位置
names.insert(2,'插入')
print(names)

# 删除末尾元素
names.pop()
print(names)

# 删除指定索引位置
names.pop(1)
print(names)

# 索引为1的替换为 '啦啦'
list2[1]='啦啦'
print(list2)

list2 = ['张三',True,4]
list3 = ['张三',55,list2]
# 从list3中获取True这个元素
print(list3[2][1])

# 获取55的索引
print(list3.index(55))

print('---------------------------')

# ================>tuple  元组，不变

# 定义tuple
t = (1,4,'sa','ad')
print(t)

# 只有一个元素且是数字时 这个（）会当运算符

# 4
a = (4)
print(a)

# 只有一个元素且是数字时 加个,，防止将（）误解为运算符

# (4,)
b = (4,)
print(b)

list3 = ['小红','小绿','小芬']
c = (4,36,list3,32,32,54,32,32)

# 获取32所在位置的索引 第一次出现时的
print(c.index(32))

# 计算32有多少个
print(c.count(32))

# 体会不变  不变是 指向不变

# (4, 36, ['小红', '小绿', '小芬'], 32, 32, 54, 32, 32)
print(c)

# (4, 36, ['小红', '小绿', '小芬', '白加黑'], 32, 32, 54, 32, 32)
list3.append("白加黑")
print(c)

print('---------------------------')

# ================>dict   字典,类似java中的map

# 定义dict
d1 = {'name':'张三','age':28,'address':'浙江'}

print(d1['address'])
# 浙江

# 判断是否存在 x in dict
if 'name' in d1:
    print('有name属性')
else:
    print('没有name属性')
# 有name属性

# 判断是否存在 get() 没有就是None
print(d1.get('name'))
# 张三

print(d1.get('city'))
# None

# 没有值就用自己定义的  get(x,b) 没有拿到x就把b的值给x
print(d1.get('province','山西省'))
# 山西省

# 删除一个值 pop()
d1.pop('age')
print(d1)
# {'name': '张三', 'address': '浙江'}


print('-------------------------------------')

# ================>set  类似java中的set

# 创建set  是无序集合
s = set([1,3,6,91,'aa'])
print(s)
# {1, 3, 6, 'aa', 91}

# 重复元素会自动过滤
s1 = set([22,64,22,64,8])
print(s1)
# {64, 8, 22}

# 添加元素
s.add('er')
print(s)
# {1, 3, 6, 'er', 91, 'aa'}

# 删除元素
s.remove(91)
print(s)
# {1, 3, 6, 'er', 'aa'}

s2 = set([22,54,12])
s3 = set([22,65,'li'])

# 交集
print(s2&s3)
# {22}

# 并集
print(s2|s3)
# {65, 54, 22, 'li', 12}


# 观察set的不重复性

list4 = [2,5,32]
s4 = ([2,42,'a',list4])
print(s4)
# [2, 42, 'a', [2, 5, 32]]

list4.append(54)
print(s4)
# [2, 42, 'a', [2, 5, 32, 54]]

list4.append(5)
print(s4)
# [2, 42, 'a', [2, 5, 32, 54, 5]]


# ======================>体验变化
list5 = [3,2,55,3,4,1]
list5.sort()
print(list5)
# [1, 2, 3, 3, 4, 55]

list5.sort(reverse=True)
print(list5)
# [55, 4, 3, 3, 2, 1]

st = 'abcde'
st2 = st.replace('b','B')
print(st)
# abcde

print(st2)
# aBcde
