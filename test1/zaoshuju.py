# -*- coding:utf-8 -*-
#需要xlwt库的支持
from xlwt import *

#指定file以utf-8的格式打开
file = Workbook(encoding = 'ascii')
#指定打开的文件名
table = file.add_sheet('aaa.xlsx')
i = 1   #定义初始循环次数变量
k = 1   #身份证号码
q = 1000        #家庭编号
a = 1
'''
   创建表头
'''
table.write(0,0,"身份证号码") #在1行1列写入
table.write(0,1,"缴费金额") #在1行2列写入
table.write(0, 2, "家庭编号")#。。。
table.write(0, 3, "姓名")#。。。
table.write(0,4,"性别")#.....
table.write(0,5,"年龄")#....
table.write(0,6,"爱好")#.....
'''
循环为Excel表格写入数据
'''
while i<20:
    table.write(i,0,repr(k)) #在1行1列写入身份证号码，使用repr方法将数据转换成字符串
    table.write(i,1,0.01) #在1行2列写入缴费金额
    table.write(i, 2, repr(q))#在1行3列写入家庭编号，使用repr方法将数据转换成字符串
    table.write(i, 3, "李四" + repr(i))  #在1行4列写入姓名， 使用repr方法将数据转换成字符串
    i = i+1
    k = k+1
    '''
    将q（家庭编号）数据进行五次循环
    '''
    if a % 5 != 0:
        q = q
    else:
        q = q + 1
    a = a+1
    #print (q)
    '''
    循环写入客户性别及年龄
    '''
    if a%3 !=0:
        table.write(i-1, 4, "男")
        table.write(i - 1, 5, "25")
    else:
        table.write(i-1, 4, "女")
        table.write(i - 1, 5, "23")

print (k)



file.save('aaa.xls')

