import datetime,requests
import data.time as tim
import os
text=tim.time['text']
def hour(t):
    global text
    with open('./data/time.py','r',encoding='utf-8')as f:
        red=eval(f.read()[5:])
    if red['text_hour']==t:
        return text
    else:
        with open('./data/time.py','w',encoding='utf-8')as f:
            text=requests.get("https://v1.hitokoto.cn/?c=f&encode=text").text
            red['text_hour']=datetime.datetime.now().hour
            red['text']=text
            f.write(f'time={red}')
        return text
hour(datetime.datetime.now().hour)
    