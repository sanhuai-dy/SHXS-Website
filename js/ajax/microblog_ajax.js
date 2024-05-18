function loading_more(showMicroblog){
    $.get('/microblog/load', function (result) {
        showMicroblog(result);
    });
}

function head_update(img){
    head_image = img.src.split('/');
    head_image = head_image[head_image.length - 1];
    $.get('/user/update?head=' + head_image,function(result){
        if(result['state'] == 'success'){
            window.location.reload();
        }
    })
}