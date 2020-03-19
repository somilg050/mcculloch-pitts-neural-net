from tkinter import *
import numpy as np
from PIL import ImageTk,Image
import math
 
root = Tk()
 
photoXOR = PhotoImage(file="XOR.png")
photoAND = PhotoImage(file="AND1.png")
photoOR = PhotoImage(file="OR.png")
photoHNC = PhotoImage(file="HNC.png")
 
root.title("McCulloh-Pitts Assignment")
root.geometry('1000x400')
root.configure(background="white")
 
res=0
def OR(x1,x2):
    X = np.array([x1,x2])
    W = np.array([2,2])
    threshold = 2
    if (np.dot(X,W.T) >= threshold):
        return 1
    else:
        return 0
 
def AND(x1,x2):
    X = np.array([x1,x2])
    W = np.array([1,1])
    threshold = 2
    if (np.dot(X,W.T) >= threshold):
        return 1
    else:
        return 0
 
def AND_NOT(x1,x2):
    X = np.array([x1,x2])
    W = np.array([2,-1])
    threshold = 2
    if (np.dot(X,W.T) >= threshold):
        return 1
    else:
        return 0
 
def XOR(x1,x2):
    z1 = AND_NOT(x1,x2)
    z2 = AND_NOT(x2,x1)
    y = OR(z1,z2)
    return y
 
 
lbl1 = Label(root, text = "Assignment - 1: Neural Networks and Fuzzy Logic", font=("Arial", 15), bg="white")
lbl1.place(x=280, y=0)
 
lbl2 = Label(root, text="Semester-2 (2019-2020)", font=("Arial", 14), bg="white")
lbl2.place(x=380, y=25)
 
lbl2 = Label(root, text="By:", font=("Arial", 13), bg="white")
lbl2.place(x=480, y=75)
 
lbl2 = Label(root, text="Somil Gupta (2017A7PS0142G)", font=("Arial", 14), bg="white")
lbl2.place(x=360, y=100)
lbl2 = Label(root, text="Hardik Gupta (2016A7PS0390G)", font=("Arial", 14), bg="white")
lbl2.place(x=360, y=125)
 
lbl2 = Label(root, text="Under the guidance of Professor Basbadatta Sen Bhattacharya", font=("Arial", 13), bg="white")
lbl2.place(x=200, y=200)
 
lbl2 = Label(root, text="Click to load corresponding GUI", font=("Arial", 8), bg="white")
lbl2.place(x=430, y=260)
 
def new_XOR_win():
    newwin = Toplevel(root)
    newwin.title('XOR Gate')
    l = Label(newwin,image=photoXOR)
    l.image=photoXOR
    l.grid()
    e1 = Entry(newwin, width=10, bg="white")
    e1.place(x=115, y=230)
    e2 = Entry(newwin, width=10, bg="white")
    e2.place(x=115, y=400)
 
    def myClick():
        x1 = bool(int(e1.get()))
        x2 = bool(int(e2.get()))
        output1 = (x2 and (not x1))
        output2 = (x1 and (not x2)) 
        output3 = output1 or output2
        myLabel = Label(newwin, width=10, text=output1, bg="white")
        myLabel.place(x=390,y=230)
        myLabel2 = Label(newwin, width=10, text=output2, bg="white")
        myLabel2.place(x=390,y=400)
        myLabel3 = Label(newwin, width=13, text="OUTPUT: "+ str(int(output3)), bg="white")
        myLabel3.place(x=610,y=315)
 
    button = Button(newwin, text="RUN", command=myClick)
    button.place(x=470, y=530)
    lbl11 = Label(newwin, text="Enter values in given blanks and press RUN", font=("Arial", 13))
    lbl11.place(x=270, y=570)
    lbl21 = Label(newwin, text="NOTE: Weights are shown at edges. T=2", font=("Arial", 13))
    lbl21.place(x=300, y=600)
 
def new_AND_win():
    def AND(x1,x2):
        X = np.array([x1,x2])
        W = np.array([1,1])
        threshold = 2
        if (np.dot(X,W.T) >= threshold):
            return 1
        else:
            return 0
    newwin = Toplevel(root)
    newwin.title('AND Gate')
    l = Label(newwin,image=photoAND)
    l.image=photoAND
    l.grid()
    e1 = Entry(newwin, width=10, bg="white")
    e1.place(x=170, y=200)
    e2 = Entry(newwin, width=10, bg="white")
    e2.place(x=170, y=440)
 
    def myClick():
        x1 = bool(int(e1.get()))
        x2 = bool(int(e2.get()))
        output =  x1 and x2
        myLabel3 = Label(newwin, width=15, text="Y_OUTPUT: "+ str(int(output)), bg="white")
        myLabel3.place(x=750,y=310)
 
    button = Button(newwin, text="RUN", command=myClick)
    button.place(x=480, y=610)
    lbl11 = Label(newwin, text="Enter values in given blanks and press RUN", font=("Arial", 13))
    lbl11.place(x=280, y=640)
    lbl21 = Label(newwin, text="NOTE: Weights W1 = 1.5 and W2 = 1.5, Threshold = 2", font=("Arial", 13))
    lbl21.place(x=240, y=670)
 
