#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang

#r模式,默认模式,文不存在则报错

f=open('a.txt',encoding='utf-8')
#print('first-read:',f.read())
#print('seconde-read: ',f.read())

#rint(f.readline(),end='')
#print(f.readline(),end='')

print(f.readlines())
#print(f.write('asdfasdfasdfasdfasdf'))
f.close()

#w模式，文不存在则创建,文件存在则覆盖
f=open('a.txt','w',encoding='utf-8')
f.write('1111111\n22222\n3333\n')
f.write('2222222\n')

f.writelines(['11111\n','22222\n','3333\n'])
f.close()

#a模式，文不存在则创建，文件存在不会覆盖，写内容是追加的方式写
f=open('a.txt','a',encoding='utf-8')
f.write('\n444444\n')
f.write('5555555\n')
f.close()

#其他方法
f=open('a.txt','w',encoding='utf-8')
f.write('asdfasdf')
f.flush()  #把内存数据刷到硬盘
f.close()
print(f.closed)
#f.readlines()

print(f.name,f.encoding)
#print(f.readable())
#print(f.writable())

f=open('c.txt','r',encoding='utf-8')
print(f.read(3))
print('first_read: ',f.read())
f.seek(0)
print('second_read: ',f.read())
f.seek(3)
print(f.tell())
print(f.read())

f=open('c.txt','w',encoding='utf-8')
f.write('1111\n')
f.write('2222\n')
f.write('3333\n')
f.write('444\n')
f.write('5555\n')
f.truncate(3)

f=open('a.txt','a',encoding='utf-8')
f.truncate(2)

#r w a; rb wb ab
f = open('a.txt','rb')
print(f.read())
print(f.read().decode('utf-8'))
f.close()

f = open('a.txt','wb')
print(f.write('你好啊'.encode('utf-8')))
f.close()

f = open('a.jpg','rb')
print(f.read())

read_file=open('a.jpg','rb')
write_file=open('a.copy.jpg','wb')
write_file.write(read_file.read())

import os 
read_f = open('a.txt','r',encoding='utf-8')
write_f = open('a.txt.swp','w',encoding='utf-8')

l = read_f.readlines()
for i in range(len(l))
	print(l(i))

for line in read_f:
	if 'alex' in line:
		#先改,在写入write_f
		line=line.replace('alex','ALEXSB')
		write_f.write(line)
	else:
		#直接写入write_f
		write_f.write(line)

read_f.close()
write_f.close()
os.remove('a.txt')
os.rename('.a.txt.swp','a.txt')

#上下文管理with
# read_f=open('a.txt','r',encoding='utf-8')
# write_f=open('.a.txt.swp','w',encoding='utf-8')
with open('a.txt','r',encoding='utf-8') as read_f,\
        open('.a.txt.swp','w',encoding='utf-8') as write_f:
    for line in read_f:
        if 'alex' in line:
            line=line.replace('alex','ALEXSB')
        write_f.write(line)
os.remove('a.txt')
os.rename('.a.txt.swp','a.txt')
