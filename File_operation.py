'''
文件操作：
1.打开/关闭
2.读操作
3.写操作
'''
#open()
mf = open('D:\\test.txt','r',encoding='utf-8')
print(mf,type(mf))
'''读操作'''
#read()
# s1 = mf.read(8)
# print(s1,type(s1))
#文件的指针随文件的读取变化
# s2 = mf.read()  #读取当前指针开始的全部内容
# print(s2)
print('-'*40)

#readlines()---> list(mf)
# flist = mf.readlines()      #将全部内容读取至列表中 换行会带有\n符号
# print(flist)
# print('-'*40)
# for line in flist:      #按行遍历内容
#     print(line,end='')

#readline()逐行
# s3 = mf.readline()
# while s3 != '':
#     print(s3,end='')
#     s3 = mf.readline()  #文件指针逐行后移

#直接遍历文件
for line in mf:
    print(line,end='')
print('-'*40)

#close()
mf.close()

'''写操作'''
