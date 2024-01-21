'''
Created by Ishan Pathak
https://github.com/Ishan1923
'''

from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np

class cal_window(Tk):

    characters = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'sin', 11 : 'cos', 12: 'tan', 13: 'asin', 14:'acos', 15:'atan', 16:'=', 17:'+', 18:'-', 19:'\u00d7',
              20: '\u00f7', 21:'c', 22:'e', 23:'\u03c0', 24: 'graph', 25: '(', 26: ')'}
    
    pie = 3.1426
    e = 2.7168

    def __init__(self, geo_x, geo_y) -> None:
        super().__init__()
        self.geo_x = geo_x
        self.geo_y = geo_y
        self.geometry(f"{self.geo_x}x{self.geo_y}")
        self.resizable(0,0)
        self.title("Calculator-Basic")

        self.screenframe = Frame(self, padx=2, pady=0)
        self.buttonframe = Frame(self)
        self.statusframe = Frame(self)
        self.screenframe.pack(side=TOP, fill=X)
        self.buttonframe.pack(side=TOP, fill=X)
        self.statusframe.pack(side=BOTTOM, fill=X)

        self.output = StringVar()
        self.output.set(0)
        self.outputtexttrigo = 0

        self.trigo = False

        self.statusVar = StringVar()
        self.statusVar.set("Ready")

    def create_graph(self, key):
        print(key)
        graph1 = GraphGUI()
        graph1.content()
        graph1.mainloop()
    
    def calculate(self):
        text = self.output.get()
        answer = eval(text)
        self.output.set(answer)
        return answer

    def updatescreen(self, key):
        text = self.output.get()
        if text == '0':
            if key in [1,2,3,4,5,6,7,8,9,0,22,23]:
                text = cal_window.characters[key]
                self.output.set(text)
            else: 
                pass
        else:
            text += cal_window.characters[key]
            self.output.set(text)
        
    def updatescreen_trigo(self, key):
        print(key)
        text = self.output.get()
        var = text
        text = cal_window.characters[key] + '(' + text + ')'
        self.output.set(text)

        if key in [10,11,12,13,14,15]:

            self.trigo = True

            if key == 10:
                ans = math.sin(float(var))
                self.outputtexttrigo = ans

            if key == 11:
                ans = math.cos(float(var))
                self.outputtexttrigo = ans

            if key == 12:
                ans = math.tan(float(var))
                self.outputtexttrigo = ans

            if key == 13:
                if float(var) < 1:
                    ans = math.asin(float(var))
                    self.outputtexttrigo = ans
                else:
                    self.output.set("ERROR")
                    print("ERROR")

            if key == 14:
                if float(var) < 1:
                    ans = math.acos(float(var))
                    self.outputtexttrigo = ans
                else:
                    self.output.set("ERROR")
                    print("ERROR")

            if key == 15:
                    ans = math.atan(float(var))
                    self.outputtexttrigo = ans
        
        else:
            self.trigo = False
    
    def equal(self):
        print(16)
        if self.trigo == True:
            text = self.outputtexttrigo
            self.output.set(text)
            print(text)
        else:
            text = self.output.get()
            text = text.replace("\u00d7", "*").replace("\u00f7", "/").replace("\u03c0", str(cal_window.pie)).replace("e", str(cal_window.e))
            ans = eval(text)
            self.output.set(ans)
            print(ans)
        
        self.trigo = False
    
    def clearscreen(self, key):
        print(key)
        text = self.output.get()
        if text != "0":
            self.output.set(0)
            print("screen cleared!")

    def create_button_num(self, key, texttobeshown, x, y):
        Button(self.buttonframe, text=texttobeshown, command=lambda m = key: cal_window.updatescreen(self,m)
               ,font=("Consolas", 16, "bold"), padx=10, pady=10).grid(row=x, column=y)
        return key
        
    
    def create_button_equal(self, key, texttobeshown, x, y):
        print(key)
        Button(self.buttonframe, text=texttobeshown, command=self.equal
               ,font=("Consolas", 16, "bold"), padx=10, pady=10).grid(row=x, column=y)
        return key

    def create_button_trigo(self, key, texttobeshown, x, y):
        Button(self.buttonframe, text=texttobeshown, command=lambda m = key: cal_window.updatescreen_trigo(self, m)
               ,font=("Consolas", 16, "bold"), padx=10, pady=10).grid(row=x, column=y)
        return key

    def create_button_clear(self, key, texttobeshown, x, y):
        print(key)
        Button(self.buttonframe, text=texttobeshown, command = lambda m = key: cal_window.clearscreen(self, m)
               ,font=("Consolas", 16, "bold"), padx=10, pady=10).grid(row=x, column=y)
        return key
    
    def graph_button(self,key, texttobeshown, x, y):
        print(key)
        Button(self.buttonframe, text = texttobeshown
               ,font=("Consolas", 16, "bold"), padx=10, pady=10, command=lambda m = "graph": cal_window.create_graph(self,m)).grid(row=x, column=y)
        return key

    def create_screen(self, bg_user, text_font_tuple, relief_user, fg_user):
        self.screen = Label(self.screenframe, textvariable = self.output, bg = bg_user, font=text_font_tuple, relief=relief_user, fg=fg_user
                            ,padx=10, pady=10)
        self.screen.pack(side=TOP, fill=X)
    
    def create_status_bar(self):
        Label(self.statusframe, textvariable=self.statusVar, font=("Century Gothic", 11,"bold"), bg="white", fg='black', 
              anchor=W).pack(fill=X)
        Label(self.statusframe, text="Ishpatk Develec", font=("Century Schoolbook", 11, "bold"), bg ="white", fg = "grey", 
             anchor=E).pack()

