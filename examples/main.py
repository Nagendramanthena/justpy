import justpy as jp

web = jp.QuasarPage(tailwind=True) # we can use quasar webpage which has better styles and can make tailwind to true.
#QBtn Quasar button



def home():
    web = jp.WebPage()
    div = jp.Div(a=web,classes="bg-gray-200 h-screen border border-black")

    div1 = jp.Div(a=div,classes="grid grid-cols-3 gap-4 p-4 ")
    in_1 = jp.Input(a=div1,placeholder="first value" ,
             classes="form-input")
    in_2 =jp.Input(a=div1,placeholder="Enter second value",classes="form-input ")
    d = jp.Div(text="result goes here...",a=div1,classes="text-gray-600")
    jp.Div(text="Just another div",a=div1,classes="text-gray-600")
    jp.Div(text="Yet another div",a=div1,classes="text-gray-600")

    div2 = jp.Div(a=div,classes="grid grid-cols-2 gap-4 p-4")
    jp.Button(a=div2,text="Calculate",click=sumup,in1 = in_1,in2 = in_2,d1=d,classes="border border-blue-500 "
                                             "m-2 py-1 px-4 rounded text-blue-600 hover:bg-red-500 hover:text-white") #if you want to split leave space before oherwise we will not get the results

    jp.Div(a=div2,text="cool interactive div",mouseenter = mouse_entered,mouseleave = mouse_left, classes="hover:bg-green-500 text-white bg-red-500  border border-gray-300 m-2 p-4")
    return web


def sumup(widget,msg):
    sum = float(widget.in1.value)/float(widget.in2.value)
    widget.d1.text = sum

def mouse_entered(widget,msg):
    print("hello")
    widget.text = "mouse entered the house"

def mouse_left(widget ,msg):
    widget.text = "mouse left the house"
jp.Route("/",home)
jp.justpy(port=3003)

