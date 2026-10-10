'''
函数：实现代码复用
1.定义、调用
2.嵌套
3.函数的参数、返回值
4.匿名函数lambda
'''

'''
    函数的定义、调用
'''
def hello():        #函数的定义
    print('hello')
hello()             #函数的调用

def get_v(x,y):     #带参函数定义
    return          #不带表达式的return返回None
print(get_v(3,4))#None

def getCircleArea(r):
    print("圆的面积是：{:>8.2f}".format(3.14*r*r))
    return
getCircleArea(5)
print(getCircleArea)    #函数名也是变量，拥有自己的内存地址
print(type(getCircleArea))
print(getCircleArea(5))     #return无返回值表达式，打印返回None，原理：函数名也是变量

'''
    函数的嵌套 - 模块化程序设计结构
'''
def main():
    print("输入数据")
    userinput()
    print("处理数据")
    userprocessing()
    print("输出数据")
    useroutput()

def userinput():
    pass#占位符：打草稿用

def userprocessing():
    pass

def useroutput():
    pass
'''
    函数的参数
'''
def getVolume(r,h):
    print("圆柱的体积是：{:>8.2f}".format(3.14*r*r*h))
    return
#位置传参
getVolume(3,4)
getVolume(4,3)

#赋值传参
getVolume(h = 3,r = 5)
getVolume(r = 5,h = 3)

"""
    实际参数的类型
"""
#实参为基本数据类型
a = 10
def func(num):
    num += 1
    print("形参的地址 {}".format(id(num)))
    print("形参的值 {}".format(num))
    a = 1   #局部变量
    return
func(a)     #实参、形参两个不同的变量
print(a,id(a))  #实参值传递不发生变化对原变量

#实参为组合数据类型
tup = (1,5,7,8,12,9)
ls = []
print(id(ls))
def getOdd(tup_f,ls_f):
    print(id(ls_f))     #传递地址
    for x in tup_f:
        if x % 2 != 0:
            ls_f.append(x)
    return ls_f
getOdd(tup,ls)  #引用传递改变原变量
print(ls)
'''
    默认参数
'''
def showmessage(name, age = 18):
    print("姓名：{}".format(name))
    print("年龄：{}".format(age))
    return
showmessage(age = 19, name="Curry")     #传入默认参数使用新值
print("-" * 40)
showmessage(name = "kelvin")        #为传入默认参数则用默认值
'''
    可变参数
'''
#若多出的参数没有指定名称，*p_info以元组的形式保存这些剩余的参数
def showmessage_ch(name, *p_info):
    print("姓名：{}".format(name))
    print(type(p_info))     #元组类型
    for e in p_info:
        print(e, end=",")
    return
showmessage_ch('scrutiny')
print('-'*40)
showmessage_ch('repertoire','prestige',18, 'cynicism')
print()
#若多出的参数指定了名称，**scores以字典的形式保存这些剩余的参数
def showmessage_ch2(name, *p_info, **scores):
    print('姓名：{}'.format(name))
    print(type(p_info))
    print(type(scores))        #字典类型
    for e in p_info:
        print(e, end=",")
    for item in scores.items():
        print(item, end=",")
    print()
    return
showmessage_ch2('geometry','geography', 99, 'crucialism')
print('-'*40)
showmessage_ch2('not','at','all',math = 96, chemistry = 99, age = 18)
"""
    函数的返回值
"""
#比大小
def compare_s(arg1, arg2):
    result = arg1 > arg2
    return result
test = compare_s('a','z')   #返回值赋值
print(test)
#查找参数中含有字符e的单词
def findword_e(sentence):
    result = []
    words = sentence.split()#字符串分隔，默认空格分
    print(words)
    for word in words:
        if word.find('e') != -1:#查找字符串的子串，未找到输出-1
            result.append(word)
    return result
ss = "The people are the Country, put the people First"
print(findword_e(ss))

"""
    lambda匿名函数
"""
import math
area = lambda r: math.pi * r * r
volume = lambda r,h: math.pi * r * r * h
print("圆的面积为：{:6.2f}".format(area(2)))
print("圆柱体体积为：{:6.2f}".format(volume(2,4)))
#按照绝对值大小升序
lst1 = [6,-1,9,-2,-4,10]
lst2 = sorted(lst1, key= lambda x: abs(x))      #key参数为排序规则函数
print(type(lst2))
print(lst2)
