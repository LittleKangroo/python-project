from tkinter import *
import math


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.minsize(320, 500)
        self.root.title('计算器')
        frame1(self.root)


class frame1():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.frame1 = Frame(self.master, relief=RAISED, borderwidth=2)
        self.frame1.pack(fill=BOTH, expand=1)
        label = Label(self.frame1, textvariable=shownum, bg='gray', \
                      font=('宋体', 20), anchor='e', bd=5, fg='white')
        label.place(x=20, y=60, width=280, height=50)

        # 第二行
        btn2_1 = Button(self.frame1, text='off', bg='#988', bd=3, command=self.master.quit)
        btn2_1.place(x=10, y=120, width=50, height=50)
        btn2_2 = Button(self.frame1, text='CE', bg='#988', bd=3, command=lambda: gui01())  # CE是清除全部数字，但不影响以前的计算
        btn2_2.place(x=70, y=120, width=50, height=50)
        btn2_3 = Button(self.frame1, text='C', bg='#988', bd=3, command=lambda: gui0())  # C健是重新开始计算，和ESC键是一样的功能
        btn2_3.place(x=130, y=120, width=50, height=50)
        btn2_4 = Button(self.frame1, text='+/-', bg='#988', bd=3, command=lambda: pressnum('+/-'))
        btn2_4.place(x=190, y=120, width=50, height=50)
        btn2_5 = Button(self.frame1, text='√', bg='#988', bd=3, command=lambda: equal('√'))  # --------√开平方
        btn2_5.place(x=250, y=120, width=50, height=50)
        # 第三行
        btn3_1 = Button(self.frame1, text='7', bg='#aaaaaa', bd=3, command=lambda: pressnum('7'))
        btn3_1.place(x=10, y=180, width=50, height=50, )
        btn3_2 = Button(self.frame1, text='8', bg='#aaaaaa', bd=3, command=lambda: pressnum('8'))
        btn3_2.place(x=70, y=180, width=50, height=50)
        btn3_3 = Button(self.frame1, text='9', bg='#aaaaaa', bd=3, command=lambda: pressnum('9'))
        btn3_3.place(x=130, y=180, width=50, height=50)
        btn3_4 = Button(self.frame1, text='/', bg='#708069', command=lambda: presssign('/'))
        btn3_4.place(x=190, y=180, width=50, height=50)
        btn3_5 = Button(self.frame1, text='%', bg='#708069', command=lambda: presssign('%'))
        btn3_5.place(x=250, y=180, width=50, height=50)
        # 第四行
        btn4_1 = Button(self.frame1, text='4', bg='#aaaaaa', bd=3, command=lambda: pressnum('4'))
        btn4_1.place(x=10, y=240, width=50, height=50)
        btn4_2 = Button(self.frame1, text='5', bg='#aaaaaa', bd=3, command=lambda: pressnum('5'))
        btn4_2.place(x=70, y=240, width=50, height=50)
        btn4_3 = Button(self.frame1, text='6', bg='#aaaaaa', bd=3, command=lambda: pressnum('6'))
        btn4_3.place(x=130, y=240, width=50, height=50)
        btn4_4 = Button(self.frame1, text='*', bg='#708069', command=lambda: presssign('*'))
        btn4_4.place(x=190, y=240, width=50, height=50)
        btn4_5 = Button(self.frame1, text='1/x', bg='#708069',
                        command=lambda: equal('1/x'))  # ----------------------------------倒数
        btn4_5.place(x=250, y=240, width=50, height=50)
        # 第五行
        btn5_1 = Button(self.frame1, text='1', bg='#aaaaaa', bd=3, command=lambda: pressnum('1'))
        btn5_1.place(x=10, y=300, width=50, height=50)
        btn5_2 = Button(self.frame1, text='2', bg='#aaaaaa', bd=3, command=lambda: pressnum('2'))
        btn5_2.place(x=70, y=300, width=50, height=50)
        btn5_3 = Button(self.frame1, text='3', bg='#aaaaaa', bd=3, command=lambda: pressnum('3'))
        btn5_3.place(x=130, y=300, width=50, height=50)
        btn5_4 = Button(self.frame1, text='-', bg='#708069', command=lambda: presssign('-'))
        btn5_4.place(x=190, y=300, width=50, height=50)
        btn5_5 = Button(self.frame1, text='=', bg='#708069', command=lambda: equal('='))
        btn5_5.place(x=250, y=300, width=50, height=110)
        # 第六行
        btn6_1 = Button(self.frame1, text='0', bg='#aaaaaa', bd=3, command=lambda: pressnum('0'))
        btn6_1.place(x=10, y=360, width=110, height=50)
        btn6_3 = Button(self.frame1, text='.', bg='#708069', command=lambda: pressnum('.'))
        btn6_3.place(x=130, y=360, width=50, height=50)
        btn6_4 = Button(self.frame1, text='+', bg='#708069', command=lambda: presssign('+'))
        btn6_4.place(x=190, y=360, width=50, height=50)
        btn10 = Button(self.frame1, text='scientific cal', bg='#988', bd=2, command=self.change)
        btn10.place(x=11, y=0, width=90, height=50)

    def change(self, ):
        self.frame1.destroy()
        frame2(self.master)


