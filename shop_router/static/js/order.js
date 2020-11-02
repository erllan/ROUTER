
function order(){
    $('#plus').on('click',function(event){
  		event.preventDefault();
  		var count = $('#count')
  		var url = $(this).attr('href');
  		$.get(`${url}`,function(response){
  			if(response.result == 'yes'){
  				count.html(Number(count.html()) +1)
  			}
  		
  		})
    })


}
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
