var submit=document.querySelector('.submite')
var title=document.querySelector('.titlee')
var text=document.querySelector('.textt')
submit.onclick=function(){
    title=document.querySelector('.titlee').value
    text=document.querySelector('.textt').value
    console.log(title,text)
    $.post('/getsend?send=',{"title":title,"text":text},function(result){
        if (result=='1'){         
            alert("发送成功")
            window.location.href="/blog"
        }else{
            alert("发送失败")
        }
    })
}

