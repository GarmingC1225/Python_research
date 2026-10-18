'''
文件操作：
1.打开/关闭
2.读操作
3.写操作
4.文件的定位读写
5.读写二进制文件
6.读写Python对象
'''
#open()
mf = open('D:\\test.txt','r',encoding='utf-8')
print(mf,type(mf))
'''读操作'''
#read()
s1 = mf.read(8)
print(s1,type(s1))
#文件的指针随文件的读取变化
s2 = mf.read()  #读取当前指针开始的全部内容
print(s2)
print('-'*40)

#readlines()---> list(mf)
flist = mf.readlines()      #将全部内容读取至列表中 换行会带有\n符号
print(flist)
print('-'*40)
for line in flist:      #按行遍历内容
    print(line,end='')

#readline()逐行
s3 = mf.readline()
while s3 != '':
    print(s3,end='')
    s3 = mf.readline()  #文件指针逐行后移

#直接遍历文件
for line in mf:
    print(line,end='')
print('-'*40)

#close()
mf.close()

'''写操作'''
#write()写入字符串
fname = input("路径文件名:")
f1 = open(fname,"w+",encoding='utf-8')  #w+模式 以读/写模式打开文件 文件存在时清空内容重新创建
f1.write("向文件中写入字符串\n")
f1.write("继续写入")
f1.write("改变open()函数中的编码后再写入一次")
f1.close()

#writelines()写入序列都可
f2 = open("D:\\test.txt","a",encoding='utf-8')
lst = ['stumble','trivial','jockey']
tup1 = ('hockey','diet','assistance')
m1 = {'renovation':'翻新','innovation':'创新','extend':'扩大'}
f2.writelines('\n')
f2.writelines(lst)  #写入序列时不会给每个元素增加换行符
f2.writelines('\n')
f2.writelines(tup1)
f2.writelines('\n')
f2.writelines(m1)#只写入了键
f2.close()

#推导式遍历序列写入
f2_f  = open('D:\\test3.txt','w+',encoding='utf-8')
f2_f.writelines(s + '\n' for s in lst)
f2_f.writelines(t + '\n' for t in tup1)
f2_f.writelines(k + ':' + v + '\n' for k,v in m1.items())
f2_f.close()

'''
    文件的定位读写
'''
#tell()获取文件的当前读写位置
f3 = open('D:\\test3.txt','r+',encoding='utf-8')
str1 = f3.read(10)
print(str1)
print(f3.tell())    #定位至当前文件内容指针
print(f3.readline())    #打印当前文件指针位置的内容
print(f3.tell())
print(f3.readlines())
print(f3.tell())    #当文件指针至文件内容最后时，tell()可看文件长度大小
f3.close()

#seek()移动文件的当前位置-文件指针
f4 = open('D:\\test2.txt','r+',encoding='GBK')
print(f4.tell())
print(f4.seek(6))   #偏移量为6,指定位置默认为0即起始位置
print(f4.tell())
str2 = f4.read(5)
print(str2)
print(f4.tell())

'''
    读写二进制文件
'''
#读写字节字符串
file_b = open(r"D:\mydata.dat","wb")
print(file_b.write(b"Hello python"))    
n = 134
print(file_b.write(bytes(str(n),encoding = 'utf-8')))   #整数转化为字节字符串
print(file_b.write(b"\n3000"))
file_b.close()
file_b2 = open(r"D:\mydata.dat","rb")   #rb模式打开二进制文件
print(file_b2.read())   #返回字节字符串的内容
file_b2.close()
file_b3 = open(r"D:\mydata.dat","r")    #r模式打开二进制文件
print(file_b3.read())   #正常字符串内容
file_b3.close()
'''
    读写python对象
'''
#pickle()标准模块
l1 = ['intervention','temporary','cosmopolitan','fabulous']
d1 = {"word1":'annual','word2':'summit',"word3":'bridge'}
file_b4 = open(r"D:\data_pyobj.dat","wb")
import pickle
#写入python对象数据
pickle.dump(l1,file_b4)
pickle.dump(d1,file_b4)
file_b4.close()
#读取数据
file_b5 = open(r"D:\data_pyobj.dat","rb")
print(file_b5.read())   #输出由pickle序列化后的二进制字节流
file_b5.seek(0) #文件指针移动至起始位置
x = pickle.load(file_b5)
y = pickle.load(file_b5)
print(x,y)
file_b5.close()