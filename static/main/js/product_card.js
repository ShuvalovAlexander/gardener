document.addEventListener('DOMContentLoaded', function () {
    let thumbnailSlider = new Swiper('.thumbnail-slider', {
        direction: 'horizontal',
        slidesPerView: 'auto',
        spaceBetween: 10,
        centeredSlides: true,
        slideToClickedSlide: true,
        mousewheel: {
            invert: false,
        },
    });

    let mainSlider = new Swiper('.main-slider', {
        slidesPerView: 1,
        spaceBetween: 10,
        loop: true,
        scrollbar: {
            el: '.swiper-scrollbar',
            draggable: true,
        },
        thumbs: {
            swiper: thumbnailSlider,
        },
    });
    
});

