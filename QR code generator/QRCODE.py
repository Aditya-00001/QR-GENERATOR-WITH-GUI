import qrcode
from tkinter import *
from PIL import Image, ImageTk
from CTkMessagebox import ctkmessagebox

class QrCode:
    def __init__(self, root):
        self.root = root
        self.root.title('QR CODE GENERATOR')
        self.root.geometry("500x500")
        self.root.resizable(0, 0)
        self.img = Image.open(r"FILE LOCATION")
        self.img = self.img.resize((500, 500))
        self.img = ImageTk.PhotoImage(self.img)
        self.show_img = Label(self.root, image=self.img)
        self.show_img.place(x=0, y=0, width=500, height=500)
        #
        Label(self.root, text='Enter the text', font=('arial', 20, 'bold'), fg='White',bg='purple').place(x=95,y=50)
        self.input = Text(self.root, width=34, font='15', bg='white', relief=FLAT, borderwidth=3)
        self.input.place(x=95, y=120, height=35)
        Label(self.root, text='Enter the file name', font=('arial', 20, 'bold'), fg='White',bg='purple').place(x=95,y=190)
        self.input2 = Entry(self.root, width=34, font='15', bg='white', relief=FLAT, borderwidth=3)
        self.input2.place(x=95, y=260, height=25)
        btn_short = Button(self.root, relief=GROOVE, text="Create", font=('verdana', 10, 'bold'), bg="blue",
                           fg="white", command=self.create)
        btn_short.place(x=210, y=310, width=65, height=25)

    def create(self):
        self.text = self.input.get('0.0','end')
        self.name = self.input2.get()

        if self.name == '':
            ctkmessagebox.CTkMessagebox(title='Invalid Information',message='Enter a Valid File Name')
        else:
            self.img = qrcode.make(self.text)
            self.img_name = self.name+'.jpg'
            self.img.save(self.img_name)
            self.img = Image.open(r"FILE LOCATION")
            self.img = self.img.resize((500, 500))
            self.img = ImageTk.PhotoImage(self.img)
            self.show_img = Label(self.root, image=self.img)
            self.show_img.place(x=0, y=0, width=500, height=500)
            #---------------------------------------------------------------------------------------------#
            self.show_image = Image.open('FILE LOCATION')
            self.show_image = self.show_image.resize((300, 300))
            self.show_image = ImageTk.PhotoImage(self.show_image)
            self.show_img2 = Label(self.root, image=self.show_image)
            self.show_img2.place(x=100, y=100)
            Label(self.root, text='QR CODE GENERATED, PLEASE CHECK THE FOLDER WHERE THIS APP IS STORED',
                  bg='purple',fg='white').place(x=0,y=50)



if __name__ == '__main__':
    rt = Tk()
    obj = QrCode(rt)
    rt.mainloop()
