"""
类实现抽象和封装：
    类的创建
    对象的创建
    构造方法
    析构方法
    self参数
    类中的变量：成员变量，类变量
    类中的方法：成员方法、类方法、静态方法
"""
from pydantic import color


#创建类
class Dog:  #类的名称 一般首字母大写
    num = 0
    def __init__(self, name, age):  #构造函数   self表对象本身
        self.name = name    #成员变量
        self.age = age
    def enjoy(self):    #成员方法
        print("旺旺旺")
    def show(self,mass):
        print("体重为{}".format(mass))
# 创建类Dog的对象dog
dog = Dog("tadi",3)
print("我的狗狗叫{}，今年{}岁".format(dog.name,dog.age))
dog.enjoy()
dog.weight = 50 #为对象dog添加属性
dog.show(dog.weight)

#用无参数的构造方法构造对象
class Cat:
    def __init__(self):     #构造方法
        self.color = "white"    #初始化属性值
    def show(self):
        print("颜色是{}".format(self.color))
cat = Cat() #构造对象
cat.show()

#带参数的构造方法构造对象
class Human:
    def __init__(self, sex = "",name = "",age = 0): #设置了默认参数
        self.sex = sex
        self.name = name
        self.age = age
    def show(self):
        print("性别：{} 姓名：{} 年龄：{}".format(self.sex, self.name, self.age))
person1 = Human(sex = "man",name="curry",age = 20)
person1.show()
person2 = Human(sex="woman",name="lala",age = 10)
person2.show()

#析构方法：删除对象
class Fish:
    def __init__(self, size = '',weight = 0):
        self.size = size
        self.weight = weight
    def show(self):
        print("这鱼的看起来是{}鱼，重量有{}".format(self.size,self.weight))
    def __del__(self):#析构方法
        print("对象被清除")
fish = Fish(size = "small",weight = 10)
fish.show()
print(id(fish))
del fish #释放对象fish
print(id(fish))

#self参数
class Animal:
    def __init__(self):
        self.color = ''#成员变量
        num = 0 #类属性
    def enjoy(self):
        print("jiongjiongjiong")
    def show(self):
        print("重量{}千克".format(self.weight))
ani = Animal()
ani.weight = 52
ani.enjoy()
ani.show()

'''
成员变量与类变量两点区别：
1.定义
  成员变量于构造方法__init__中定义，通过self参数引用
  类变量于类中方法之外定义的变量，如类Animal中的变量num
2.类外部如何访问
  成员变量属于对象，只能通过对象名访问
  类变量属于类，对象名、类名都可以
'''
class Plant:
    def __init__(self,color = ''):
        self.color = color#成员属性
    variety = 5#类属性
    def show(self):
        print("颜色是{}".format(self.color))
        print("目前植物种类有{}".format(self.variety))
flower1 = Plant() #创建对象即实例
flower1.color = 'blue'
flower1.show()
# Plant.color = 'red'#不成立
# Plant.show()
# flower1.variety = 1 #成立
# flower1.show()
Plant.variety = 2 #成立
Plant.show(flower1) #show()方法属于成员方法，类名不能直接调用
'''
类的方法：
成员方法由对象调用，构造方法、析构方法属于成员方法
类方法、静态方法可以由类名调用，也可以对象调用
'''
class DemoClass1:
    def instanceMethod(self):
        print("属于成员方法")
    @classmethod
    def classMethod(cls):
        print("属于类方法")
obj = DemoClass1()
obj.instanceMethod()#对象调用成员方法
obj.classMethod()#对象调用类方法
DemoClass1.classMethod()#类名调用类方法
#类方法
class DemoClass2:
    def __init__(self,year = 0,month = 0,day = 0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def get_date(cls,string_date):#首参数cls表调用当前的类名
        year,month,day = map(int,string_date.split("-"))#此处为属于get_date()内部的局部变量
        date1 = cls(year,month,day)#date1 = DemoClass2(year,month,day)创建对象date1
        return date1

    def output_date(self):
        print("{}年{}月{}日".format(self.year,self.month,self.day))
rq1 = DemoClass2(2004,9,10)
rq1.output_date()
rq2 = DemoClass2.get_date("2026-10-30")
rq2.output_date()
#静态方法
class DemoClass3:
    def instanceMethod2(self):#成员方法
        print("成员方法")
    @staticmethod
    def staticMethod():
        print("静态方法")
obj = DemoClass3()  #创建对象
obj.instanceMethod2()   #对象调用成员方法
obj.staticMethod()  #对象调用静态方法
DemoClass3.staticMethod()   #类调用静态方法
