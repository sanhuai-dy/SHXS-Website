var ajax_flag = false;
var blog_id = $('.kid-info-title').attr('data-blog-id');

//点赞
function like_on(img){
    if(ajax_flag)return;
    ajax_flag = true;
    var likes = $('.kid-info-like span').html();
    $.get('/like/create?blog_id='+blog_id,function(result){
        if(result.status == 'success'){
            $(img).attr('src','/static/images/like.png').attr('onclick','like_cancle(this)');
            $('.kid-info-like span').html(parseInt(likes) + 1);
            ajax_flag = false;
        }else{
            window.location.href = "/user/login";
        }
    })
}

//取消点赞
function like_cancle(img){
    if(ajax_flag)return;
    ajax_flag = true;
    var likes = $('.kid-info-like span').html();
    $.get('/like/delete?blog_id=' + blog_id,function(result){
        if(result.status == 'success'){
            $(img).attr('src','/static/images/like-no.png').attr('onclick','like_on(this)');
            $('.kid-info-like span').html(parseInt(likes) - 1);
            ajax_flag = false;
        }else{
            window.location.href = "/user/login";
        }
    })
}

//发表评论
function comment_pub(){
    if(ajax_flag)return;
    ajax_flag = true;
    var textarea = $('.kid-info-textarea textarea')
    var content = textarea[0].value;
    data = {'blog_id':blog_id,'content':content}
    $.post('/comments/create',data,function(result){
        if(result['status'] == 'success'){
            $.get('/comments/list?blog_id=' + blog_id,function(result){
                //成功返回
                comment_list = result.data;
                //重置评论框
                $('.kid-info-message img').click();
                textarea[0].value = '';
                //评论数增加
                comments_count = $('.kid-info-message span').html();
                $('.kid-info-message span').html(parseInt(comments_count) + 1);
                //最新评论显示
                $('.kid-info-comlist').html('')
                for(var i = 0;i<comment_list.length;i++){
                    var comment = comment_list[i];
                    var comment_template =
                            '<div class="kid-comlist-item">'+
                                '<div class="com-photo" style="background-image:url(/static/images/'+comment['author'].head+')"></div>'+
                                '<div class="com-username">'+comment['author'].username+'</div>'+
                                '<div class="com-time">'+comment.create_time+'</div>'+
                                '<div class="com-content">'+comment.content+'</div>'+
                                '<div style="clear: both;"></div>'+
                            '</div>';
                    $(comment_template).appendTo($('.kid-info-comlist'));
                }
                ajax_flag = false;
            })
        }else{
            console.log(result['data'])
            window.location.href = "/user/login";
        }
    });
}