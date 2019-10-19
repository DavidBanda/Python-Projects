from tkinter import*
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        '''
        quitButt = Button()
        quitButt["text"] = "Quit"
        quitButt["command"] = self.client_exit
        quitButt.place(x=0, y=0)
        '''

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)


        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showText)
        menu.add_cascade(label='Edit', menu=edit)

    def showImg(self):
        load = Image.open('py.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text='Hey soy un texto')
        text.pack()

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(master=root)
app.mainloop()