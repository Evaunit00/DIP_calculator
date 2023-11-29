import tkinter as tk
class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1080x480")
        self.root.title("Calculator Pro X +++")

        self.label = tk.Label(self.root, text="Calculator Pro X +++", font=('Comic Sans MS', 69))
        self.label.pack()
        self.button = tk.Button(self.root, text="Download Here", font=('Comic Sans MS', 10))
        self.button.place(x=500, y=150)


        
        self.root.mainloop()

MyCalculator()