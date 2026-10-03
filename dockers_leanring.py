'''
容器
1.操作符：切片、字符串链接
2.操作方法：取长、取最大小、index()、count()
3.遍历列表、列表推导式创建列表
4.元组的基本操作、与列表的转换
5.生成器
6.字典的基本操作、字典的常用方法
7.集合的基本操作、集合的运算
'''

str1 = 'asdfghjkl'
#切片
print(str1[4])   #g
print(str1[:4]) #asdf
print(str1[-4])  #h
print(str1[-4:-2])   #hj
print(str1[:9])  #0-8 默认步长为1
print(str1[::3]) #afj
#字符串链接
print(str1*2)    #asdfghjklasdfghjkl
print(str1+' 33')    #asdfghjkl 33

str2 = 'the belt and road initative'
print(len(str2))    #取序列长度包括空格
print(ord('v')) #118
print(ord(' ')) #32
print(max(str2))
print(min(str2))
print(str2.count(' '))  #空格在str2中出现的总次数
print(str2.count('d'))  #d在str2中出现的总次数
'''
s.index(x[, i[, j]])
- `x`：要查找的目标元素
- `i`（可选）：查找起始下标，**包含 i**，默认 0
- `j`（可选）：查找终止下标，**不包含 j**，默认序列长度（到末尾）
'''
print(str2.index(' ',6))    #从序列下标6开始往后找第一次出现空格的下标
# print(str2.index(' ',0,3))  #0-3下标内找，是不包括3的
print(str2.index(' ',0,4)) #3
'''
先纠正：**`index()` 本身不会自动倒序查找！**
`index` 永远是**从左向右（正向）**搜索元素，负下标只是用来定位区间，**不会改变查找方向**。
'''
# print(str2.index(' ',-1,-11))

"""
列表
可不同类型
可变数据类型：任意增加/删除
遍历、排序、反转
"""
lst1 = [100, 'LBJ', 5.0+9.0j, [1,'tom']]
print('LBJ' in lst1)
print(lst1[3])
print(lst1.index(5.0+9.0j,1,3))
print(lst1.count('LBJ'))
print(lst1[:: 2])
print(lst1[::-1]) #容器反转
print(lst1[1::2])

lst1[2] = 'james' #替换元素
print(lst1)

ls1 = ['curry',789,20.6,[1,3,2]]
ls2 = [1,2,3,9,5,60]
ls3 = ['bro','sister']
ls1[0:3] = ls2[0:3] #替换ls1列表0-2个元素为ls2 0-2个元素
print(ls1)
print(ls2)
ls2[0:2] = ls3
print(ls2)
ls1[0:4:2] = ls3
print(ls1)
print(ls1[1:4:-1])  #为空[] 因为步长为负数表列表反转来排，则原本下标为1的应为最左边的元素
print(ls1[3:1:-1])
ls1[3:1:-1] = ls3   #倒转后的列表替换元素按照ls3的顺序将指定位置替换
print(ls1)
del ls1[0:1]
print(ls1)
del ls1[::2]
print(ls1)
print(ls2)
ls2.extend(ls1)
print(ls2)

l1 = [74,5,6,78,9]
l1.append(10) #列表最后追加元素
print(l1)
l2 = l1.copy() #复制列表的元素
print(l2)
l2.clear() #删除列表的所有元素
print(l2)
print(l1.pop(0)) #返回列表索引为0的元素并删除它
print(l1)
print(id(l1))   #获取对象的内存地址
print(l1)
l1.reverse()    #翻转列表
print(l1)
l1.sort()   #排序列表 默认升序
print(l1)
l1.sort(reverse=True) #更改为降序
print(l1)

for item in l1:     #遍历列表
    print(item, end='|')
print('\n')

i = 0
for item in range(0,len(l1),2): #用range()遍历来指定列表
    l2.append(l1[item])
print(l2)

l3 = []
while i < len(l2):
    l3.append(l2[i] + l2[i])
    i += 1
print(l3)

'''
    for循环创建简单列表
'''
alist = [x for x in range(11)] #列表推导式
print(alist)
alist2 = []
for x in range(0,11,1):     #range()里面的stop是开区间
    alist2.append(x)
