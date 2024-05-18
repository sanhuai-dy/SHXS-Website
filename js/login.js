var submit=document.querySelector('.submit')
var usertext=document.querySelector('.usertext')
var passtext=document.querySelector('.passtext')
var see=document.querySelector('.see')
var goindex=document.querySelector('.goindex')
var p=0
see.onclick = function(){
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
    var username=document.querySelector('.username').value
    var password=document.querySelector('.password').value
    data_re={'username':username,'password':password}
    $.post('/login?data_re=',data_re,function(result){
        result=String(result)
        console.log(result)
        if (result=='1'){
            passtext.innerHTML='密码错误'
        }else if(result=='0'){
            usertext.innerHTML='用户名不存在'
        }else{
            window.location.href="/"
            goindex.style.display='block'
        }
    },"json")
}