class frame2():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.frame2 = Frame(self.master, relief=RAISED, borderwidth=2)
        self.frame2.pack(fill=BOTH, expand=1)
        button0 = Button(self.frame2, text='standard cal', bg='#988', bd=2, command=self.back)
        button0.place(x=11, y=0, width=90, height=50)
        label = Label(self.frame2, textvariable=shownum, bg='gray', \
                      font=('宋体', 20), anchor='e', bd=5, fg='white')
        label.place(x=20, y=60, width=280, height=50)
        # 第一行
        btn1 = Button(self.frame2, text='off', bg='#988', bd=2, command=self.master.quit)  # Memory Clear 清除存储器中的数值
        btn1.place(x=10, y=120, width=50, height=50)
        btn2 = Button(self.frame2, text='CE', bg='#988', bd=2, command=lambda: gui01())  # Memory Read 存储器读出
        btn2.place(x=70, y=120, width=50, height=50)
        btn3 = Button(self.frame2, text='C', bg='#988', bd=2, command=lambda: gui0())  # Memory Save 存入存储器
        btn3.place(x=130, y=120, width=50, height=50)
        btn4 = Button(self.frame2, text='+/-', bg='#988', bd=2,
                      command=lambda: pressnum('+/-'))  # Memory Plus 将数值与存储器中的数值相加
        btn4.place(x=190, y=120, width=50, height=50)
        btn5 = Button(self.frame2, text='π', bg='#988', bd=2, command=lambda: pressnum('π'))
        btn5.place(x=250, y=120, width=50, height=50)
        # 第二行
        btn2_1 = Button(self.frame2, text='n!', bg='#988', bd=3, command=lambda: equal('n!'))
        btn2_1.place(x=10, y=180, width=50, height=50)
        btn2_2 = Button(self.frame2, text='ln', bg='#988', bd=3, command=lambda: equal('ln'))  # CE是清除全部数字，但不影响以前的计算
        btn2_2.place(x=70, y=180, width=50, height=50)
        btn2_3 = Button(self.frame2, text='lg', bg='#988', bd=3, command=lambda: equal('lg'))  # C健是重新开始计算，和ESC键是一样的功能
        btn2_3.place(x=130, y=180, width=50, height=50)
        btn2_4 = Button(self.frame2, text='ex', bg='#988', bd=3, command=lambda: equal('ex'))
        btn2_4.place(x=190, y=180, width=50, height=50)
        btn2_5 = Button(self.frame2, text='sin', bg='#988', bd=3, command=lambda: equal('sin'))  # --------√开平方
        btn2_5.place(x=250, y=180, width=50, height=50)
        # 第三行
        btn3_1 = Button(self.frame2, text='7', bg='#aaaaaa', bd=3, command=lambda: pressnum('7'))
        btn3_1.place(x=10, y=240, width=50, height=50, )
        btn3_2 = Button(self.frame2, text='8', bg='#aaaaaa', bd=3, command=lambda: pressnum('8'))
        btn3_2.place(x=70, y=240, width=50, height=50)
        btn3_3 = Button(self.frame2, text='9', bg='#aaaaaa', bd=3, command=lambda: pressnum('9'))
        btn3_3.place(x=130, y=240, width=50, height=50)
        btn3_4 = Button(self.frame2, text='/', bg='#708069', command=lambda: presssign('/'))
        btn3_4.place(x=190, y=240, width=50, height=50)
        btn3_5 = Button(self.frame2, text='cos', bg='#708069', command=lambda: equal('cos'))
        btn3_5.place(x=250, y=240, width=50, height=50)
        # 第四行
        btn4_1 = Button(self.frame2, text='4', bg='#aaaaaa', bd=3, command=lambda: pressnum('4'))
        btn4_1.place(x=10, y=300, width=50, height=50)
        btn4_2 = Button(self.frame2, text='5', bg='#aaaaaa', bd=3, command=lambda: pressnum('5'))
        btn4_2.place(x=70, y=300, width=50, height=50)
        btn4_3 = Button(self.frame2, text='6', bg='#aaaaaa', bd=3, command=lambda: pressnum('6'))
        btn4_3.place(x=130, y=300, width=50, height=50)
        btn4_4 = Button(self.frame2, text='*', bg='#708069', command=lambda: presssign('*'))
        btn4_4.place(x=190, y=300, width=50, height=50)
        btn4_5 = Button(self.frame2, text='tan', bg='#708069',
                        command=lambda: equal('tan'))  # ----------------------------------倒数
        btn4_5.place(x=250, y=300, width=50, height=50)
        # 第五行
        btn5_1 = Button(self.frame2, text='1', bg='#aaaaaa', bd=3, command=lambda: pressnum('1'))
        btn5_1.place(x=10, y=360, width=50, height=50)
        btn5_2 = Button(self.frame2, text='2', bg='#aaaaaa', bd=3, command=lambda: pressnum('2'))
        btn5_2.place(x=70, y=360, width=50, height=50)
        btn5_3 = Button(self.frame2, text='3', bg='#aaaaaa', bd=3, command=lambda: pressnum('3'))
        btn5_3.place(x=130, y=360, width=50, height=50)
        btn5_4 = Button(self.frame2, text='-', bg='#708069', command=lambda: presssign('-'))
        btn5_4.place(x=190, y=360, width=50, height=50)
        btn5_5 = Button(self.frame2, text='=', bg='#708069', command=lambda: equal('='))
        btn5_5.place(x=250, y=360, width=50, height=110)
        # 第六行
        btn6_1 = Button(self.frame2, text='0', bg='#aaaaaa', bd=3, command=lambda: pressnum('0'))
        btn6_1.place(x=10, y=420, width=110, height=50)
        btn6_3 = Button(self.frame2, text='.', bg='#708069', command=lambda: pressnum('.'))
        btn6_3.place(x=130, y=420, width=50, height=50)
        btn6_4 = Button(self.frame2, text='+', bg='#708069', command=lambda: presssign('+'))
        btn6_4.place(x=190, y=420, width=50, height=50)

    def back(self, ):
        self.frame2.destroy()
        frame1(self.master)


