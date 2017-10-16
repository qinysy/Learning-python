#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#定义列表
l=[1,'a',[3,4]]  #l=list([1,'a',[3,4]])

#取值
print(l[0])
print(l[2][0])

l=[1,2,[['a','b'],'c']]
print(l[2][0][1])

#循环
l=[1,2,3,[4,5]]

count=0
while count < len(l):
	print(l[count])
	count+=1

for count in range(len(l)):
	print(l[count])
l=[1,2,3,[4,5]]
for count in range(len(l)):
	if type(l[count]) is list:
		#pass
		for i in range(len(l[count])):
			print(l[count][i])

	else:
		print(l[count])

l=[1,2,3,[4,5]]
l_size=len(l)
for index in range(l_size):
	value=l[index]
	if type(value) is list:
		#value是列表,value=[4,5]
		for i in range(len(value)):
			print(value[i])
	else:
		#value不是列表,直接打印
		print(value)



print('没有修改之前的列表: ',id(l),type(l),l)

#id不动，type也不动，value被修改了，则称为可变类型
#可变指的是：在id和type不动的前提下,值可变

print(l[0])
print(l[3][1])
l[0]=11111111111111111
print(1)
print('修改之后的列表: ',id(l),type(l),l)



#列表常用操作
#索引
#切片
l=['ab',1,2,'hello']
print(l[1:3])  #切片操作是读操作,并不会修改原来的数据
print(l)


#追加
l=['ab',1,2,'hello']
print(l)
l.append('alex')
l.append('alex1')
l.append('alex2')
l.append('alex3')
print(l)
#插入
l.insert(0,'first')
print(l)
l.insert(2,'abc')
print(l)
#删除
l=['a','b','c','hello']
print(l)
l.pop(1)
print(l)
l.pop()
l.pop()

l.pop(0)
#l.pop(0)
#print('刚刚删除的元素是',l.pop(0))

print(l)

#队列: 先进先出
l=[]
#append与pop()
#入队列
l.append('people1')
l.append('people2')
l.append('people3')
print(l)
#出队列
print(l.pop(0))
print(l.pop(0))
print(l.pop(0))

#insert(0,item)
#入队
l.insert(0,'people1')
l.insert(0,'people2')
l.insert(0,'people3')
print(l)


#出队
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)

#堆栈：先进后出，或者说后进的先出
l=[]
l.append('people1')
l.append('people2')
l.append('people3')
print(l)

print(l.pop())
print(l.pop())
print(l.pop())

l=[1,2,3]

print(len(l))

#切片
#循环
#包含

s='alex is sb'
print('sb' in s)

names=['alex','egon','yuanhao']
print('yuanhao' in names)

#列表的其他操作
l=list(['a1','a2','a3'])

print(l)
print(l.index('a2'))

l.append('a2')
print(l.count('a2'))

print(l)
l.extend([1,2,3])
print(l)
l.extend([1,2,3])
print(l)

l.remove('a2')
print(l)

l=[2,3,1]
l.sort(reverse=True)
print(l)

l=['a','c','alex']
l.reverse()
print(l)

