(function() {
    // Gets the current page from the <title>
    // and activates the corresponding navbar item
    var
        getTitleText = function() {
            var list = $('title').text().split('|');
            if (list.length === 1) return undefined;
            return list[0].trim();
        },

        getNavbarItems = function() {
            return $('#site-navbar').find('li');
        }, titleText = getTitleText(), navBarItems = getNavbarItems();

    if (!titleText) return navBarItems.first().addClass('active');

    return navBarItems.each(function() {
        var self = $(this);
        if (self.find('a').text() === titleText)
            self.addClass('active');
    });

}());
