import justpy as jp

#About(jp.QusarPage) ____ inheritance and pass self instead of wp varialbe

class About:
    path = "/about"

    @classmethod
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp,classes = "bg-gray-200 h-screen")
        jp.Div(a=div,text="This is the about page",classes = "text-4xl m-2")
        jp.Div(a=div,text="""
        jxdjsj nj j nnxnxnxn
        
        """,classes = "text-lg")
        return wp

