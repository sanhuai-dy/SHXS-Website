function buyPropsAjax(propId){
    $.get('/store/buy?prop_id='+propId,function(result){
        $('.shop-board').html(result['data'])
        $('.shop-mask').show();
        setTimeout(function(){
            $('.shop-mask').hide();
        },1500)
    })
}

function dataInit(propId,callback){
  $.get('/game/data_init?prop_id='+propId,function(result){
    if(result['code'] == 0){
      callback();
    }
  })
}
