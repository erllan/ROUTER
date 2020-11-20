    $(document).ready(function(){


    $('a.addToCard').click(function(event){
event.preventDefault()
var url = $(this).attr('href')
var iconPlus = $(this).find('.plus')
iconPlus.html('	&#10003;')
})
$('.drop-link').hover(function(){

var id = $(this).attr('data-id')
$.get('/category-data/',{'id':id},function(response){
$('.dropdown-content-routers').html('')
for(var i = 0; i < response.length;i++){
$('.dropdown-content-routers').append($('<a href="/routers/'+response[i]['id']+'" class="drop__link-routers">'+response[i]['category']+'</a>'))


}
})
})

$('.view').click(function(){
var id = $(this).attr('data-id')
var url = '/product-data/'
$.get(url,{"id_object":id},function(rest){
$('.popup__feature').html(rest.title)
$('.popup__text-modem').html(rest.description)
$('#safety').html(rest.safety)
$('#interface').html(rest.interface)
$('#size').html(rest.size)
$('.stock__colour').html(rest.color)
$('.price__feature-cost').html(rest.price)
$('.more__info').attr('href','/product/'+id)
$('.popup__img').attr('src',rest.album_set[0]['photo'])
$.get('/in-basket/',{'id':id},function(respon){
event.preventDefault()
$('.on__trash').html('<a href="#popup" class="onTrash">Добавить в корзину</a>')
if(respon.status ==='no'){
$(".on__trash").click(function(){
$.get('/addProductToBascet/'+id,function(res){
event.preventDefault()
if(res.status === 200){
$('.on__trash').html('<a href="#popup" class="onTrash">уже в корзине</a>').css('color','white')
}
})})}
else if(respon.status ==='yes'){
$('.on__trash').html('<a href="#popup" class="onTrash">уже в корзине</a>')

}

})

})
})
$('.plus').click(function(){
$.get('/count-order/',function(response){
$('.ball h6').html(response.result)

})
})






    })