print(alist2)

'''
    for循环中使用if分支创建列表
'''
#创建1-10偶数平方的列表
alist3 = []
for x in range(11):
    if(x % 2 == 0):
        x **= 2
        alist3.append(x)
print(alist3)
#用推导式表示
alist3_t = [x **2 for x in range(11) if x % 2 == 0]
print(alist3_t)

'''
    多重for循环创建列表
'''
alist4 = []
for x in range(3):
    for y in range(3):
        alist4.append((x, y))
print(alist4)
#推导式表示
alist4_t = [(x, y) for x in range(3) for y in range(3)]
print(alist4_t)

'''
    列表推导式使用函数
'''
#将所有字符转换成小写字符
alist5 = ['Constitutional','Adquate','Crystal','Cynicism']
for x in alist5:
    print(x.lower())
#推导式表示
alist5_t = [x.lower() for x in alist5]
print(alist5_t)

#practice
lst_prac = ['456312', 'charter', 'hasten', 'convergence', 'penguin']
lst_prac.insert(2,'valley')
print(lst_prac)
lst_prac[3:5] = "disintegration", 100 #替换原本的元素值
print(lst_prac)
vector1 = [x for x in range(-5,10,2)]
print(vector1)
vector2 = ''.join([chr(ord('a')+x) for x in range(26) ])
print(vector2)

'''
    元组的基本操作
'''
tup1 = ('exceedingly','repertoire','acid',2004,5.2+8.8j)
print(tup1)
tup2 = 'amid','ammunition','artful','tactful',4     #声明元组的圆括号可省略
print(tup2)
tup3 = ('familiarity',)     #元组只有一个元素的时候后面的逗号不可省略
print(tup2 + tup3)      #实现元组的连接
print(tup1[4])  #访问元组元素
print(len(tup1),max(tup3[0]))
print(tup1.index(2004))
print(help(tuple))  #显示元组的属性和方法
tup_lst = (2005,'元组是不可变序列',[5,'comvergency',88.8])
tup_lst[2][0] = 'list_type'     #元组里的列表元素可以改变值
print(tup_lst)
'''
    元组与列表的相互转换
'''
#元组 -> 列表
tup4 = ('division','frequency',2006,999.9)
lst_t4 = list(tup4)   #变成列表后可以进行修改操作
print(lst_t4)
lst_t4[2] = 1996
print(lst_t4)

#列表 -> 元组
tup4_lst = tuple(lst_t4)
print(tup4_lst)

#生成器 生成器对象
gen1 = ((i**2) for i in range(10,20))   #创建生成器对象gen1
print(gen1)     #打印该生成器的对象类型+地址
print(list(gen1))   #list()强制遍历生成器
gen2 = ((i+2) for i in range(10) if (i%2==0))
print(gen2.__next__())  #单步迭代遍历，一次性计算输出
print(gen2.__next__())
print(list(gen2))
gen2 = ((i+2) for i in range(10) if (i%2==0)) #已经单步后，想重新完整计算遍历需要重新定义
for j in gen2:  #for循环遍历生成器对象
    if (j == 10):
        print(j)    #print()函数end参数默认换行
        break
    print(j,end=',')

'''
    序列解包
'''
tuple1 = (False, 3, "complacency")
x,y,z = tuple1  #序列解包
print(x,y,z)
#map()函数
m, n, p = map(str, range(3))    #map()函数将对象映射给str再做解包
print(m, n, p)
#列表解包
lst_x = [1,3,2,4]
a,b,c,d = lst_x #序列解包
print(a,c)
#字典解包
dicts_x = {'a':1,'b':2,'c':3}
v1,v2,v3 = dicts_x  #字典序列解包，默认对键进行操作
print(v1,v2,v3)
x,y,z = dicts_x.items() #字典方法items() 使解包对键值对操作
print(x,y,z)
x2,y2,z2 = dicts_x.values() #字典方法values() 使解包对值进行操作
print(x2,y2,z2)
#内置函数enumerate()的序列解包
lst_e = ['s','t','u','n']
for i,x in enumerate(lst_e):    #i作为索引
    print(i,x)
