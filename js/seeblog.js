var button=document.querySelectorAll('.buttons')
var sure=document.querySelector('.sure')
var blogid=document.querySelector('.blogid').innerHTML
button[0].onclick = function(){
    sure.style.display='block';
}
button[1].onclick = function(){
    sure.style.display='none';
}
button[2].onclick = function(){
    console.log(blogid)
    $.post('/blog/del?blogid=',{'blogid':blogid},function(result){
        if (result=='0'){
            alert('删除成功')
            window.location.href="/blog"
        }else{
            alert('你不是blog发表人，无法删除！')
        }
    },"json")
}
