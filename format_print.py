print("{:0>10.3f}".format(3.14))    #填充符号 + 对齐方式 + 总宽度 + 精度 + 格式化类型

#%
print("%d"%100)
print("%10s" % "welcome")
n = 'crucial'
a = 200
print("姓名：%s,年龄：%d" % (n, a))

'''
    format()
'''
#位置参数
print("{}{}{}".format('I',"wish",'you'))
print("{1}{0}{2}".format('I',"wish",'you'))
#关键字参数
print("姓名:{name},年龄:{age}".format(name = "james",age = 40))
#格式说明符
# 基本格式：{:[填充][对齐][宽度][.精度][类型]}
# 对齐方式
print("{:<10}".format("left"))    # left      （左对齐）
print("{:>10}".format("right"))   #      right（右对齐）
print("{:^10}".format("center"))  #   center  （居中对齐）
# 填充字符
print("{:*<10}".format("left"))   # left******
print("{:0>10}".format(42))       # 0000000042
# 数字格式化
print("{:.2f}".format(3.14159))   # 3.14
print("{:,.2f}".format(1234567))  # 1,234,567.00
print("{:+.2f}".format(3.14))     # +3.14
print("{:.2%}".format(0.756))     # 75.60%（百分比）
# 进制转换
print("{:b}".format(10))   # 1010（二进制）
print("{:o}".format(10))   # 12（八进制）
print("{:x}".format(10))   # a（十六进制）

"""
    f-string
"""
#直接嵌入变量
n2 = 'entrust'
a2 = 99
print(f"姓名：{n2}, 年龄：{a2}")
print(f"name:{'Bob'}, age:{48}")
#嵌入表达式
a, b = 10, 20
print(f"{a} * {b} = {a * b}")
#格式说明符
# 和 format() 一样的格式说明符
num = 3.14159
print(f"{num:.2f}")        # 3.14
print(f"{num:0>10.3f}")    # 000003.142
print(f"{num:,.2f}")       # 3.14（无千分位，因为不够大）
# 对齐
name = "Python"
print(f"{name:*<10}")      # Python****
print(f"{name:*>10}")      # ****Python
print(f"{name:*^10}")      # **Python**
# 数字格式化
big_num = 1234567
print(f"{big_num:,}")      # 1,234,567
print(f"{big_num:,.2f}")   # 1,234,567.00
print(f"{big_num:.2e}")    # 1.23e+06
# 百分比
rate = 0.856
print(f"{rate:.1%}")       # 85.6%