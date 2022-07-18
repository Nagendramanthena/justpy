import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls,req):
        #mainlayout
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        #drawer and the links
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="leftDrawerOpen", side="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer,classes="fit")
        scrolllist = jp.QList(a=scroller)
        a_classes = "p-4 m-3 text-lg text-blue-400  hover:text-blue-700"
        jp.A(a=scrolllist,text="Home",href="/",classes=a_classes)
        jp.Br(a=scrolllist)
        jp.A(a=scrolllist,text="Search for a word",href="/dictionary",classes=a_classes)
        jp.Br(a=scrolllist)
        jp.A(a=scrolllist,text="About me",href="/about",classes=a_classes)
        jp.Br(a=scrolllist)


        #toolbar
        jp.QBtn(a=toolbar, dense=True, flat="True", round=True, icon="menu",click = cls.move_drawer,drawer=drawer)
        toolbartitle = jp.QToolbarTitle(a=toolbar)
        jp.QAvatar(a=toolbartitle,src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg")


        Qpagecontainer = jp.QPageContainer(a=layout)
        div = jp.Div(a=Qpagecontainer, classes="bg-gray-200 h-screen p-3")
        jp.Div(a=div, text="This is the Home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                jxdjsj nj j nnxnxnxn

                """, classes="text-lg")
        jp.A(text='Search a word here', href="/dictionary", a=div,
             classes='m-2 p-2 text-xl text-white bg-blue-500 hover:bg-blue-700 ')
        return wp

    @staticmethod
    def move_drawer(widget,msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True



