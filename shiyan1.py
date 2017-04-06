#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####一元二次方程的解
import math
def a(a,b,c):
	m=math.sqrt(b**2-4*a*c)
	x1=(-b+m)/(2*a)
	x2=(-b-m)/(2*a)
	return x1,x2

print (a(1,3,-4))

# 斐波那契数列

def a(max):
	n,a,b=0,0,1
	while n<max:
		print (b)
		a,b=b,a+b
		n=n+1
	return 'done'

print (a(100))


#把‘123.456’变为123.456整形数据

from functools import reduce

def a(s):
	def b(m,n):
		return m*10+n
	x=s.index('.')     #利用 index() 函数确定字符串 S 中 ‘.’的位置
	S1=list(map(int,[i for i in s[:x]]))   #分割整数部分
	S2=list(map(int,[i for i in s[x+1:]]))   #分割小数部分

	#先利用切片把我们传入的 str 分成以前以后两个部分
	#（其实就是根据小数点分成整数和浮点数，分别处理）
	#然后再把切割好的 str 利用 int 变成整数
	#map() 函数负责把 int 作用到截取的 str 的每个元素中去。 
	return reduce(b,S1)+reduce(b,S2)/10**len(S2)  #根据位数len()来添加小数点

print (a('123.456'))

#生成一个素数序列！！
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def a():     #生成一个奇数序列
	n=1
	while True:
		n=n+2
		yield n

def shaixuan(n):     #定义一个筛选函数
	return lambda x:x%n>0

def primes():     #定义生成器，不断返回下一个函数
	yield 2
	it=a()
	while True:    #在每一次循环中对奇数序列进行筛选
		n=next(it)
		yield n
		it=filter(shaixuan(n),it)

for x in primes():
	if x<1000:
		print(x)
	else:
		break



