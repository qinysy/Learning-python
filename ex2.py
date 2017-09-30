#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang



n=1
f=1.3

print(type(n))
print(type(f))

print(1.3e-3)
print(1.3e3)

print(bin(10))
print(oct(10))

print(hex(10))

#数字类型的特点
#1.只能存放一个值

#2.意境定义，不可更改

#3.直接访问

x=10123123123
print(id(x))
x=11
print(id(11))


#字符串类型：引号包含的都是字符串类型
#需要掌握的常用操作：
'''
msg='hello'
移除空白 msg.strip()
分割msg.split('|')
长度len(msg)
索引msg[3] msg[-1]
切片msg[0:5:2] #0 2 4

'''

s='hello world'
s1="hello world"
s2="""hello world"""
s3='''hello world'''

print(type(s))
print(type(s1))
print(type(s2))
print(type(s3))

x='*****egon*****'

x=x.strip()
print(x)
print(x.strip('*'))

#首字母大写
x='hello'
print(x.capitalize())

#所有字母大写
x='hello'
print(x.upper())

#居中显示
x='hello'
print(x.center(30,'#'))

#统计某个字符的长度，空格也算字符
x='hel lo love'
print(x.count('1'))
print(x.count('1',0,4)) # 0 1 2 3

x='hello '
print(x.endswith(' '))
print(x.startswith(' '))

x='hello '
print(x.find('e'))
print(x.find('l'))

#格式化字符串
msg='Name:{},age:{},sex:{}'
print(msg)
print(msg.format('egon',18,'male'))

msg='Name:{0},age:{1},sex:{0}'
print(msg.format('aaaaaaaaaaaaaaaaa','bbbbbbbbbbbbbb'))

msg='Name:{x},age:{y},sex:{z}'
print(msg.format(y=18,x='egon',z='male'))



x='hello world'
print(x[0])
print(x[4])
print(x[5])
#print(x[100]) #报错

print(x[-1])
print(x[-3])
print(x[1:3])
print(x[1:5:2])

x='hello'
print(x.index('o'))
print(x[4])
print(x[x.index('o')])

x='123'
print(x.isdigit())

age=input('age: ')
if age.isdigit():
	new_age=int(age)
	print(new_age,type(new_age))

msg='hello alex'
print(msg.replace('x','X'))
print(msg.replace('alex','SB'))
print(msg.replace('l','A'))
print(msg.replace('l','A',1))
print(msg.replace('l','A',2))


#补充
#x='a' 
#x=str('a')
#str.replace()

x='hello    world alex SB'
x='root:x:0:0::/root:/bin/bash'
print(x.split(':'))




x='hello'
print(x.upper())
x='H'
print(x.isupper())

x='HELLO'
print(x.islower())
print(x.lower())

x='    '
print(x.isspace())
msg='Hello'
msg='hEEEE'
print(msg.istitle())

x='abc'
print(x.ljust(10,'*'))
print(x.rjust(10,'*'))

x='Ab'
print(x.swapcase())

x='hello'
print(x.title())
