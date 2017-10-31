#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#形参与实参
def foo(x,y):
	return x+y

foo(1,2)

#位置参数：按照从左到右的顺序依次定义的参数
def foo(x,y):
	print(x)
	print(y)
#按位置定义的形参，必须被传值，多一个不行，少一个不行
#foo(1,2,3)

#按位置定义的实参,与形参一一对应
foo(2,10)
#关键字参数：实参在定义时，按照key=value形式定义
def foo(x,y):
	print(x)
	print(y)

foo(y=10,x=1) #关键字参数可以不用像位置实参一样与形参一一对应，指名道姓地传值

def foo(x,y,z):
     print(x)
     print(y)
     print(z)
 # foo(1,z=20,10)
foo(1,y=2,z=10)
#注意的问题一：位置实参必须在关键字实参的前面
#注意的问题二：实参的形式既可以用位置实参又可以是关键字实参，但是一个形参不能重复传值


