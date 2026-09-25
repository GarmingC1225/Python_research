'''
容器
1.操作符：切片、字符串链接
2.操作方法：取长、取最大小、index()、count()
'''
str = 'asdfghjkl'
#切片
print(str[4])   #g
print(str[:4]) #asdf
print(str[-4])  #h
print(str[-4:-2])   #hj
print(str[:9])  #0-8 默认步长为1
print(str[::3]) #afj
#字符串链接
print(str*2)    #asdfghjklasdfghjkl
print(str+' 33')    #asdfghjkl 33

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
