$(document).ready(function(){
    $('.slider').slick({
        arrows: true,
        dots: true,
        adaptiveHeight: true,
        infinite: true,
        initialSlide: 0,
        autoplay: true,
        autoplaySpeed: 1500,
        pauseOnFocus: true,
        pauseOnDotsHover: true,
        pauseOnHover: true
    }); 
});
$(document).ready(function(){
    $('.slideBar').slick({
        arrows: true,
        slidesToShow: 4,
        adaptiveHeight: true,
        infinite: true,
        initialSlide: 0,
        autoplay: true,
        autoplaySpeed: 1500,
        pauseOnFocus: true,
        pauseOnDotsHover: true,
        pauseOnHover: true,
        mobileFirst:true,
        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 4,
              }
            },
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 2,
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
              }
            },
            {
              breakpoint: 320,
              settings: {
                slidesToShow: 1,
              }
            },
          ]
    }); 
});
$(document).ready(function(){
    $('.slide__popup').slick({
        arrows: true,
        slidesToShow: 4,
        infinite: true  ,
        pauseOnFocus: true,
        pauseOnDotsHover: true,
        pauseOnHover: true,
        mobileFirst:true,
        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 4,
              }
            },
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 4,
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 4,
              }
            },
            {
              breakpoint: 320,
              settings: {
                slidesToShow: 2,
              }
            },
          ]
    }); 
});

function go(){
  document.getElementById("search__input").style.display = "block";
  document.getElementById("search").style.display = "none";
  document.getElementById("contact").style.display = "none";
}
function closeSearch(){
  document.getElementById("search__input").style.display = "none";
  document.getElementById("search").style.display = "block";
  document.getElementById("contact").style.display = "block";
}
function consent(){
  document.getElementById("tick").style.display = "block";
}