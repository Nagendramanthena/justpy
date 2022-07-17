import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                jxdjsj nj j nnxnxnxn

                """, classes="text-lg")
        jp.A(text='Search a word here', href="/dictionary", a=div,
             classes='m-2 p-2 text-xl text-white bg-blue-500 hover:bg-blue-700 ')
        return wp



