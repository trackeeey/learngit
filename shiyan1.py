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

for x in primes():    #对于无限序列需要有退出序列的循环
	if x<1000:
		print(x)
	else:
		break


#判断是否为回数

def a(n):
	return str(n)==str(n)[::-1]
L=list(filter(a,range(1000)))
print (L)


#sorted 函数的用法-----高阶函数的强大抽象能力

print (sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
#key是作用于每一个项的函数，然后在进行排列
#reverse是正反向排序的参数

#isinstance(对象，数据类型)----来判断数据类型----True/False
#Interable----可迭代对象
#Iterator----迭代器----可以被next()函数调用的对象
#这是一种数据流，全体长度是未知的,有可能是一个函数


def b(*args):
	def c():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return c       #返回函数在return时返回自己
f=b(1,2,3,4,5)


print (f)          #调用时输入变量，然后用f来输出
print (f())
print (f)

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#纯英文的str可以用ASCII编码为bytes，内容是一样的
#含有中文的str可以用UTF-8编码为bytes
#含有中文的str无法用ASCII编码
#因为中文编码的范围超过了ASCII编码的范围，Python会报错