class GraphGUI(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph")
        self.geometry("643x634")
        self.minsize(643, 634)

        self.frame = Frame(self)
        self.frame.pack(pady=10)

        self.framefunctions = Frame(self)
        self.framefunctions.pack(pady=10, side=TOP)


        self.eq = StringVar()
        self.eq.set("write equation")

    
    def getVal(self):
        text = self.eq.get()
        if text == "write equation": 
            pass
        else: 
            print(text)
            return text
    
    def content(self):

        Label(text="Bekar ka Graph", font=("Press Start 2P", 24), pady=40, fg="#18854c").pack(side=TOP)

        eqlabel = Entry(self.frame, textvariable=self.eq, font=("Roboto",20), border=0)
        enterbutton = Button(self.frame, text="Enter", font=("Gill Sans",13, "bold"), command = lambda : GraphGUI.getVal(self), border=0.5, relief=RAISED,
                             padx=10, pady=10, bg="white")
        
        sinbutton = Button(self.framefunctions, text='sin', font = ("Gill Sans", 20,"bold"), border=0.5, command= lambda m = 0: GraphGUI.draw(self, m), bg="white")
        sinbutton.grid(row=1, column=1)
        cosbutton = Button(self.framefunctions, text='cos', font = ("Gill Sans", 20,"bold"), border=0.5, command= lambda m = 1: GraphGUI.draw(self, m),bg="white")
        cosbutton.grid(row=1, column=2)
        tanbutton = Button(self.framefunctions, text='tan', font = ("Gill Sans", 20,"bold"), border=0.5, command= lambda m = 2: GraphGUI.draw(self, m),bg="white")
        tanbutton.grid(row=1, column=3)
        logbutton = Button(self.framefunctions, text='ln', font = ("Gill Sans", 20,"bold"), border=0.5, command= lambda m = 3: GraphGUI.draw(self, m),bg="white")
        logbutton.grid(row=1, column=4)

        eqlabel.grid(row=0, column=0)
        enterbutton.grid(row=1, column=0)

        enterbutton.bind("<Leave>", lambda event: enterbutton.config(bg="white", fg="black"))
        enterbutton.bind("<Enter>", lambda event: enterbutton.config(bg="#33cc4f", fg="white"))

        sinbutton.bind("<Leave>", lambda event: sinbutton.config(bg="white", fg="black"))
        sinbutton.bind("<Enter>", lambda event: sinbutton.config(bg="#6f827c", fg="white"))

        cosbutton.bind("<Leave>", lambda event: cosbutton.config(bg="white", fg="black"))
        cosbutton.bind("<Enter>", lambda event: cosbutton.config(bg="#6f827c", fg="white"))

        tanbutton.bind("<Leave>", lambda event: tanbutton.config(bg="white", fg="black"))
        tanbutton.bind("<Enter>", lambda event: tanbutton.config(bg="#6f827c", fg="white"))

        logbutton.bind("<Leave>", lambda event: logbutton.config(bg="white", fg="black"))
        logbutton.bind("<Enter>", lambda event: logbutton.config(bg="#6f827c", fg="white"))

        eqlabel.bind("<Enter>", lambda event: eqlabel.config(cursor="plus"))
        eqlabel.bind("<Leave>", lambda event: eqlabel.config(cursor="arrow"))
    
    def draw(self, key):
        x = np.arange(0., 10, 0.1)
        if key == 0:
            a = np.sin(x)
            plt.plot(x, a, 'b')
            plt.show()
        if key == 1:
            a = np.cos(x)
            plt.plot(x, a, 'r')
            plt.show()
        if key == 2:
            a = np.tan(x)
            plt.plot(x, a, 'black')
            plt.show()
        if key == 3:
            a = np.log(x)
            plt.plot(x, a, '#18854c')
            plt.show()



####   Driver Code   #####


cal = cal_window(444, 368)# width x height

cal.create_screen("#27752b", ("Handjet", 26), SUNKEN, "white")

button1 = cal.create_button_num(1, "1", 1 ,1)
button2 = cal.create_button_num(2, "2", 1 ,2)
button3 = cal.create_button_num(3, "3", 1 ,3)
button4 = cal.create_button_num(4, "4", 2 ,1)
button5 = cal.create_button_num(5, "5", 2 ,2)
button6 = cal.create_button_num(6, "6", 2 ,3)
button7 = cal.create_button_num(7, "7", 3 ,1)
button8 = cal.create_button_num(8, "8", 3 ,2)
button9 = cal.create_button_num(9, "9", 3 ,3)
button0 = cal.create_button_num(0, "0", 4 ,2)

buttonsin = cal.create_button_trigo(10, " sin ", 1 ,7)
buttoncos = cal.create_button_trigo(11, " cos ", 2 ,7)
buttontan = cal.create_button_trigo(12, " tan ", 3 ,7)
buttonasin = cal.create_button_trigo(13, " asin ", 1 ,8)
buttonacos = cal.create_button_trigo(14, " acos ", 2 ,8)
buttonatan = cal.create_button_trigo(15, " atan ", 3 ,8)

button_equalto = cal.create_button_equal(16, "=", 1 ,5)
button_plus = cal.create_button_num(17, "+", 2 ,5)
button_minus = cal.create_button_num(18, "-", 3 ,5)
button_multiplication = cal.create_button_num(19, "\u00d7", 4 ,6)#multiplication
button_division = cal.create_button_num(20, "\u00f7", 4 ,5)#division

button_clear = cal.create_button_clear(21, "c", 1 ,6)

button_euler = cal.create_button_num(22, "e", 2 ,6)#euler's constant
button_pie = cal.create_button_num(23, "\u03c0", 3 ,6)#pie

button_graph = cal.graph_button(24, "graph", 4 ,7)

buttonleftparanthesis = cal.create_button_num(25, '(', 4, 1)
buttonrightparanthesis = cal.create_button_num(26, ')', 4, 3)

cal.create_status_bar()

cal.mainloop()
