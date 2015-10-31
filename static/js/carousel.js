(function() {
    $('.carousel-indicators')
        .children()
        .first()
        .addClass('active');
    $('.carousel-inner')
        .find('.item')
        .first()
        .addClass('active');
    $('.carousel').carousel({
        interval: 5000
    });
}());
