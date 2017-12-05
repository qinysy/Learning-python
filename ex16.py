#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

import os
#内置函数 all(iterable)
#如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
# 注意：空元组、空列表返回值为True，这里要特别注意。
print(abs(-9))           #9
print(all([1,2,3,4]))    #True
print(all([1,2,3,0]))    #False
print(all([1,2,3,None])) #False
print(all([1,2,3,'']))   #False
print(all([]))           #True

print(all(i for i in range(1,3))) #True


print(any('')) #False


print(bin(3))
print(oct(9))
print(hex(13))
print(hex(15))
print(hex(16))

print(bool(0))
print(bool(None))
print(bool(''))

#print(bytes('sss',encoding='utf-8')) #python3
print('sss'.encode('utf-8'))


def func():pass
print(callable(func))

print(chr(66))
print(ord('B'))

x=1-2j
x=complex(1-2j)
print(x.real)
print(x.imag)
int
dict
list
tuple
set
str



import os

print(dir(os)) #os.walk

print(help(os))

def func():
    'my function'
    pass
print(help(func))