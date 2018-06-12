# -*- coding: utf-8 -*-
__author__ = 'momo'

'字符串拼接'

# 1.用+拼接
print('aa'+"好的")    # aa好的
# print('aa'+34)  # TypeError: must be str, not int

# 2.用,拼接   ------>,处会多出一个空格
print('aa','好的')    # aa 好的
print('aa',34,'bb')     # aa 34 bb

# 3.直接写一起
print('aa''bb')     # aabb
print('aa'  'bb')   # aabb

# 4.用%拼接  %s会自动用右边的集合中元素替换
print('参数一:%s,参数二:%s'%('Jim', 'Green'))     #   参数一:Jim,参数二:Green
print('参数一:%s,参数二:%s'%('aa',34))    #   参数一:aa,参数二:34

# 5.用join拼接 只能是字符串
list1 = ['aa','bb','cc']
print(''.join(list1))   #   aabbcc
list2 = ['aa','bb','cc',34]
# print(''.join(list2))   #  TypeError: sequence item 3: expected str instance, int found

# 6.奇怪的方式
print(3*'abc')  #    abcabcabc

# 7.format 这个用法比较强大，网上很多，这里不再赘述