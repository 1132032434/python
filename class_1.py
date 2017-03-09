#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''print(85-72,'%个百分点')


classList = ['a','b','c']
print(classList)
write_e = input()
classList.insert(3,write_e)
print(classList)
classList.pop()
print(classList)
classList.append(input())
print(classList)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#打印apple
print(L[0][0])
#打印python
print(L[1][1])
#打印Lisa
print(L[2][2])

print('验证if判断')
age = 3
if age>18:
	print('adult')
elif age >=6:
	print('teenager')
else:
	print('kid')
	
x = 0
if x:
	print('true');
else:
	print('false');
	
	birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')
'''


sum = 0;
#for x in [1,2,3,4,5,6,7,8]:
#	sum = sum +x
#print(sum)	
	
#range(5)是从0开始。所以加100要写101	
print(list(range(5)))

for x in list(range(101)):
	sum += x
print(sum)
	
#while 循环
#python3 的if，while，for 等 ： 号很重要，切记缩进
#好处要求了python 的写法必须规范。
n= 1
while n<10:
	n +=1
	if n==5 :
		continue
	print(n)
	
print('end')

print('---------------------------------------')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)