from bs4 import BeautifulSoup
import requests
import random
def fanyi(word):
    url='https://fanyi.baidu.com/sug'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'}
    data={'kw':word}
    resp=requests.post(url=url,headers=head,data=data).json()
    respv=resp['data'][0]['v']
    k=list(respv)
    respm=''
    lis=[[],[]]
    # for j in range(97,123):
    #     if chr(j) in list(respv) and chr(j) != respv[0]:
    #         lis[0].append(k.index(chr(j)))
    #         k[lis[0][-1]-1]='\n'
    # for i in k:
    #     respm+=i
    return respv
o=fanyi('hello')
o.replace(' ','').replace('\n','')
print(o[2:])

def scrword(word):
    url=f'https://hanyu.baidu.com/s?wd={word}'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'}
    data={'wd': word}
    resp=requests.get(url=url,headers=head,data=data)
    if '<dd>' in resp.text:
        start=resp.text.find('<dd>')
        end=resp.text.find('</dd>')
        resptext=resp.text[start:end]
        start=resptext.find('<p>')+24
        end=resptext.find('</p>')-37
        resptext=resptext[start:end]
        resptext.replace('\n','')
        resptext.replace(' ','')

    else:
        return f'未能找到“{word}”的释义'
    return resptext

#fight fight fight 战斗 parse parse parse解析
def chengyu(word):
    url='http://chengyu.chinahuasheng.cn/search/'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'}
    data={'zi1': word,'zi2':'','zi3': '','zi4':''}
    resp=requests.post(url=url,headers=head,data=data)
    if '<ul><li><a href=' in resp.text:
        m=resp.text.find('的意思"')+5
    else:
        l=0
        return f'未能找到以“{word}”开头的成语，我输了'
    return resp.text[m:m+4]


def checkCY(word):
    if len(word) < 4 or len(word) > 4:
        return False
    for i in word:
        if 13000>ord(i) or ord(i) > 41000:
            return False
    url='http://chengyu.chinahuasheng.cn/search/'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'}
    data={'zi1': word[0],'zi2':word[1],'zi3': word[2],'zi4':word[3]}
    resp=requests.post(url=url,headers=head,data=data)
    if '<ul><li><a href=' in resp.text:
        return True
    return False

def randomword():
    liststr='以一亿亦伊易义阿呵爱艾矮按安案暗岸把罢拔巴八倍被杯背北备本笨奔蹦绷侧侧策厕恻擦拆柴差钗岑参层曾惨残餐灿蚕禅缠铲蝉吃池持赤迟齿尺大打答达搭嗒带待代戴待代呆但弹单单丹淡胆担旦诞的得地德对堆顿敦钝遁动洞东栋董冬等登灯瞪登恩发法伐罚乏伐服服富夫付反饭烦凡翻番范凡放防芳房方仿访分分粉芬粪风封丰冯峰嘎呷旮感肝干赶敢甘刚钢纲纲岗滚衮贵鬼归桂魂混昏浑行行行行航夯沆了乐勒呵及几即吉既吉'
    return chengyu(liststr[random.randint(0,len(liststr)-1)])

def fukp(level):
    url=f'https://fun.886.be/api.php?level={level}'
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'}
    data={'level':level}
    msg=(requests.get(url=url,headers=head,data=data).text)
    return msg

def tianqi(adcode):
    key='58f3545cdfee67b47eabc86297f79e4c'
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'}
    url=f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={key}"
    msg=eval((requests.get(url=url,headers=head).text))['lives'][0]
    return msg

