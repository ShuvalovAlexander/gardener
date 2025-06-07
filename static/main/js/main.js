document.addEventListener('DOMContentLoaded', function() {
  var swiper = new Swiper(".mySwiper", {
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {       
        delay: 3000,    
        disableOnInteraction: false 
    },
    loop: true,
    slidesPerView: 3,
    spaceBetween: 30
  });
});
