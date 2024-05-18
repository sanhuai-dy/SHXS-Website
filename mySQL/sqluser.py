#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2018/5/13
import pymysql
# 创建连接
import datetime as dt
import random
db  = pymysql.connect(host="localhost", port=3306, user="root", passwd="-SpituG(Q2-4HX/L-", db="user", charset="utf8")
# 创建游标(查询数据返回为元组格式)
# cursor = conn.cursor()
# 创建游标(查询数据返回为字典格式)
cursor = db.cursor(pymysql.cursors.DictCursor)# 执行数据查询
sql ="insert into users values(%s,%s,%s,%s,%s)"#格式："insert into [数据库] values(插入值1,插入值2,插入值3...)"
#insertthing=(str(str(dt.datetime.now().year)+str(dt.datetime.now().month)+str(dt.datetime.now().day)+str(dt.datetime.now().hour)+str(dt.datetime.now().minute)+str(dt.datetime.now().second)+str(random.randint(1000,9999))),input(),input(),input(),dt.datetime.now())
m={'123123': {'username': '123123', 'password': '123123', 'user_ip': '113.109.43.132'}, 'shxs666': {'username': 'shxs666', 'password': 'Liang20100120', 'user_ip': '27.46.234.139'}, 'LLLL': {'username': 'LLLL', 'password': '123123'}, 'lo111': {'username': 'lo111', 'password': '111111'}, 'xxxxx': {'username': 'xxxxx', 'password': '123456'}, '12312333': {'username': '12312333', 'password': '123123'}, '123123123': {'username': '123123123', 'password': '123123'}, '123123123123': {'username': '123123123123', 'password': '123123123'}, 'A一只一只白熊A': {'username': 'A一只一只白熊A', 'password': 'Lifh090910'}, '阿瓦达肯大褂': {'username': '阿瓦达肯大褂', 'password': '123456', 'user_ip': '0'}, '1233': {'username': '1233', 'password': '112344'}, '22222': {'username': '22222', 'password': '22222222'}, '114514': {'username': '114514', 'password': '1919810'}, 'sblbmshxs': {'username': 'sblbmshxs', 'password': 'sblbmshxs'}, '2345647yu5iu6yutrhegdf': {'username': '2345647yu5iu6yutrhegdf', 'password': 'fdgsfdhgfjythrgef'}, 'helloword': {'username': 'helloword', 'password': '123456'}, 'fuckusb': {'username': 'fuckusb', 'password': '666666', 'user_ip': '0'}, '1231231': {'username': '1231231', 'password': '123123'}, '12312312': {'username': '12312312', 'password': '123123'}, '1231231234': {'username': '1231231234', 'password': '123123'}, '12312312345': {'username': '12312312345', 'password': '123123'}, '123123123456': {'username': '123123123456', 'password': '123123'}, 'ffffffffff': {'username': 'ffffffffff', 'password': '111111111'}, '5555555': {'username': '5555555', 'password': '5555555'}, '1234567890876543': {'username': '1234567890876543', 'password': '123456789'}, '刘衍恒是人': {'username': '刘衍恒是人', 'password': '100520'}, 'hello world': {'username': 'hello world', 'password': '123123'}, 'stu20': {'username': 'stu20', 'password': '123345'}, 'white_bear_114514': {'username': 'white_bear_114514', 'password': '123456', 'user_ip': '117.136.32.215'}, 'stu223': {'username': 'stu223', 'password': '123456'}}
for i,j in m.items():
    insertthing=(str(i),str(m[i]['password']),'0',1,0)
    cursor.execute(sql,insertthing)#查询数据库单条数据
db.commit()
sql ="select * from users"#格式："select * from [数据库]"

#cursor.execute(sql)#查询数据库单条数据
#result = cursor.fetchall()
#print(result)
username=input()
# sql ="insert into users values(%s,%s,%s,%s,%s)"#格式："insert into [数据库] values(插入值1,插入值2,插入值3...)"
# 
# insertthing=(username,123,"0",1,0)
# cursor.execute(sql,insertthing)#查询数据库单条数据
# db.commit()
# sql =f'select * from users where username="{username}"'#格式："select * from {数据库} [where {条件}]"("[]"为选填，"{}"为必填) 查询
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)
# password=input()
# sql = f'UPDATE users SET password = "{password}" where username = "{username}"'
# a=cursor.execute(sql)
# db.commit()#提交修改 --- 重！！！
# print(a)
db.close()