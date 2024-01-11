import tkinter as tk
from tkinter import*

root=Tk()
root.geometry("275x445")
root.title("CALCULATOR")
rootlabel = Label(root,text="CALCULATOR",bg='White',font=("Tiroots",30,'bold'))
rootlabel.pack(side=TOP)
root.config(background='Dark gray')

textin = StringVar()
operator = ""

'''
Functions
'''
def equalbut():
    global operator
    temp_op = str(eval(operator))
    operator = temp_op
    textin.set(temp_op)

def percentbut():
    global operator
    temp = str(eval(operator+'/100'))
    textin.set(temp)


'''
Display and  Buttons
'''

text_display = Entry(root, font=('sans-serif', 20, 'bold'), textvariable=textin,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right')
text_display.pack()

but1=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=310)

but2=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=75,y=310)

but3=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=140,y=310)

but4=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=10,y=240)

but5=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=240)

but6=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=140,y=240)

but7=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=10,y=170)

but8=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=75,y=170)

but9=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=170)

but0=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=75,y=380)

butdot=Button(root,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=10,y=380)

butequal=Button(root,padx=47,pady=14,bd=4,bg='#00BFFF',command=equalbut,text="=",font=("Courier New",16,'bold'),fg='white')
butequal.place(x=140,y=380)

butclearall=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="C",command=clearallbut,font=("Courier New",16,'bold'))
butclearall.place(x=10,y=100)

butdel=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="D",command=clearbut,font=("Courier New",16,'bold'))
butdel.place(x=75,y=100)

butpercent=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="%",command=percentbut,font=("Courier New",16,'bold'))
butpercent.place(x=140,y=100)

butpl=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(root,padx=14,pady=14,bd=4,bg='white',fg='#FF8C00',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)


root.mainloop()