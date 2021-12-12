from tkinter import *
root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0,"enter your name")
def myClick():
    myLabel = Label(root, text="hello " + e.get(), padx= 50)
    # OR (create a variable)
    
    # hello = "hello " + e.get()
    myLabel.pack()
mybutton = Button(root, text= "CLICK ME !",command=myClick)
mybutton.pack()
root.mainloop()  