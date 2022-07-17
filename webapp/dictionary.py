import justpy as jp

import defintion


class Dictionary:
    path = "/dictionary"
    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        div =  jp.Div(a=wp,classes = "bg-blue-400 h-screen")
        jp.Div(a=div,text="Instant Dictionary app",classes = "text-4xl m-2 p-4")

        jp.Div(a=div,text="Get the definiton of any English word instantly as yout type",classes='text-lg')
        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        outputdiv = jp.Div(a=input_div, text="content goes here ...",
                           classes="m-2 p-2 text-lg border-2 border-grey-300 h-40 rounded")
        Inputbox = jp.Input(a=div,placeholder="Type in a word here..",
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline:none focus:border-green-500 "
                 "py-2 px-4 rounded",output_div = outputdiv)
        Inputbox.on('input',cls.get_definiton)
     #   jp.Button(a=input_div, text="Get Definition",classes = "border-2 border-gray-400 text-gray-500 rounded",inp = Input,click=cls.get_definiton,output_div = outputdiv)
        return wp

    @staticmethod
    def get_definiton(widget,msg):
        defined = defintion.Definition(widget.value).getdefiniton()
        widget.output_div .text= "".join(defined)




    #request handler and event handlers
