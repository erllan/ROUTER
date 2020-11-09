    $(document).ready(function(){
    $('a.addToCard').click(function(event){
event.preventDefault()
var url = $(this).attr('href')
var iconPlus = $(this).find('.plus')
iconPlus.html('	&#10003;')
})
    })
