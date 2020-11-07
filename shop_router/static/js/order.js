function orderPlus(){
$('.plus-btn').click(function(){
var url = $(this).data('action')
var $this = $(this)
$.get(url,function(data){
if(data.status === 200){
var count = $this.closest('.quantity__block').find('.count')
count.text(Number(count.text()) + Number(1))
}
})
})
}

function orderMinus(){
$('.minus-btn').click(function(){
var url = $(this).data('action')
var $this = $(this)
$.get(url,function(data){
if(data.status === 200){
var count = $this.closest('.quantity__block').find('.count')
count.text(Number(count.text()) - Number(1))
}
})
})
}



