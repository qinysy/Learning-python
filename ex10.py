#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#字典的常用方法
d={'x':1,}
d.clear()
print(d)

#print(d['x'])
#print(d['y'])
print(d.get('y'))
print(d.get('y','找不到的啦'))
print(d.get('x','找不到的啦'))

d={'x':1,'y':1}
print(d.items())

for item in d.items():
	print(item)

for k,v in d.items():
	print(k,v)

d={'x':1,'y':1}
print(d.keys())

for i in d.keys():
	print(i)

for i in d:
	print(i)

d={'x':1,'y':1}
print(d.keys(),type(d.keys()))

res=list(d.keys())
print(res,type(res))

d={'x':1,'y':12222}
print(d.values())
print(list(d.values()))
print(list(d.values())[1])

res=d.pop('y')
print(res)
print(d)


d={'x':1,'y':12222}
print(d.pop('z','没有的啦'))


d={'x':1,'y':12222}
print(d.popitem())
print(d)


d={'x':1,'y':12222}
d.setdefault('z',3)
print(d)

d['name']='egon'
print(d)

d={'x':1,'y':12222}
print(d.setdefault('x',33333333333333333333333333333))
print(d)

d1={}
d2=dict()
print(d1,d2)

d3=dict(x=1,y=2,z=3)
print(d3)

d4=dict({'x':1,'y':2,'z':3})
print(d4)

d5=dict([('x',1),('y',2),('z',3)])
print(d5)

d6={}.fromkeys(['name','age'],None)
print(d6)

d7={}.fromkeys(['name','age'],['egon',18])
print(d7)

d={'name':'alex','sex':'male'}

d1={'name':'alexsb','age':50}
d.update(d1)
print(d)

#新增
d={}
d['x']=1
print(d)

#删除
d.pop('x')
#d.popitem()
#键丶值丶键值对
d.keys()
d.values()
d.items()

#循环

#长度
d={'x':1,'u':2}
print(len(d))

#成员运算
d={'x':1,'u':2}
print('x' in d)
print(1 in d.values())

