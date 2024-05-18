
var htm=document.querySelector('html')
var x=[255,255,255]
var rg=""
var a=255
var b=255
var c=255
var x1=255
var y1=255
var z1=255
var r=255
var r1=255
var r2=255
setInterval(function(){
    a=parseInt(Math.random()*255)
    b=parseInt(Math.random()*255)
    c=parseInt(Math.random()*255)
    x1=x[0]
    y1=x[1]
    z1=x[2]
    r=x[0]
    r1=x[1]
    r2=x[2]
    //console.log("rgb("+String(parseInt(Math.random()*255))+","+String(parseInt(Math.random()*255))+","+String(parseInt(Math.random()*255))+")")
    x=[a,b,c]
    
    
},3000)
setInterval(function(){
    x1+=(a-r)/100
    y1+=(b-r1)/100
    z1+=(c-r2)/100
    rg="rgb("+String(parseInt(x1))+","+String(parseInt(y1))+","+String(parseInt(z1))+")"
    htm.style.background=rg
},30) 
//时间
var goodt=document.querySelector('.time')
var dtime=document.querySelector('.now')
var timer=document.querySelector('.timer')
var date=12
var time=0
var time2=0
date=new Date()
time=date.getFullYear()+"/"+String(date.getMonth()+1)+"/"+ date.getDate()
if (date.getMinutes()<10&date.getSeconds()<10){
    time2=date.getHours() + ':0' + date.getMinutes() + ':0' + date.getSeconds()
}else if (date.getMinutes()<10&date.getSeconds()>=10){
    time2=date.getHours() + ':0' + date.getMinutes() + ':' + date.getSeconds()
}else if (date.getMinutes()>=10&date.getSeconds()<10){
    time2=date.getHours() + ':' + date.getMinutes() + ':0' + date.getSeconds()
}else{
    time2=date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
}
timer.innerHTML=time2
dtime.innerHTML=time
setInterval(function(){
    date=new Date()
    if (date.getMinutes()<10&date.getSeconds()<10){
        time2=date.getHours() + ':0' + date.getMinutes() + ':0' + date.getSeconds()
    }else if (date.getMinutes()<10&date.getSeconds()>=10){
        time2=date.getHours() + ':0' + date.getMinutes() + ':' + date.getSeconds()
    }else if (date.getMinutes()>=10&date.getSeconds()<10){
        time2=date.getHours() + ':' + date.getMinutes() + ':0' + date.getSeconds()
    }else{
        time2=date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
    }
    
    time=date.getFullYear()+"/"+String(date.getMonth()+1)+"/"+ date.getDate()
    
    timer.innerHTML=time2
    dtime.innerHTML=time
},1000)
console.log(time)
if (date.getHours()<11 & date.getHours()>=5){
    goodt.innerHTML='早上好'
}
else if (date.getHours()<14){
    goodt.innerHTML='中午好'
}
else if (date.getHours()<18){
    goodt.innerHTML='下午好'
}
else if (date.getHours()<22){
    goodt.innerHTML='晚上好'
}
else{
    goodt.innerHTML='该睡了'
}
setInterval(function(){
    date=new Date()
    time=date.getFullYear()+"/"+String(date.getMonth()+1)+"/"+ date.getDate()
    time2=date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
    console.log(time)
    if (date.getHours()<11 & date.getHours()>=5){
        goodt.innerHTML='早上好'
    }
    else if (date.getHours()<14){
        goodt.innerHTML='中午好'
    }
    else if (date.getHours()<18){
        goodt.innerHTML='下午好'
    }
    else if (date.getHours()<22){
        goodt.innerHTML='晚上好'
    }
    else{
        goodt.innerHTML='该睡了'
    }

},1000000)
//输入框
inpu=document.querySelector('.say')
sayb=document.querySelector('.sayborder')
var text=''
function enter(){
    var code=event.keyCode
    var coutr=document.querySelectorAll(".myqip").length 
    if (code==13){
        text=inpu.value
        inpu.value=""
        //<div class="qip"><span class="robotsay">HI!我是SHXD 跟我聊聊天吧！</span></div>
        var e = document.createElement("div");
        var y = document.createElement("span");
        var s = ''
        if (text.length>=26){
            console.log(1)
            for(var i=1;i<text.length;i++){
                s+=text[i]
                if (i%26==0){
                    console.log(1)
                    s+='<br />'
                }
            }
            text=s
        }
        console.log(text)
        e.className="myqip"
        e.innerHTML=text
        e.style.marginLeft=-20*(coutr+2)+'px';
        console.log(y,e)
        sayb.appendChild(e)
        var data={"say":text}
        $.get('/api/robot?data=',data,function(result){
            s=''
            console.log(result)
            if (result.length>=26){
                console.log(1)
                for(var i=0;i<result.length;i++){
                    s+=result[i]
                    if (i%26==0 & i!=0){
                        console.log(1)
                        s+='<br />'
                    }
                }
                result=s
            }
            var e1 = document.createElement("div");
            var y1 = document.createElement("span");
            e1.className="qip"
            e1.innerHTML=result
            sayb.appendChild(e1)
        })
    }
    
}
//名言
var saiapi=document.querySelector('#saidapi')
setInterval(function(){
    data={'1':1}
    $.get("/api/say?data=",data,function(result){
        saiapi.innerHTML=result
    })
},300000)

//用户
var userid=document.querySelector('.usertt')
var tip1 = document.querySelector('.TS1')
var tip2 = document.querySelector('.TS2')
var tip = document.querySelector('#tip')
if (userid.innerHTML){
    tip1.style.display='inline';
    tip2.style.display='none';

}else{
    tip1.style.display='none';
    tip2.style.display='inline';
}
if (tip.innerHTML){
    alert(tip.innerHTML)
}
