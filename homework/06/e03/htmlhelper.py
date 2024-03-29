from importlib import import_module
def generate_html_page(title, content):
    """
    Function will return a valid html5 page as string.
    """

    
    valid_page = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
        {content}
        
    </body>
    </html>"""
    return valid_page