import webbrowser
def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Wrong url")
        print("Thist is text after function")
    return wrapper
@validator    
def open_url(url):
    webbrowser.open(url)
open_url("https://wwwyoutubecom/watch?v=tuFuDKE7DF8&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa&index=20")
print("Грейт Ворк")
