var htmlr=document.querySelector('html');
//获取blog
$.post('/getblog?send=',{"title":1,"text":3},function(result){
    /*
    <a href="#" class="bloglook"><div class="blog">
        <span class="title">123123</span>
        <span class="subtitle">123123</span>
    </div></a>
    */
    result=result['0']
    var hij=document.querySelector('.hij')
    var all=document.querySelector('.all')
    for(var i=0;i<result.length;i++){
        e1 = document.createElement("a");
        e2 = document.createElement("div");
        y1 = document.createElement("span");
        y2 = document.createElement("span");
        e1.href='/blog/'+result[i]['blogname'];
        e1.className='bloglook';
        e2.className='blog';
        y1.className='title';
        y2.className='subtitle';
        y1.innerHTML=result[i]['title'];
        y2.innerHTML=String(result[i]['text']).substring(0,30);
        e1.style.marginTop=String(50*(i+1))+'px';
        y2.innerHTML=y2.innerHTML.replace(/<br>/g," ")
        e2.appendChild(y1);
        e2.appendChild(y2);
        e1.appendChild(e2);
        var hij=document.querySelector('.hij')
        hij.appendChild(e1);
        all.style.height=result.length*160+450+'px'
        console.log(1);
    }
})

//签到
var blogqd=document.querySelector('.blogqd')
blogqd.onclick = function(){
    alert('签到成功~~~经验+0')
}

