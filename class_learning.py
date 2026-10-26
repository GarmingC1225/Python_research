"""
类实现抽象和封装：
    类的创建
    对象的创建
    构造方法
    析构方法
"""
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
        print("性别：{} 姓名：{} 年龄：{}".format(self.sex,self.name,self.age))
person1 = Human(sex = "man",name="curry",age = 20)
person1.show()
person2 = Human(sex="woman",name="lala",age = 10)
person2.show()