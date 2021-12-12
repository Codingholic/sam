from tkinter import *
root = Tk()
# mybutton = Button(root, text= "CLICK ME !", padx = 20, pady = 20, state=DISABLED)

def myClick():
    myLabel = Label(root, text="i clicked a buuton!")
    myLabel.pack()
mybutton = Button(root, text= "CLICK ME !",command=myClick)
mybutton.pack()
root.mainloop()  