#'*'星号解包
print([9,8,74,5,6])
print(*[9,8,74,5,6])
print(tuple(range(4)))
print(*range(4))

'''
    字典的基本操作
'''
#创建字典
dict1 = {}
dict2 = {"id": 1, "name": "rose", "address": "cdsklajf", "phone": "+1 234 567", "email": ""}    #经典
dict3 = dict(id=2, name="vibration", address="beijing")     #dict()函数+关键字参数
dict4 = dict([("id",101),("name",'delicious'),("email",'')])       #dict()函数+键值对序列
print(dict2)
print(dict3)
print(dict4)

#检索字典元素
dict5 = {"id": 10, "name":"provocation", "address":"interruption"}
print('id' in dict5)    #in 运算符检索
print('provation' in dict5)
print(dict5['id'])      #关键字检索
tu1 = (dict5['id'], dict5['name'], dict5['address'])
print(tu1,type(tu1))

#添加、修改字典元素
dict6 = {1:'bridegroom',2:'bride',3:'groom'}
print(dict6)
dict6[3] = 'master' #键3存在则修改值
print(dict6)
dict6[4] = 'promoted' #键4不存在则添加值
print(dict6)

'''
    字典的常用方法
'''
#keys()
dicts = {'w1':'hypothetical','w2':'psychiatric','w3':'cynicism'}
key1 = dicts.keys()     #所有键信息
print(type(key1))
print(key1)
for k in key1:
    print(k,end=',')
#values()
values1 = dicts.values()    #所有值信息
print()
for v in values1:
    print(v,end=',')
#items()
items1 = dicts.items()      #所有键值对信息
print()
for items in items1:
    print(items,end='|')
print()
# get()
print(dicts.get('w1'))  #返回键存在的相应值
print(dicts.get('w4'))  #键不存在返回默认值，默认为None
print(dicts.get('w4','202'))    #设置默认值
#pop()
print(dicts.pop('w3'))  #返回键存在相应值并删除此键值对
print(dicts)
print(dicts.pop('w4','查无此词'))   #键不存在返回默认值
#popitem()
print(dicts.popitem())  #删除字典最后的键值对
print(dicts)
print(dicts.popitem())
print(dicts)
#copy()
dicts = dict6.copy()    #复制字典
print(dicts)
print(id(dicts),id(dict6)) #3111703166208 3111703166144
print(dicts is dict6)
dicts[2] = 'homogeneous' #需改副本字典不影响原字典的值
print(dicts)
print(dict6)
#update()
dict_u1 = {1:'fertilizer','w2':'buffalo',3.0:'plaintiff'}
print(dict_u1)
dict_u2 = {'w1':"prompt",'w2':'respond',3:'jeff'}
print(dict_u2)
dict_u1.update(dict_u2)     #更新dict_u1字典
# 原则：保留原本有的而2中没有的；修改与2中键一样的为2中的值；添加只有2中存在的键值对

'''
    集合的基本操作
'''
#创建集合
aset = set('speculation')   #set()函数
bset = set([58,5,4,5,6])
cset = set()
print(aset,bset,cset)

#常用操作
cset = bset.copy()  #copy()
print(aset,bset,cset)

bset.add('y')   #add()添加元素
print(bset)

print(bset.pop())  #pop()随机选择移除
print(bset)

print(bset.isdisjoint(aset))    #isdisjoint()判断集合中是否存在相同元素

print(len(aset))    #计算集合元素个数

cset.clear()    #clear()移除集合所有元素
print(cset)

#集合的遍历
for k in aset:
    print(k,end="-")
print()

"""
    集合的运算
"""
cal_set1 = set([10,20,30])
cal_set2 = set([20,30,40])
set1 = cal_set1 & cal_set2  #交集运算
set2 = cal_set1 | cal_set2  #并集运算
set3 = cal_set1 ^ cal_set2  #补集运算
set4 = cal_set1 - cal_set2  #差集运算 //{10}
print(set1)
print(set2)
print(set3)
print(set4)

print(set1 < cal_set1)  #子集运算 判断set1是否其真子集
print(cal_set1 > set1)  #超集运算 判断cal_set1是否其超真集
print(cal_set1 > set2)  #False





