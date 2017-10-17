#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#元组的元素可以是任意数据类型
t=('a',1,'b',1,(3,4))
print(id(t),type(t),t)

#元组的特性是：不可变
#取值
print(t[4][0])

#循环
t=('a',1,'b',1,(3,4))
index=0
while index < len(t):
	print(t[index])
	index+=1

for i in range(len(t)):
	print(t[i])


#tuple类型的方法
print(t.count(1))
print(t.index('b'))


#tuple常用操作
# 索引
# 切片
t=('a',1,'b',1,(3,4))
print(t[1:3])
print(t)
#循环
#长度
print(len(t))
#包含
print('a' in t)

#元组的特性是：不可变，元组的元素可以是任意数据类型
t=(1,2,['a','b'])
print(id(t),type(t),t)
#元组里的列表可变
t[2][0]='aaaaaaa'
print(t)
print(id(t),type(t),t)

#t[2]=3
t[2][0]=123123123123
print(t)


#评论

comments=[('真傻比',),('确实傻逼',)]
print(comments)
comments.pop(0)
comments[0]='真牛逼'
print(comments)


