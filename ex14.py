#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

name = 'alex'
def func():
	name = 'egon'
	def bar():
		print(name)
	return bar

b = func()
print(b)
name = 'hahahahahahahahahahahhaha'

def foo():
     name='ssssssssssssssssssssssssssssssssssssssss'
     b()

foo()




# name='alex'
# def func():
#     name='egon'
#     def bar():
#         print(name)
#     return bar
#
# f=func()





# name='alex'
# def func():
#     name='egon'
#     x=1000000000000000000000
#     def bar():
#         print(name)
#         print(x)
#         a=1
#         b=2
#     return bar
# #
# f=func()
#
# # print(f.__closure__[0].cell_contents)
# print(f.__closure__[1].cell_contents)


# name='alex'
# def func():
#     name='egon'
#     x=1000000000000000000000
#     def bar():
#         print(name)
#         print(x)
#         a=1
#         b=2
#     print(bar.__closure__)

# func()

#闭包函数：1 内部函数  2 包含对外部作用域而非全局作用域的引用
#闭包函数的特点：
    # 自带作用域
    # 延迟计算
# name='alex'
# def func():
#     def bar():
#         print(name)
#     return bar
#
# f=func()
# print(f.__closure__)
#
# f()

#
#
# money=1000
# def tell_ino(name):
#     print('%s have money %s' %(name,money))
#
# tell_ino('egon')
#
# def f1():
#     money=10
#     tell_ino('egon')
#
# f1()

#
# money=1000
# def f1():
#     money=10
#     def tell_ino(name):
#         print('%s have money %s' %(name,money))
#     tell_ino('egon')
#
# f1()




#包一层
def wrapper():
    money=1000
    def tell_info():
        print('egon have money %s' %(money))
    return tell_info

tell_info=wrapper()

def foo():
    money=100
    tell_info()

# foo()


#包两层

# def aaa():
#     name='egon'
#     def wrapper():
#         money=1000
#         def tell_info():
#             print('egon have money %s' %(money))
#             print('my namn is %s' %name)
#         return tell_info
#     return wrapper
#
# w=aaa()
# tell_info=w()
# print(tell_info.__closure__[0].cell_contents)
# print(tell_info.__closure__[1].cell_contents)








'''
报错NameError: name 'money' is not defined

原因：
    函数的作用域关系在函数定义阶段就已经固定，与调用位置无关
    无论函数在何处调用，都需要回到定义阶段去找对应的作用域关系
    此例：虽然tell_info('egon')是在foo内调用并且引用money，但仍需要回到定义
    tell_info的阶段去找作用域关系，而定义时tell_info引用的money就是全局的money
    如果全局不存在则抛出异常NameError

'''


#定义闭包函数的基本形式


# def 外部函数名():
#     内部函数需要的变量
#     def 内部函数():
#         引用外部变量
#     return 内部函数

# def deco(x):
#     def wrapper():
#         print(x)
#
#     return wrapper
#
# wrapper=deco()
#
# print(wrapper)





# def wrapper():
#     print(x)
#     print(y)

# def deco1():
#     y=2
#     def deco():
#         x=1
#         def wrapper():
#             print(x)
#             print(y)
#
#         return wrapper
#     return deco
#
#
#
# deco=deco1()
#
# wrapper=deco()
#
#
#
#
#
# wrapper()


from urllib.request import urlopen

# print(urlopen('http://www.xiaohua100.cn/').read())
#print(urlopen('https://www.python.org').read())

# def get(url):
#     return urlopen(url).read()
#
#
#print(get('http://www.xiaohua100.cn/'))
#
# def index(url):
#     # url='http://www.xiaohua100.cn/'
#     def get():
#         return urlopen(url).read()
#     return get
#
#
# xiaohua=index('http://www.xiaohua100.cn/')
#
#
#
# python=index('https://www.python.org')
#
#
# baidu=index('http://www.baidu.com')
#
#
# print(python())
globals()
