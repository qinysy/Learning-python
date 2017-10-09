#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

import threading
import time

def foo(n):
	time.sleep(n)
	print("foo....%s" % n)

	print(threading.activeCount())
	
def bar(n):
	time.sleep(n)
	print("bar......%s" % n)

s=time.time()
t1=threading.Thread(target=foo,args=(2,))
#t1.setDaemon(True)
t1.start()


t2=threading.Thread(target=bar,args=(6,))
#t2.setDaemon(True)
t2.start()

t1.join()   #阻塞主线程
t2.join()

print("++++++",threading.activeCount())
print("ending!")
print("cost time:",time.time()-s)

# foo(4)
# foo(5)

