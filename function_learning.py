'''
函数：实现代码复用
1.定义、调用
2.嵌套
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
