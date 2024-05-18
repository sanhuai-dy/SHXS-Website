//snow
var htmlr=document.querySelector('html')
var htmlwidth=htmlr.offsetWidth;
var htmlheight=Math.max(window.screen.availHeight,htmlr.offsetHeight);
var text=["*","i","O","o","&","#",".",",",'*',"原神","SHXS",'0','1']
var litranform=[0,0,0,0,0,0]
var body=document.querySelector('body')
var snowdict={}
var qi=0;
var snows=setInterval(function(){
    var snow = document.createElement("div");
    litranform[0]=Math.random()*360
    litranform[1]=Math.random()*360
    litranform[2]=Math.random()*360
    litranform[3]=Math.random()*360
    litranform[4]=Math.random()*360
    litranform[5]=(Math.random()*3)/2-0.75
    snowdict[String(qi)]={}
    snowdict[String(qi)]["pos"]={'0':Math.random()-100,'1':Math.random()*htmlwidth}
    snowdict[String(qi)]['speed']=(Math.random()+5)/5
    snowdict[String(qi)]['mas']=0.9
    
    if (Math.random()>0.5){
        snowdict[String(qi)]['xspeed']=(Math.random()*0.3)
    }else{
        snowdict[String(qi)]['xspeed']=-(Math.random()*0.3)
    }
    snow.className='snow';
    snow.style.top=String(snowdict[String(qi)]["pos"]['0'])+'px'
    snow.style.right=String(snowdict[String(qi)]["pos"]['1'])+'px'
    snow.innerHTML=text[parseInt(Math.random()*text.length)]
    body.appendChild(snow)
    qi++;
    snow.style.transform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[0]+litranform[5])+'deg)'
	snow.style.msTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[1]+litranform[5])+'deg)'
	snow.style.mozTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[2]+litranform[5])+'deg)'
	snow.style.webkitTransform='scale('+(Math.random()+1.7)/2+') rotate('+(litranform[3]+litranform[5])+'deg)'
	snow.style.oTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[4]+litranform[5])+'deg)'
},300)
var rand=0
var snowy=document.querySelectorAll('.snow')

setInterval(function(){
    snowy=document.querySelectorAll('.snow')
    
    for(var i=0;i<snowy.length;i++){
        if (snowdict[String(i)]["pos"]['0']>= htmlheight-300){
            if (snowy[i]==undefined){
                return true
            }
            snowdict[String(i)]["mas"]-=0.01;
            
            if (snowdict[String(i)]["mas"]<=-0.4){
                clearInterval(snows)
                snowdict[String(i)]["mas"]=0.9;
                snowy[i].style.color="rgba("+(Math.random+8)/8*169+","+(Math.random+7)/8*238+","+(Math.random+6)/8*255+", "+String(snowdict[String(i)]["mas"])+")"
                snowdict[String(i)]["pos"]={'0':Math.random()-100,'1':Math.random()*htmlwidth}
                snowy[i].innerHTML=text[parseInt(Math.random()*text.length)]
                litranform[0]=Math.random()*360
                litranform[1]=Math.random()*360
                litranform[2]=Math.random()*360
                litranform[3]=Math.random()*360
                litranform[4]=Math.random()*360
                litranform[5]=(Math.random()*3)/2-0.75
                snowy[i].style.transform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[0]+litranform[5])+'deg)'
                snowy[i].style.msTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[1]+litranform[5])+'deg)'
                snowy[i].style.mozTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[2]+litranform[5])+'deg)'
                snowy[i].style.webkitTransform='scale('+(Math.random()+1.7)/2+') rotate('+(litranform[3]+litranform[5])+'deg)'
                snowy[i].style.oTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[4]+litranform[5])+'deg)'
            }
        }
        snowdict[String(i)]["pos"]['1']+=snowdict[String(i)]["xspeed"]
        snowdict[String(i)]["pos"]['0']+=snowdict[String(i)]["speed"]
        //snowy[i].style.boxShadow='1px 4px 10px rgba(0, 0, 0, '+String(0.39*(snowdict[String(i)]["mas"]+0.1))+')'
        snowy[i].style.textShadow='1px 4px 10px rgba(0, 0, 0, '+String(0.39*(snowdict[String(i)]["mas"]+0.1))+')'
        snowy[i].style.color="rgba("+(Math.random+7)/8*255+","+(Math.random+7)/8*255+","+(Math.random+6)/8*255+", "+String(snowdict[String(i)]["mas"])+")"
        snowy[i].style.top=String(snowdict[String(i)]["pos"]['0'])+'px'
        snowy[i].style.right=String(snowdict[String(i)]["pos"]['1'])+'px'
        snowy[i].style.transform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[0]+litranform[5])+'deg)'
        snowy[i].style.msTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[1]+litranform[5])+'deg)'
        snowy[i].style.mozTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[2]+litranform[5])+'deg)'
        snowy[i].style.webkitTransform='scale('+(Math.random()+1.7)/2+') rotate('+(litranform[3]+litranform[5])+'deg)'
        snowy[i].style.oTransform= 'scale('+(Math.random()+1.7)/2+') rotate('+(litranform[4]+litranform[5])+'deg)'
    }    
},8)