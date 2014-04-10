$(document).ready(
    function() {
        $('.thumbnail img').click(
            function(event) {
                var scale = 150 / 100;
                var pos = $(this).offset();
                var clickX = event.pageX - pos.left;
                var clickY = event.pageY - pos.top;
                var container = $(this).parent().get(0);

                $(this).css({
                    width: this.width * scale,
                    height: this.height * scale
                });

                container.scrollLeft = ($(container).width() / -2) + clickX * scale;
                container.scrollTop = ($(container).height() / -2) + clickY * scale;
            }
        );
    }
);