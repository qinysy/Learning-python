#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#字典定义的基本形式: key:value
d={'name':'egon','age':18} 
d=dict({'name':'egon','age':18})


print(id(d),type(d),d)
#定义字典需要注意的问题：key必须是不可变类型，或者说是可hash类型
print(hash(1))
print(hash('xxxxxx'))
print(hash((1,2,3)))
#print(hash({'a':1}))

d={1:'id','a':1,'b':2,'name':'egon',(1,2):'aaaaaaaa'}
#字典的取值，字典是无序的
print(d[1])
print(d['name'])
print(d[(1,2)])


d={'name':'alex','age':18}
print(d['name'])
d['name']='aaaaasb'
print(d)

#循环
d={'name':'alex','age':18,'sex':'male','height':130,'weight':200}

print(d.keys())
print(d.values())
print(type(d.keys()))

for k in d:
	print(k,d[k])

l=[1,2,3]
for i in l:
	print(i)

t=(1,2,3)
for i in t:
	print(i)

s='hello'
for i in s:
	print(i)

'''
一：可变不可变
    可变：列表，字典
    不可变：数字，字符串，元组

二：存放值的个数
    一个值：数字，字符串
    多个值(容器类型)：列表，元组，字典

三：取值方式
    直接取值：数字
    序列类型：字符串，元组，列表
    映射类型：字典
'''

#字典的嵌套使用
d={'a':1}
#print(d['b'])
print(d.get('a'))

user_info=[
	{'username':'egon','password':'123'},
	{'username':'alex','password':'alex3714'},
	{'username':'yuanhao','password':'sb123'},
]
for item in user_info:
	print(item['username'],item['password'])

tag=True
while tag:
	user=input('u>>: ')
	pwd=input('p>>: ')
	for item in user_info:
		if user == item['username'] and pwd == item['password']:
			print('login ok')
			tag=False
			break
user_info=[
	{'username':'egon','password':'123'},
	{'username':'alex','password':'alex3714'},
	{'username':'yuanhao','password':'sb123'},
]

user_dic={
	'egon':'123',
	'alex':'alex3714',
	'yuanhao':'sb123'	
}

print('egon' in user_dic)

while True:
	user=input('u>>: ')
	pwd=input('p>>: ')
	if user in user_dic:
		if pwd == user_dic[user]:
			print('login ok')
			break




