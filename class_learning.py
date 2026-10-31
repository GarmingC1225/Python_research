"""
类实现抽象和封装：
    类的创建
    对象的创建
    构造方法
    析构方法
    self参数
    类中的变量：成员变量，类变量
    类中的方法：成员方法、类方法、静态方法
    类的继承：继承实现、方法重写、super()方法、python的多继承
    类的多态
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

"""实现继承"""
#子类继承父类
class Animal:#父类
    num = 0 #类变量
    def __init__(self):#成员方法：构造方法
        print("父类Animal")
    def show(self):#成员方法方法
        print("父类Animal成员方法")
class Cat(Animal):#子类继承Animal父类
    def __init__(self):
        print("构建子类Cat")
    def run(self):
        print("子类Cat成员方法")
cat = Cat()#创建对象cat并自动调用构造函数初始化
cat.run()#子类自己的方法
cat.show()#调用父类的方法show()
print(cat.num)#调用父类的类变量
"""方法重写：子类重写的方法需和父类被重写的方法具有相同的方法名和参数列表"""
class Animal:
    def __init__(self,isAnimal):
        self.isAnimal = isAnimal
    def run(self):
        print("父类Animal通用的run()方法")
    def show(self):
        print("父类Animal的show()方法")
class Cat(Animal):
    def __init__(self):
        print("子类的构造方法")
    def run(self):  #方法重写
        super().run()#super()--->父类Animal 实现拓展而非替代
        print("子类cat重写的run()方法")
ani = Animal(False)
ani.show()
cat = Cat()
cat.run()
cat.show()#调用父类方法
"""多继承"""
class Phone:
    def receive(self):#成员变量
        print("接电话")
    def send(self):
        print("打电话")
class Message:
    def receiveMsg(self):
        print("接收短信")
    def sendMsg(self):
        print("发送短信")
class Mobile(Phone,Message):#同时继承Phone和Message
    pass
mobile = Mobile()#创建对象mobile
mobile.receive()
mobile.send()
mobile.receiveMsg()
mobile.sendMsg()
"""
类的多态：狗、猫都继承了动物这个类，类中有个叫喊的方法
由于对象不同（狗、猫），则同一个方法的执行效果不同
实现组成：继承、重写、同一接口（包含重写方法）
"""
class Animal:
    def __init__(self,name):
        self.name = name
    def enjoy(self):
        print("jiongjiongjiong")

class Cat(Animal): #继承Animal
    def enjoy(self):#成员方法
        print(self.name,"miaomiaomiao")

class Dog(Animal):
    def enjoy(self):#成员方法
        print(self.name,"wangwangwang")

class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def drive(self,ani):
        ani.enjoy()#包含enjoy()方法，同一接口不同对象实现多态
cat = Cat("Mikey")#创建对象cat
dog = Dog("Dahuang")#创建对象dog
person = Person(99,"curry")
#多态效果
person.drive(cat)
person.drive(dog)
#父类实例实现多态
obj_Animal = Animal("dengdeng") #创建父类的实例对象
person.drive(obj_Animal)

