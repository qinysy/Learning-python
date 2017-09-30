#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang


username=input('请输出你的用户名: ')
print(username,type(username))

#在python2中有raw_input与python3的input是一个意思
#特点是：把所有用户的输入都转成字符串类型
#username=raw_input('please input your name: ')
#print(username,type(username))

#在python2中有input
#特点是：把用户输入什么类型,就存成什么类型
#x=input('>>: ')
#print(x,type(x))

#接受用户输入的用户名和密码
#user=input('用户名: ')
#password=input('密码: ')

#print(user)
#print(password)

import getpass
user=input('用户名: ')
password=getpass.getpass('密码: ')

#print('这是用户输入的用户名 ',user)
#print('这是用户输入的密码 ',password)

print('用户名是: %s 密码是: %s' %(user,password))


#猜年龄
age=21
inp=input('您来猜猜我的年纪: ')
res=int(inp)

if res > age:
	print('猜大了')
elif res < age:
	print('猜小了')
else:
	print('猜对了')
