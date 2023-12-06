import tkinter as tk
class MyCalculator:
    
    title="Calculator Pro X +++"
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("470x650")
        #self.root.resizable(0, 0)
        self.root.option_add("*Font", "ComicSansMS 25")
        self.root.title(self.title)

        self.label_text =tk.StringVar()
        self.label = tk.Label(self.root, text="Calculator Pro X +++", font=('Comic Sans MS', 30))
        self.label.grid(row=0, column=0, columnspan=4, sticky="NEWS", padx=20, pady=(20, 10), ipadx=20, ipady=10)
        self.label = tk.Label(self.root, textvariable=self.label_text, font=('Comic Sans MS', 30),bg="yellow")
        self.label.grid(row=1, columnspan=4, padx=20, pady=(0, 10), ipadx=20, ipady=10)
        
        self.buttonCE = tk.Button(self.root, text="CE", width=3, height=1)
        self.buttonCE.grid(row=2, column=0)
        self.buttonCE.bind("<Button-1>", self.CE)

        self.buttonParen = tk.Button(self.root, text="()", width=3, height=1)
        self.buttonParen.grid(row=2, column=1)
        self.buttonParen.bind("<Button-1>", self.Paren)
        
        self.buttonPerc = tk.Button(self.root, text="%", width=3, height=1)
        self.buttonPerc.grid(row=2, column=2)
        self.buttonPerc.bind("<Button-1>", self.Perc)

        self.buttondivide = tk.Button(self.root, text="/", width=3, height=1)
        self.buttondivide.grid(row=2, column=3)
        self.buttondivide.bind("<Button-1>", self.divide)

        self.buttonmultiply = tk.Button(self.root, text="x", width=3, height=1)
        self.buttonmultiply.grid(row=3, column=3)
        self.buttonmultiply.bind("<Button-1>", self.multiply)
        
        self.buttonsubtract = tk.Button(self.root, text="-", width=3, height=1)
        self.buttonsubtract.grid(row=4, column=3)
        self.buttonsubtract.bind("<Button-1>", self.subtract)

        self.buttonadd = tk.Button(self.root, text="+", width=3, height=1)
        self.buttonadd.grid(row=5, column=3)
        self.buttonadd.bind("<Button-1>", self.add)

        self.button7 = tk.Button(self.root, text="7", width=3, height=1)
        self.button7.grid(row=3, column=0)
        self.button7.bind("<Button-1>", self.seven)

        self.button8 = tk.Button(self.root, text="8", width=3, height=1)
        self.button8.grid(row=3, column=1)
        self.button8.bind("<Button-1>", self.eight)
        
        self.button9 = tk.Button(self.root, text="9", width=3, height=1)
        self.button9.grid(row=3, column=2)
        self.button9.bind("<Button-1>", self.nine)

        self.button4 = tk.Button(self.root, text="4", width=3, height=1)
        self.button4.grid(row=4, column=0)
        self.button4.bind("<Button-1>", self.four)

        self.button5 = tk.Button(self.root, text="5", width=3, height=1)
        self.button5.grid(row=4, column=1)
        self.button5.bind("<Button-1>", self.five)

        self.button6 = tk.Button(self.root, text="6", width=3, height=1)
        self.button6.grid(row=4, column=2)
        self.button6.bind("<Button-1>", self.six)

        self.button1 = tk.Button(self.root, text="1", width=3, height=1)
        self.button1.grid(row=5, column=0)
        self.button1.bind("<Button-1>", self.one)

        self.button2 = tk.Button(self.root, text="2", width=3, height=1)
        self.button2.grid(row=5, column=1)
        self.button2.bind("<Button-1>", self.two)

        self.button3 = tk.Button(self.root, text="3", width=3, height=1)
        self.button3.grid(row=5, column=2)
        self.button3.bind("<Button-1>", self.three)

        self.buttonposinega = tk.Button(self.root, text="+/-", width=3, height=1)
        self.buttonposinega.grid(row=6, column=0)
        self.buttonposinega.bind("<Button-1>", self.posinega)

        self.button0 = tk.Button(self.root, text="0", width=3, height=1)
        self.button0.grid(row=6, column=1)
        self.button0.bind("<Button-1>", self.zero)

        self.buttondot = tk.Button(self.root, text=".", width=3, height=1)
        self.buttondot.grid(row=6, column=2)
        self.buttondot.bind("<Button-1>", self.dot)

        self.buttonequal = tk.Button(self.root, text="=", width=3, height=1)
        self.buttonequal.grid(row=6, column=3)
        self.buttonequal.bind("<Button-1>", self.equal)


        self.root.mainloop()
    def CE(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("")
        self.label.grid(row=1, colum=0)

    def Paren(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("()")
        self.label.grid(row=1, colum=0)

    def Perc(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("%")
        self.label.grid(row=1, colum=0)

    def divide(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("/")
        self.label.grid(row=1, colum=0)

    def multiply(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("x")
        self.label.grid(row=1, colum=0)
    
    def subtract(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("-")
        self.label.grid(row=1, colum=0)

    def add(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("+")
        self.label.grid(row=1, colum=0)

    def seven(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("7")
        self.label.grid(row=1, colum=0)

    def eight(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("8")
        self.label.grid(row=1, colum=0)
        
    def nine(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("9")
        self.label.grid(row=1, colum=0)

    def four(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("4")
        self.label.grid(row=1, colum=0)

    def five(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("5")
        self.label.grid(row=1, colum=0)

    def six(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("6")
        self.label.grid(row=1, colum=0)
        
    def one(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("1")
        self.label.grid(row=1, colum=0)

    def two(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("2")
        self.label.grid(row=1, colum=0)

    def three(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("3")
        self.label.grid(row=1, colum=0)

    def posinega(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("+/-")
        self.label.grid(row=1, colum=0)

    def zero(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("0")
        self.label.grid(row=1, colum=0)

    def dot(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set(".")
        self.label.grid(row=1, colum=0)

    def equal(self, event):
        print(event)
        self.title = "My Calculator"
        self.root.title(self.title)
        self.label_text.set("=")
        self.label.grid(row=1, colum=0)
        
MyCalculator()