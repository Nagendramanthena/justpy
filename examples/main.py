import justpy as jp



def home():
    web = jp.WebPage()
    jp.Div(a=web,text="hello world")
    jp.Div(a=web,text="another div")
    return web
jp.Route("/",home)
jp.justpy()