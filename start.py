import time,os
while 1:
    try:
        print(2)
        f=open('./info.txt','r',encoding='utf-8')
        x=f.read()
        if x=='1':
            os.system(r'python3 index.py')
            print('right')
        else:
            v=open('./info.txt','w',encoding='utf-8')
            v.write('1')
            v.close()
        f.close()
        
    except:
        print(1)
        v=open('./info.txt','w',encoding='utf-8')
        v.close()
    time.sleep(5)