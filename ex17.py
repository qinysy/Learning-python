#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang


import time
import random
def init(func):
    def wrapper(*args,**kwargs):
        g = func(*args,**kwargs)
        next(g)
        return g
    return wrapper

def producer(target,count):
    for i in range(count):
        time.sleep(random.randrange(1,4))
        x='baozi%s' % i
        print('\033[45m厨师造好的包子：%s\033[0m' % x)
        target.send(x)



@init
def consumer(name):
    while True:
        food = yield
        time.sleep(random.randrange(1,4))
        print('\033[46m%s start to eat %s\033[0m' % (name, food))

producer(consumer('alex'),10)




