#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#链式赋值
x=y=z=1

#增量赋值
x+=1

#变量的解压

a,b,c,d,e='hello'
a,*_,e='hello'
print(a,e)

a,*_=[1,2,3,4]
print(a)

k,v=(1,2)
print(k,v)

d={'x':1,'x':2}
print(d)


res="Name:%s" %'egon'
print(res,type(res))

res="Age:%s" %100
print(res,type(res))

res="Age:%d" %100
print(res,type(res))


#res="Age:%d" %'eeee'
#print(res,type(res))

#count=1
#while count < 10:
#	print(count)
#	continue
#	count+=1
#else:
#	print('=========>')

for i in range(10):
	print(i)
	if i ==3:
		break
else:
	print('=======>')

names=['egon','alex','egon','wupeiqi']
res=[]
print(list(set(names)))

#True和False
print(type(True))

count=10
print(bool(count > 10))

#所有的数据类型自带布尔值,只有0，None,空的布尔值为False

l=[]
if len(l) == 0:
	print('列表为空')

print(bool(l))
if not l: #bool(l)
	print('列表为空')

print(bool(112.3123123123))
print(bool(-1111))
print(bool(0))

print(bool([1,2,3]))


#while 1:
#	cmd=input('>>: ')
#	if not cmd:
#		continue
#	print('=======cmd',cmd)


python_1=['egon','alex','钢蛋','老王']
linux_1=['alex','钢蛋','欧德博爱','艾里科四']

res=[]
for i in python_1:
	if i in linux_1:
		res.append(i)
print(res)

res=[]
for i in python_1:
	if i not in linux_1:
		res.append(i)
print(res)

#集合的作用一:关系运算
#集合的作用二:去重

#定义集合:
#集合内的元素必须是唯一的:
#集合内的元素必须是可hash的，也就是不可变类型
#集合是无序的
s={'egon',123,'egon','1'} #s=set({'egon',123,'egon','1'} )
print(s,type(s))

#s={'1',1,[1,2]}
s={'1',1,(1,2),'a','b'}
print(s)

#循环
s={'1',1,(1,2),'a','b'}
for i in s:
	print(i)

#关系运算
python_s={'egon','alex','钢蛋','老王'}
linux_s={'alex','钢蛋','欧德博爱','艾里科四'}

#取共同部分:交集
print(python_s & linux_s)
#取所有报名学习的学生:并集
print(python_s|linux_s)

#取只报名了python课程的学生：差集
print(python_s - linux_s)

#取只报名了linux课程的学生:差集
print(linux_s - python_s)

#取没有同时报名python和Linux课程的学生：对称差集
print(linux_s ^ python_s)

#集合方法
python_s={'egon','alex','钢蛋','老王'}
linux_s={'alex','钢蛋','欧德博爱','艾里科四'}

print(python_s.intersection(linux_s))#交集: python_s & linux_s
print(python_s.union(linux_s))#并集
print(python_s.difference(linux_s))#python_s-linux_s
print(python_s.symmetric_difference(linux_s))#对称差集 linux_s ^ python_s

python_s={'egon','alex','钢蛋','老王'}
linux_s={'alex','钢蛋','欧德博爱','艾里科四'}
python_s.difference_update(linux_s)
print(python_s)

s1={'a',1}
s2={'a','b',2}

s1.update(s2)
print(s1)

s1={'a',1}
s1.add(1)
print(s1)

s1.discard('a')
s1.discard('b')
print(s1)

#s1.remove('bbbbbbb')
print(s1)

#输出和想象中不一样
s1={'a',1,'b','c','d'}
print(s1.pop())

s1={1,2,}
s2={1,2,3}
print(s1.issubset(s2))
print(s2.issuperset(s1))


s1={1,2,'a'}
s2={1,2,3}

print(s1.isdisjoint(s2))
s1={'a','b'}
s2={'c','d'}
print(s1.isdisjoint(s2))




