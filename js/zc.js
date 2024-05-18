
var see=document.querySelector('.see')
var submit=document.querySelector('.submit')
var username=''
var password=''
var repassword=''
var repasstext=document.querySelector('.repasstext')
var p=0
var passtext=document.querySelector('.passtext')
var usertext=document.querySelector('.usertext')
var gologin=document.querySelector('.gologin')
var endname=''
var thatname=''
var xx=0
see.onclick = function(){
    console.log(passtext,usertext)
    password=document.querySelector('.password')
    if (p==0){
        p=1;
        password.type='text'
        }
    else{
        p=0;
        password.type='password'
        }
    
}

submit.onclick = function(){
    passtext.innerHTML=''
    usertext.innerHTML=''
    repasstext.innerHTML=''
    username=document.querySelector('.username').value
    password=document.querySelectorAll('.password')[0].value
    repassword=document.querySelectorAll('.password')[1].value
    
    if (username.length<4){
        console.log(1)
        usertext.innerHTML='用户名过短！用户名需要由至少四个字符组成！'
    }else if(password.length<6){
        console.log(2)
        passtext.innerHTML='密码过短！密码至少由六个字符组成！'
    }else if(password != repassword){
        console.log(3)
        repasstext.innerHTML='前后密码不一致'
    }else{
    
        data_re={'username':username,'password':password,'repassword':repassword}
        $.post('/zc?data_re=',data_re,function(result){
            thatname=result
            console.log('注册',result)
            console.log(thatname)
            if (thatname==username){
                usertext.innerHTML='用户名已存在'
            }else{
                window.location.href="/"
                gologin.style.display='block'
                
            }
        },"json")
        
        }
}