# root.minsize(320,500)
# root.maxsize(500,900)
# root.title('计算器')
# frame1=Frame(root,relief=RAISED,borderwidth=2)
# frame1.pack(fill=BOTH,expand=1)

root = Tk()
shownum = StringVar()
shownum.set(0)

numstrlist = []  # -------------------------------存储数字 符号
isjisuan = False  # ------------------------------运算标志


def pressnum(num):  # ---------------------------按下数字
    global isjisuan
    if isjisuan == True:
        shownum.set('0')
        isjisuan = False
    oldnum = shownum.get()
    if oldnum == '0':  # 旧数字是否为0
        if num == 'π':
            shownum.set(math.pi)
        else:
            shownum.set(num)
    else:
        if num == '+/-':
            if oldnum.startswith('-'):
                shownum.set(oldnum[1:])
            else:
                shownum.set('-' + oldnum)
        elif num == 'π':
            a = oldnum * math.pi
            shownum.set(a)
        else:
            shownum.set(oldnum + num)


def presssign(sign):  # ------------------------按下加减符号
    global numsrtlist
    global isjisuan
    oldnum = shownum.get()
    numstrlist.append(oldnum)
    numstrlist.append(sign)
    isjisuan = True
    print(numstrlist)


def equal(sign):
    global numstrlist
    if sign == '=':
        oldnum = shownum.get()
        numstrlist.append(oldnum)
        print(numstrlist)
        resu1 = ''.join(numstrlist)
        result = eval(resu1)
        print(result)
        shownum.set(result)
        numstrlist.clear()
    if sign == '1/x':
        oldnum = shownum.get()
        result = 1 / float(oldnum)
        print(result)
        shownum.set(result)
    if sign == '√':
        oldnum = shownum.get()
        result = math.sqrt(float(oldnum))
        print(result)
        shownum.set(result)
    if sign == 'n!':
        oldnum = shownum.get()
        result = math.factorial(int(oldnum))
        print(result)
        shownum.set(result)
    if sign == 'ln':
        oldnum = shownum.get()
        result = math.log(float(oldnum))
        print(result)
        shownum.set(result)
    if sign == 'lg':
        oldnum = shownum.get()
        result = math.log(float(oldnum), 10)
        print(result)
        shownum.set(result)
    if sign == 'ex':
        oldnum = shownum.get()
        result = math.pow(math.e, float(oldnum))
        print(result)
        shownum.set(result)
    if sign == 'sin':
        oldnum = shownum.get()
        result = math.sin(float(oldnum))
        a = round(result, 4)
        print(result)
        shownum.set(a)
    if sign == 'cos':
        oldnum = shownum.get()
        result = math.cos(float(oldnum))
        print(result)
        a = round(result, 4)
        shownum.set(a)
    if sign == 'tan':
        oldnum = shownum.get()
        result = math.tan(float(oldnum))
        print(result)
        a = round(result, 4)
        shownum.set(a)


def gui0():
    global numstrlist
    global isjisuan
    numstrlist.clear()
    isjisuan = False
    shownum.set(0)


def gui01():
    global numstrlist
    global isjisuan
    isjisuan = False
    shownum.set(0)


basedesk(root)
root.mainloop()
