from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Whatever')
root.iconbitmap('C:\\Users\\Administrator\\Documents\\MuseScore3\\5135073.ico')
my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Administrator\\Desktop\\NEW SHIT\\course.png"))


myLabel = Label(image=my_img)
myLabel.pack()
mybutton = Button(root, text= "CLICK ME !",command=root.quit)
mybutton.pack()
root.mainloop()