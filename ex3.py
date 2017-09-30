#!/usr/bin/env python3
#coding: utf-8
#__author:qinzhang


#使用while循环输出123456 8910
#第一种
count = 1
while count < 11:
	if count == 7:
		count+=1
		continue;
	print(count)
	count+=1

#第二种
count=1
while count < 11:
	if count != 7:
		print(count)
	count+=1



#求1-100的所有数的和

count=1
sum=0
while count <= 100:
	sum+=count
	count+=1
print(sum)

#for循环
sum=0
for i in range(1,101):
	sum+=i
print(sum)

#输出1-100中的偶数
count=1
while count <= 100:
	if count % 2 == 0:
		print(count)
	count+=1

#1-4中的偶数和，奇数和之差
count=1
sum=0
while count <= 4:
	if count % 2 == 0:
		sum-=count
	else:
		sum+=count
	count+=1

print(sum)


count=0
while True:
	if count == 3:
		print('try too many times')
		break
	u=input('u>>: ')
	p=input('p>>: ')
	if u == 'qinzhang' and p == '123':
		print('login ok')
		break
	count+=1
