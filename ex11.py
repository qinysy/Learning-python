#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang


#一 为何要有函数？
#不加区分地将所有功能的代码垒到一起，问题是：
#    代码可读性差
#    代码冗余
#    代码可扩展差

#如何解决？
#函数即工具，事先准备工具的过程是定义函数，拿来就用指的就是函数调用

#结论：函数使用必须是：先定义，后调用



#二：函数的分类
#    1.内置函数:built-in
#    2.自定义函数:
#        def 函数名(参数1,参数2，...):
#            '''注释'''
#            函数体

print(len('asdfasdfasdf'))
print(len)

print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(sum([1,2,3,4,5]))

'''
************
************
************
hello world
************
************
************
'''

def print_tag(tag,count,line_num):
	for i in range(line_num):
		print(tag*count)

def print_msg(msg):
	print(msg)

print_tag('*',20,3)
print_msg('hello world')
print_tag('*',20,3)

#函数的使用:先定义，后调用
#如何定义函数之定义函数的三种形式
#1 定义无参函数：函数的执行不依赖于调用者传入的参数就能执行时，需要定义为无参函数
def print_tag():
	print('********************')

def main():
	print_tag('*',20,3)
	print_msg('hello world')
	print_tag('*',20,3)
#main()
#2 定义有参数：函数的执行需要依赖于调用者传入的参数才能执行时，需要定义为有参函数
def print_tag(tag,count,line_num):
	for i in range(line_num):
		print(tag*count)
#3 定义空函数：函数体为pass
def func(x,y,z):
	pass

def auth():
	'''用户认证'''
	pass

def get():
	'''download file'''
	pass

def put():
	'''upload file'''
	pass

def check_hash():
	'''check file hash value'''
	pass

#如何调用函数
def func():
	print('from func')

func()

def func1(x):
	print('from func',x)

func1(1111111)

def func():
	print('from func')
func()

res=func()
print(res)

def func():
	return 11111
	print('from func')

	return 222
	return 3333
res=func()
print(res)

def max2(x,y):
	if x > y:
		return x
	else:
		return y

res=10*max2(20,2)
res*=10
print(res)

def max2(x,y):
	if x > y:
		return x
	else:
		return y
res=max2(max2(11,23),100)
print(res)

