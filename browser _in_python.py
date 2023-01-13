# import webbrowser
# url = 'https://codefather.tech/blog/'  
# webbrowser.open(url)

# import webbrowser
# webbrowser.get()


# import webbrowser
# url = 'https://google.com'
# browser = 'safari'
# webbrowser.get(browser).open(url)

import webbrowser
urls = ['www.google.com', 'www.youtube.com', 'www.bbc.com']
browser = 'firefox'
for url in urls:
    webbrowser.get(browser).open_new_tab(f'https://{url}')