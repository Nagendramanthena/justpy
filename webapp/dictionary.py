import justpy as jp

import defintion
import requests


class Dictionary:
    path = "/dictionary"
    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        # drawer and the links
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="leftDrawerOpen", side="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        scrolllist = jp.QList(a=scroller)
        a_classes = "p-4 m-3 text-lg text-blue-400  hover:text-blue-700"
        jp.A(a=scrolllist, text="Home", href="/", classes=a_classes)
        jp.Br(a=scrolllist)
        jp.A(a=scrolllist, text="Search for a word", href="/dictionary", classes=a_classes)
        jp.Br(a=scrolllist)
        jp.A(a=scrolllist, text="About me", href="/about", classes=a_classes)
        jp.Br(a=scrolllist)

        # toolbar
        jp.QBtn(a=toolbar, dense=True, flat="True", round=True, icon="menu", click=cls.move_drawer, drawer=drawer)
        toolbartitle = jp.QToolbarTitle(a=toolbar)
        jp.QAvatar(a=toolbartitle, src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg")

        Qpagecontainer = jp.QPageContainer(a=layout)
        div =  jp.Div(a=Qpagecontainer,classes = "bg-blue-400 h-screen")
        jp.Div(a=div,text="Instant Dictionary app",classes = "text-4xl m-2 p-4")

        jp.Div(a=div,text="Get the definiton of any English word instantly as you type",classes='text-lg')
        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        outputdiv = jp.Div(a=input_div, text="content goes here ...",
                           classes="m-2 p-2 text-lg border-2 border-grey-300 h-40 rounded")
        Inputbox = jp.Input(a=div, placeholder="Type in a word here..",
                            classes="m-2 bg-gray-100 border-2 border-gray-200 rounded  focus:bg-white focus:outline:none focus:border-green-500 "
                                    "py-2 px-4 rounded", output_div=outputdiv)
        Inputbox.on('input', cls.get_definiton)
     #   jp.Button(a=input_div, text="Get Definition",classes = "border-2 border-gray-400 text-gray-500 rounded",inp = Input,click=cls.get_definiton,output_div = outputdiv)
        return wp

    @staticmethod
    def get_definiton(widget,msg):
        req = requests.get(f"http://127.0.0.1:8003/api?word={widget.value}")
        data = req.json()

        widget.output_div.text= " ".join(data['definition'])

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True




    #request handler and event handlers
