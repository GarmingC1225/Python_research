'''
运算符
input()
print()
分支语句
元组
'''
num1 = 0
s1 = ''
num2 = 0
result = 0.0

num1 = float(input("数字1:\n")) #输入 input()返回字符串类型
s1 = input("运算符:\n")
num2 = float(input("数字2:\n"))
tu1 = (num1,s1,num2) #元组
tu2 = (55,"+",66)

print("数字1：{}\n符号：{}\n数字2：{}".format(num1,s1,num2)) #print格式化输出1
print("{0}{1}{2}".format(num1,s1,num2)) #print格式化输出2
print("{s1}{num1}{num2}".format(num1 = num1,s1 = s1,num2 = num2)) #print格式化输出3
print("{1[0]}{0[1]}{1[1]}".format(tu1,tu2)) #print格式化输出4


if s1 == '+':
    result = num1 + num2
    print("计算结果为：{:.2f}".format(result))
elif s1 == '-':
    result = num1 - num2
    print("计算结果为：{:.2f}".format(result))
elif s1 == '*':
    result = num1 * num2
    print("计算结果为：{:.2f}".format(result))
elif s1 == '/':
    if num2 != 0:
        result = num1 / num2
        print("计算结果为：{:.2f}".format(result))
    else:
        print("分母不能为零")
elif s1 == '%':
    if num2 != 0:
        result = num1 % num2
        print("计算结果为：{:.2f}".format(result))
    else:
        print("分母不能为零")
elif s1 == '^':
    result = num1 ** num2
    print("计算结果为：{:.2f}".format(result))
elif s1 == '//':
    if num2 != 0:
        result = num1 // num2
        print("计算结果为：{:.2f}".format(result))
    else:
        print("分母不能为零")
else:
    print("error!")

