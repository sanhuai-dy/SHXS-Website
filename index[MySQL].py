from flask import Flask, render_template,request,redirect,jsonify
import flask
import requests
import datetime as dt
import robot
import time
import json
import random
import pymysql
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__, template_folder = './templates/',static_folder='',static_url_path='')
db  = pymysql.connect(host="localhost", port=3306, user='root', passwd='-SpituG(Q2-4HX/L-', db='user', charset='utf8')
cursor = db.cursor(pymysql.cursors.DictCursor)# 创建游标(查询数据返回为字典格式)

def reconnect(web):
    try:
        web.close()
    except:
        pass
    global db,cursor
    db = pymysql.connect(host="localhost", port=3306, user='root', passwd='-SpituG(Q2-4HX/L-', db='user', charset='utf8')
    cursor = db.cursor(pymysql.cursors.DictCursor)# 创建游标(查询数据返回为字典格式)
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    reconnect,
    args=[db],
    trigger='interval',
    hours=1
)
'''
sql ='select * from users'#格式："select * from [数据库]"
cursor.execute(sql)#查询数据库单条数据
result = cursor.fetchall()
print(result)

sql ='insert into users values(%s,%s,%s,%s,%s)'#格式："insert into [数据库] values(插入值1,插入值2,插入值3...)"
username=input()
insertthing=(username,123,'0',1,0)
cursor.execute(sql,insertthing)#查询数据库单条数据
db.commit()

sql =f'select * from users where username={username}'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
cursor.execute(sql)
result = cursor.fetchall()
print(result)

db.close()
'''
jg={}
@app.route('/zc', methods=['GET','POST'])
def zc():
    if  request.method=='GET':
        return render_template('zc.html')
    elif request.method=='POST':
        thatname=''
        username=request.form.get('username')
        password=request.form.get('password')
        sql =f'select * from users where username="{username}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if result:
            print(1112)
            thatname=username
        else:
            user_ip=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            if user_ip in jg:
                if time.time()-jg[user_ip]<60:
                    print(333)
                    return render_template('zc.html',time=f"注册过快，请等待{time.time()-jg[user_ip]}秒后再注册")
            sql ='insert into users values(%s,%s,%s,%s,%s)'#格式："insert into [数据库] values(插入值1,插入值2,插入值3...)"
            insertthing=(username,password,user_ip,1,0)
            cursor.execute(sql,insertthing)#插入数据
            db.commit()
            print(111)
            jg[user_ip]=time.time()
        return thatname
    else:
        print(222)
        return render_template('zc.html')

@app.route('/act')
def act():
    return render_template('act.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        dict_login=0
        sql =f'select * from users where username="{username}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            dict_login=1
            if result[0]['password']==password:
                user_ip=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
                sql = f'UPDATE users SET userip = "{user_ip}" where username = "{username}"'
                cursor.execute(sql)
                db.commit()#提交修改 --- 重！！！
                dict_login=2
        return str(dict_login)
    return render_template('login.html')

@app.route('/black')
def black():
    return render_template('black.html')            

@app.route('/',methods=['GET','POST'])
def index():
    user_ip=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    sql =f'select * from users where userip="{user_ip}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        return render_template('index.html',saidapi=requests.get("https://v1.hitokoto.cn/?c=f&encode=text").text)
    if len(result)>=2:
        return render_template('index.html',saidapi=requests.get("https://v1.hitokoto.cn/?c=f&encode=text").text,username=result[0]['username'],tip='同ip下您的账号过多，如需切换账号，请前往用户中心。')
    return render_template('index.html',saidapi=requests.get("https://v1.hitokoto.cn/?c=f&encode=text").text,username=result[0]['username'])

@app.route('/blog')
def blog():

    user_ip=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    sql =f'select * from users where userip="{user_ip}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    m = cursor.fetchall()
    if not m:
        return render_template('blog.html',href='/login',msg='暂未登录，请先登录以发博客')
    return render_template('blog.html',href='/blog/send',msg="发博客",username=m[0]['username'],level=m[0]['level'],ex=f"{m[0]['ex']}/{m[0]['level']**2+m[0]['level']*2+20}")
        

@app.route('/blog/<int:blogid>')
def seeblog(blogid):
    sql =f'select * from blog where blogname={blogid}'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    result = cursor.fetchone()
    return render_template('seeblog.html',title=result["title"],content=result["text"],username=result["username"],time=f'{result["time"]}',blogid=blogid)

@app.route('/blog/del',methods=['POST'])
def delblog():
    blogid=request.form.get('blogid')
    user_ip=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    sql =f'select * from users where userip="{user_ip}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    m1 = cursor.fetchone()
    sql =f'select * from blog where blogname="{blogid}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    m2 = cursor.fetchone()
    
    if not(m1 and m2):
        return '1'
    if m1['username']==m2['username']:
        sql='delete from blog where blogname = %s'
        cursor.execute(sql,blogid)
        db.commit()
        return '0'
    else:
        return '1'
    
    

@app.route('/getblog',methods=['POST'])
def getblog():
    sql =f'select * from blog ORDER BY time DESC'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    result = cursor.fetchall()
    return jsonify({'0':result})

@app.route('/blog/send')
def send():
    return render_template('send.html')

@app.route('/getsend',methods=['POST'])
def getsend():
    title=request.form.get("title")
    text=request.form.get("text")
    user_ip=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    sql =f'select * from users where userip="{user_ip}"'#格式："select * from {数据库} [where {条件}]"('[]'为选填，'{}'为必填)
    cursor.execute(sql)
    m = cursor.fetchone()
    if not m:
        return '0'
    username=m['username']
    sql ="insert into blog values(%s,%s,%s,%s,%s)"
    blogname=str(str(dt.datetime.now().year)+str(dt.datetime.now().month)+str(dt.datetime.now().day)+str(dt.datetime.now().hour)+str(dt.datetime.now().minute)+str(dt.datetime.now().second)+str(random.randint(1000,9999)))
    insertthing=(blogname,str(title),str(text),username,dt.datetime.now())
    cursor.execute(sql,insertthing)#查询数据库单条数据
    db.commit()
    return '1'

@app.route('/api/robot')
def api():
    say=request.args.get("say")
    return robot.post_data(say)

@app.route('/api/say')
def say():
    bsay=requests.get("https://v1.hitokoto.cn/?c=f&encode=text").text
    return bsay


# 设置500错误处理器
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')


# 设置404错误处理器
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



app.run(host='0.0.0.0',port='80',debug=True)



