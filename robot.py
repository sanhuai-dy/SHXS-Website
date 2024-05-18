from flask import Flask, request
import requests,time,datetime
import BS1
import random
import codecs
import os
import sys
app = Flask(__name__)
Yesword=['yes','没错','嗯','好','YES','Yes','玩','开始','要']
right,l=0,0
Noword=['no','NO','No','不']
lasttext=''
shop=['qq人','qq王']
shopyuan=[100,500]
poke_start=0
poke_wait=0
poke_now=[str(datetime.datetime.now().minute),str(datetime.datetime.now().hour)]
buy=0
pet_name=0
k=0
init=1
enemy_choose=[]
poke=0
pet_name_choose=0
pet_pvp_ready=0
oplist=[3069842996]
enemy_list=[]
player_stop=0
play_game=0
usearea=['商城','签到','休闲小游戏','宠物系统','其他']
pet_game_turn=0
usecommand=[{'商城指令':['"/商城"或"/store"']},{'签到指令':['/签到']},{'休闲小游戏指令':['/play或/game或/玩游戏']},{'宠物系统指令':['购买宠物:"/buy"或"我要买"','命名宠物:"/命名 [第几个宠物] [名字]"']},{'其他指令':['查看自身面板:"/查看"','抽奖指令:"/抽奖"','计算指令:"/print 式子"或"/式子"','查询词语(或字)指令:"/搜字词 [词语(或字)]"']}]
answer="看不懂"

def post_data(contect_text):
    global right,l,lasttext,answer,play_game


    # if init:
    #     answer=((,'程序已启动') )
    #     init=0

    if contect_text[:4]=='echo':
        answer=((contect_text[5:]) )

    elif contect_text=='#?' or contect_text=='#帮助' or contect_text=='/帮助' or contect_text=='help' or contect_text=='#help' or contect_text=='#？' or contect_text=='/？' or contect_text=='/help' or contect_text=='/?' or contect_text=='帮助':
        answer=(('其……其实我啥都不会 只会算数和成语接龙……\n输入数学算式如“1+1”以算数\n输入“成语接龙”以接龙\n输入“天气预报 [城市]”以获取天气'))
    
    elif contect_text=='114514':
        answer=("输入“早”or“晚”和我打招呼~\n输入“抽奖”来抽积分（虽然无用")

    elif contect_text=='成语接龙':
        answer=(('你确定要玩“成语接龙”吗') )
        right=1
    elif contect_text and right==1 and l==0:
        for i in Yesword:
            if l:
                break
            for j in Noword:
                if i in contect_text and not j in contect_text:
                    lasttext=BS1.randomword()
                    answer=(('那开始了！') )
                    time.sleep(0.1)
                    answer=((lasttext) )
                    l=1
                    break
                    
                elif j in contect_text:
                    l=2
                    answer=(('那别玩了') )
                    break
        if not l:
            answer=(('没听懂呢') )
        if l==2:
            l=0

    elif l==1:
        if BS1.checkCY(contect_text) and contect_text[0]==lasttext[3]:
            lasttext=BS1.chengyu(contect_text[-1])
            answer=((lasttext) )
            if '我输了' in lasttext:
                l=0
                right=0
        elif '结束' in contect_text or '停' in contect_text:
            l=0
            right=0
            play_game=0
            answer=(('游戏结束！') )
        elif '重来' in contect_text:
            lasttext=BS1.randomword()
            answer=('那开始了！') 
            time.sleep(0.1)
            answer=((lasttext) )
        else:
            answer=(('无法识别该成语！') )
    elif 'print' in contect_text and len(contect_text)<50:
        contect_text=contect_text[6:]
        try:
            if eval(contect_text)==0 or eval(contect_text) and len(contect_text)<30:
                if len(str(eval(contect_text)))>40 or ('**' in contect_text and len(str(contect_text))>15) or str(contect_text).count('**')>=2:
                    answer=((f'不做执行') )
                else:
                    answer=((f'{contect_text} 的值是 {eval(contect_text)}') )
            
        except:
            try:
                
                answer=((f'{contect_text} 的值是 {eval(contect_text)}') )
            except:
                answer=((f'未知变量{contect_text}') )


    
    elif '抽奖' == contect_text:
        kw=random.randint(1,40)
        answer=(((f'你抽中了{kw}分')) )
        
        
    
            
    elif '晚' in contect_text:
        a=requests.get("https://apis.tianapi.com/wanan/index?key=4ef31eb133216cf8c4a04067ed9df8e8").json()['result']['content']
        answer=((f'{a}') )
    elif '早' in contect_text:
        a=requests.get("https://apis.tianapi.com/zaoan/index?key=4ef31eb133216cf8c4a04067ed9df8e8").json()['result']['content']
        answer=((f'{a}') )
    elif contect_text[:4]=='天气预报':
        contect_text=contect_text[5:]
        f=open('adcode.txt','r',encoding='utf-8')
        read=eval(f.read())
        for i in read[0]:
            if contect_text in i:
                contect_text=read[1][read[0].index(i)]
                break
        t=''
        count=0
        for i,j in BS1.tianqi(contect_text).items():
            count+=1
            if count==3:
                continue
            if count==5:
                j=f'温度{j}°'
            if count==6:
                j=f'{j}风'
            if count==7:
                j=f'风级{j}'
            if count==8:
                j=f'空气湿度{j}'
            t+=j+' '
        answer=((f'{t}') )
    elif '办' in contect_text:
        strf='首先'+'不要'*random.randint(1,10)+'慌张'
        answer=(((strf)) )

    elif '色' in contect_text:
        strf='达咩色色'
        answer=(((strf)) )

    elif '靠' in contect_text:
        answer=((('不能说脏话！')) )
    
        
    elif '骂' in contect_text[:2]:
        QQ_namer=contect_text[1:]
        level='min'
        if '大骂' in contect_text:
            QQ_namer=contect_text[2:]
            level='max'
        msg=BS1.fukp(level)
        answer=(((f'{QQ_namer}{msg}')) )
        print(msg)
    else:
        try:
            if eval(contect_text)==0 or eval(contect_text) and len(contect_text)<30:
                if len(str(eval(contect_text)))>40 or ('**' in contect_text and len(str(contect_text))>10) or str(contect_text).count('**')>=2:
                    answer=((f'不做执行') )
                else:
                    answer=((f'{contect_text} 的值是 {eval(contect_text)}') )
            else:
                answer=((f'不知道你在说什么哦 我还在学习呢\n输入114514发现我的隐藏指令！') )
        except:
            answer=((f'我在学习啦 不要给我出这么难的汉语题\n输入/?解锁我的脑袋！'+'\n输入114514发现我的隐藏指令！'*random.randint(0,1)) )
    return answer

        