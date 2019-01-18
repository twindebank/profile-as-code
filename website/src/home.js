$.fn.resizeFont = function (size) {
        var curr_fnt_size = parseInt($(this).css('font-size'));
        var newsize = curr_fnt_size + size
        $(this).css('font-size', curr_fnt_size + size)
    };
    var sizeHeader = function (recursive) {
        var win_width = $(window).outerWidth();
        var title_width = $("#title").outerWidth();
        var title = $(".bigtitle");
        var menu = $("#menu_wrap")
        if (title_width > win_width) {
            title.resizeFont(-10);
            if (recursive) {
                sizeHeader(1)
            }
        }
        else if (title_width < win_width && parseInt(title.css('font-size')) < 100) {
            title.resizeFont(+10);
            if (recursive) {
                sizeHeader(1)
            }
        }

        titlesize = parseInt(title.css('font-size'))
        menu.css("font-size", 8 + titlesize / 6);
    };
    $(window).resize(function () {
        sizeHeader(0);
    });

    $(document).ready(function () {
        sizeHeader(1);

        $("a.transition").click(function (event) {
            event.preventDefault();
            linkLocation = this.href;
            $("#cent_wrap").fadeOut(500, redirectPage);
        });

        function redirectPage() {
            window.location = linkLocation;
        }

        $("a.soon").click(function (event) {
            event.preventDefault();
            var link = $(this)
            link.fadeOut(200, function () {
                link.html("Soon...")
                link.css("color", "#999999")
                link.fadeIn(200)
            })

        });

        function Reload() {
            try {
                var headElement = document.getElementsByTagName("head")[0];
                if (headElement && headElement.innerHTML)
                    headElement.innerHTML += "<meta http-equiv=\"refresh\" content=\"1\">";
            }
            catch (e) {
            }
        }

        if ((/iphone|ipod|ipad.*os 5/gi).test(navigator.appVersion)) {
            window.onpageshow = function (evt) {
                if (evt.persisted) {
                    document.body.style.display = "none";
                    location.reload();
                }
            };
        }
    });


    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
            m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-23081119-2', 'auto');
    ga('send', 'pageview');