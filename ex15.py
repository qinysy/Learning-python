#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

import time
import random
#装饰器
def timmer(func):
	def wrapper():
		start_time = time.time()
		func()
		stop_time = time.time()
		print('run time is %s' % (stop_time-start_time))
	return wrapper

#被装饰函数
@timmer
def index():
	time.sleep(random.randrange(1,5))
	print('welecome to index page')
@timmer
def home():
	time.sleep(random.randrange(1,3))
	print('welecome to index page')
	
#index = timmer(index)
#index()
index()

#加多个装饰器
def timmer(func):
	def wrapper():
		start_time = time.time()
		func()
		stop_time = time.time()
		print('run time is %s' % (stop_time-start_time))
	return wrapper
def auth(func):
	def deco():
		name = input('name: ')
		passwd = input('password: ')
		if name == 'qinzhang' and passwd == '123456':
			print('login successful')
			func()
		else:
			print('login err')
	return deco
#被装饰函数
@auth
@timmer
def index():
	time.sleep(3)
	print('welecome to index page')

@auth
@timmer
def home():
	time.sleep(random.randrange(1,3))
	print('welecome to HOME page')

index()
home()

#装饰器修订
#装饰器
def timmer(func):
	def wrapper(*args,**kwargs):
		start_time = time.time()
		res = func(*args,**kwargs)
		stop_time = time.time()
		print('run time is %s' % (stop_time-start_time))
		return res
	return wrapper
#被装饰函数
@timmer #index = timmer(index)
def index():
	time.sleep(random.randrange(1,5))
	print('welecome to index page')
@timmer
def home(name):
	time.sleep(random.randrange(1,3))
	print('welecome to %s HOME page' % name)
	return 123123123123123123123123123123123123123123

index()
res1 = index()
print('welecome to %s HOME page' % res1)
res2 = home('egon') #wraper()
print('home return %s' %res2)

	
