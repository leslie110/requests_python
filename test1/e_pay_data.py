# -*- coding:utf-8 -*-
import xlwt
import xlrd
import csv
import pymysql.cursors

#指定打开文件格式
file = xlwt.Workbook(encoding='utf-8')

#打开文件
table = file.add_sheet("e-pay.xlsx")
#创建表头
def firt():
    table.write(0,0,"付款人名称")
    table.write(0,1,"所属门店ID")
    table.write(0,2,"手机号码")
    table.write(0,3,"备注")

#插入数据
def secd(lie,name,shop_id,number):
    table.write(lie, 0,name)
    table.write(lie, 1,shop_id)
    table.write(lie, 2,number)
#定义数据,执行保存数据
def run():
    num = 1
    lie = 1
    shop_id = "20262025"
    number = "15836458954"
    name = "高欢"
    firt()
    while lie < 3001:
        secd(lie,name+repr(num), shop_id, number)
        lie = lie+1
        num = num+1
    file.save('e-pay.xlsx')

#读取数据
def read_e_pay():
    my_file = open(r"e-pay.csv")
    data = csv.reader(my_file)
    r = 0
    for data_line in data:
        r = r+1
        if r == 100:
            print (data_line)
#将数据库数据写入Excel表
def write(table1,cishu,id,name,mer_id,shop_id):
    table1.write(cishu, 0, id)
    table1.write(cishu, 1, name)
    table1.write(cishu, 2, mer_id)
    table1.write(cishu, 3, shop_id)

#数据库读取数据
def mysql_read():
    file = xlwt.Workbook(encoding='utf-8')
    table1 = file.add_sheet('e-pay-list.xlsx')
    table1.write(0, 0, "付款人id")
    table1.write(0, 1, '付款人姓名')
    table1.write(0, 2, '商户id')
    table1.write(0, 3, '门店id')
    #链接数据库
    i = 1
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='61638752115',
        db='news',
        charset='utf8'
    )
    cursor = connect.cursor()
    mysql = '''select company_id,company_name,mer_id,shop_id from e_p_company'''
    cursor.execute(mysql)
    connect.commit()
    results = cursor.fetchall()
    # 遍历结果,写入Excel中
    for row in results:
        id1 = row[0]
        name1 = row[1]
        mer_id1 = row[2]
        shop_id1 = row[3]
        write(table1,i,id1, name1, mer_id1, shop_id1)
        i = i + 1
        print(i-1,id1, name1, mer_id1,shop_id1)
    file.save('e-pay-list.xlsx')


def dingdan_daoru():
    file = xlwt.Workbook(encoding='utf-8')
    table = file.add_sheet("diandan_daoru.xlsx")
    table.write(0,0,'付款人编号')
    table.write(0,1,'收款金额')
    table.write(0,2,'收银员编号')
    connet = pymysql.Connect(
        host='ardy0220.mysql.rds.aliyuncs.com',
        port=3306,
        user= "root",
        passwd= "zhangdi0220DI",
        db= "e_pay_dev",
        charset='utf8'
    )
    mysql1 = '''select company_id from e_p_company'''
    cursor = connet.cursor()
    cursor.execute(mysql1)
    connet.commit()
    results = cursor.fetchall()
    cishu = 1

    for i in results:
        id = i[0]
        if int(id) >= 1000000000000000 and int(id) < 100000000000000000:
            table.write(cishu,0,id)
            table.write(cishu,1,0.01)
            table.write(cishu,2,'212907')
            cishu =cishu+1
            print (cishu-1,id)
    file.save("diandan_daoru.xlsx")


if __name__ == "__main__":
    mysql_read()