def new_OR_win():
    newwin = Toplevel(root)
    newwin.title('OR Gate')
    l = Label(newwin,image=photoOR)
    l.image=photoOR
    l.grid()
    e1 = Entry(newwin, width=10, bg="white")
    e1.place(x=150, y=180)
    e2 = Entry(newwin, width=10, bg="white")
    e2.place(x=150, y=420)
 
    def myClick():
        x1 = bool(int(e1.get()))
        x2 = bool(int(e2.get()))
        output =  x1 or x2
        myLabel3 = Label(newwin, width=15, text="Y_OUTPUT: "+ str(int(output)), bg="white")
        myLabel3.place(x=730,y=300)
 
    button = Button(newwin, text="RUN", command=myClick)
    button.place(x=480, y=610)
    lbl11 = Label(newwin, text="Enter values in given blanks and press RUN", font=("Arial", 13))
    lbl11.place(x=280, y=640)
    lbl21 = Label(newwin, text="NOTE: Weights W1 = 1, W2 = 1 and bias = -1, Threshold = 0", font=("Arial", 13))
    lbl21.place(x=220, y=670)
 
def new_HNC_win():
    newwin = Toplevel(root)
    newwin.title('HOT and COLD')
    newwin.configure(background="white")
    l = Label(newwin,image=photoHNC)
    l.image=photoHNC
    l.grid()
    new_HNC_win.t_c = 0
    
    def run(x1,x2):
        inp = [x1,x2]
        y1 = 1 if inp[0]*2 >= 2 else 0
        z2 = 1 if inp[1]*2 >= 2 else 0  
        z1 = 2 * z2 + (-1*inp[1])
        z1 = 1 if z1 >=2 else 0

        y1 = 2*z1 + 2*inp[0]
        y1 = 1 if y1 >= 2 else 0

        y2 = 1*inp[1] + 1*z2
        y2 = 1 if y2 >= 2 else 0
        y1t = "HOT" if y1 else ""
        y2t = "COLD" if y2 else ""
        myLabel9 = Label(newwin, width=5, text=y1t, bg="white")
        myLabel9.place(x=1050,y=170)
        myLabel10 = Label(newwin, width=5, text=y2t, bg="white")
        myLabel10.place(x=1050,y=530)
 
        return y1,y2,z1,z2

    def myHOT():
        x1 = 1
        x2 = 0
        y1,y2,z1,z2 = run(x1,x2)
        new_HNC_win.t_c = 0

        myLabel3 = Label(newwin, width=5, text=x1, bg="white")
        myLabel3.place(x=85,y=170)
        myLabel4 = Label(newwin, width=5, text=x2, bg="white")
        myLabel4.place(x=85,y=530)
        myLabel5 = Label(newwin, width=5, text=z1, bg="white")
        myLabel5.place(x=370,y=250)
        myLabel6 = Label(newwin, width=5, text=z2, bg="white")
        myLabel6.place(x=370,y=450)
        myLabel7 = Label(newwin, width=5, text=y1, bg="white")
        myLabel7.place(x=690,y=170)
        myLabel8 = Label(newwin, width=5, text=y2, bg="white")
        myLabel8.place(x=690,y=530)

    def myCOLD():
  
        x1 = not new_HNC_win.t_c
        x2 = bool(new_HNC_win.t_c)
        new_HNC_win.t_c = new_HNC_win.t_c + 1
        y1, y2,z1,z2 = run(x1,x2)

        myLabel3 = Label(newwin, width=5, text=x1, bg="white")
        myLabel3.place(x=85,y=170)
        myLabel4 = Label(newwin, width=5, text=x2, bg="white")
        myLabel4.place(x=85,y=530)
        myLabel5 = Label(newwin, width=5, text=z1, bg="white")
        myLabel5.place(x=370,y=250)
        myLabel6 = Label(newwin, width=5, text=z2, bg="white")
        myLabel6.place(x=370,y=450)
        myLabel7 = Label(newwin, width=5, text=y1, bg="white")
        myLabel7.place(x=690,y=170)
        myLabel8 = Label(newwin, width=5, text=y2, bg="white")
        myLabel8.place(x=690,y=530)
        

    def myNONE():
        x1=0
        x2=0
        new_HNC_win.t_c = 0
        y1,y2,z1,z2=run(x1,x2)
        myLabel3 = Label(newwin, width=5, text=x1, bg="white")
        myLabel3.place(x=85,y=170)
        myLabel4 = Label(newwin, width=5, text=x2, bg="white")
        myLabel4.place(x=85,y=530)
        myLabel5 = Label(newwin, width=5, text=z1, bg="white")
        myLabel5.place(x=370,y=250)
        myLabel6 = Label(newwin, width=5, text=z2, bg="white")
        myLabel6.place(x=370,y=450)
        myLabel7 = Label(newwin, width=5, text=y1, bg="white")
        myLabel7.place(x=690,y=170)
        myLabel8 = Label(newwin, width=5, text=y2, bg="white")
        myLabel8.place(x=690,y=530)
        myLabel9 = Label(newwin, width=5, text="    ", bg="white")
        myLabel9.place(x=1050,y=170)
        myLabel10 = Label(newwin, width=5, text="    ", bg="white")
        myLabel10.place(x=1050,y=530)
 
    button = Button(newwin, text="HOT", command=myHOT)
    button.place(x=85, y=260)
    button = Button(newwin, text="COLD", command=myCOLD)
    button.place(x=80, y=620)
    button = Button(newwin, text="RESET", command=myNONE)
    button.place(x=80, y=350)
 
 
btn1 = Button(root, text="Hot and Cold", command=new_HNC_win)
btn1.place(x=150, y=300)
 
btn2 = Button(root, text="XOR", command=new_XOR_win)
btn2.place(x=400, y=300)
 
btn3 = Button(root, text="AND", command=new_AND_win)
btn3.place(x=600, y=300)
 
btn4 = Button(root, text="OR", command=new_OR_win)
btn4.place(x=800, y=300)
 
root.mainloop()