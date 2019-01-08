def generate_html(profile, menu_items):
    html = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
    
        <title>{profile['basic_details']['name']}</title>
        <meta name="description" content="Personal info including CV and links.">
        <meta name="author" content="{profile['basic_details']['name']}">
        <link rel="icon" type="image/png" href="favicon.png">
    
    
        <link rel="stylesheet" href="css/reset.css">
        <link rel="stylesheet" href="css/animate-custom.css">
        <link rel="stylesheet" href="css/home.css">
        <link rel="stylesheet" href="css/main.css">
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i" rel="stylesheet">
    
        <script src="./src/jquery.min.js"></script>
        <script src="./src/home.js"></script>
    
    </head>
    
    <body>
    <div id="cent_wrap" class="cent_wrap">
        <div id="title_wrap" class="cent">
            <div id="title" class="bigtitle animated fadeInDown">
                <div id="word1">
                    {profile['basic_details']['name'].split(' ')[0]}
                </div>
                <div id="word2">
                    {profile['basic_details']['name'].split(' ')[1]}
                </div>
            </div>
            <div id="menu_wrap" class="animated fadeInUp">
                {_menu_items(menu_items)}
            </div>
        </div>
    </div>
    </body>
    
    </html>
    """
    return html


def _menu_item(text, link):
    html = f"""
    <div class="menu_item">
        <a href="{link}" {'class="soon"' if link == '#' else ''}>
            {text.upper()}
        </a>
    </div>
    """
    return html


def _menu_items(menu_items):
    html = ""
    for text, link in menu_items.items():
        html += _menu_item(text, link)
    return html
