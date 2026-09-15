'''
数据类型
type()
bool()
'''

num0 = 0
num1 = 0x12
num2 = 0o17 #八进制
print(type(num0),bool(num0))
print(bool(num2))

fnum1 = 1.7e3
print(type(fnum1),bool(fnum1))

cnum1 = -3.4-3.8j #复数型
print(cnum1.real,cnum1.imag) #实部 虚部
print(type(cnum1),bool(cnum1))
cnum2 = 3j
print(cnum2.real,cnum2.imag)

s1 = ''
print(type(s1),bool(s1))

l1 = [] #列表
print(type(l1),bool(l1))

d1 = {} #字典
print(type(d1),bool(d1))

t1 = ("curry",30,99.9,3.0+73j) #元组
print(type(t1),bool(t1))

aset = set("innovation") #集合
bset = set([5,6,7,8])
print(type(aset),bool(aset))
print(type(bset),bool(bset))


