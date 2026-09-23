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

