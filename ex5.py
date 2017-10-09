#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#计算密集型任务
import threading
import time

def foo(n):
	ret=0
	for i in range(n):
		ret+=1
	print(ret)

def bar(n):
	ret=1
	for i in range(1,n):
		ret*=i
	print(ret)

s=time.time()

foo(10000000)
bar(100000)

#t1=threading.Thread(target=foo,args=(100000000,))
#t1.start()

#t2=threading.Thread(target=foo,args=(100000000,))
#t2.start()

#t1.join()
#t2.join()

print("cost time:",time.time()-s)

