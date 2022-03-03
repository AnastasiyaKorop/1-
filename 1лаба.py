# 9 + 3 - 10 * 13 + 7
# 2 + 3 * 5 / 2 - 10 / 3, p=23
from tkinter import *

pr = [2]
n = 1000
for i in range(3, n+1, 2):
    k = 0
    q = int(i ** 0.5) + 2
    for j in pr:
        if j > q:
            break
        if i % j == 0:
            k = 1
            break
    if k == 0:
        pr.append(i)
def clicked():
    def stepen(a, p):
        avm = 1.1
        b = 1
        while not avm.is_integer():
            avm = (1 + p * b) / a
            b += 1
        return avm
    def kalk(x):
        while "^" in x:
            for i in range(len(x)):
                if x[i] == "^":
                    x[i] = (x[i - 1] ** x[i + 1]) % p
                    del x[i - 1]
                    del x[i]
                    break
        while "*" in x or "/" in x:
            for i in range(len(x)):
                if x[i] == "*":
                    x[i] = (x[i - 1] * x[i + 1]) % p
                    del x[i - 1]
                    del x[i]
                    break
                elif x[i] == "/":
                    x[i] = stepen(x[i + 1], p)
                    del x[i - 1]
                    del x[i]
                    break
        while "+" in x or "-" in x:
            for i in range(len(x)):
                if x[i] == "+":
                    x[i] = (x[i - 1] + x[i + 1]) % p
                    del x[i - 1]
                    del x[i]
                    break
                elif x[i] == "-":
                    x[i] = (x[i - 1] - x[i + 1]) % p
                    del x[i - 1]
                    del x[i]
                    break
        return x
    vir = txt1.get()
    if vir == "":
        lblo1 = Label(window, text="Выражение не введено", fg="red", bg="pink", font=("Times New Roman", 9))
        lblo1.grid(column=2, row=2)
        lbl3.configure(text="")
    p = 0
    lblo = Label(window, text="", fg="red", bg="pink", font=("Times New Roman", 9))
    lblo.grid(column=1, row=2)
    if txt2.get() == "":
        lblo = Label(window, text="Поле не введено", fg="red", bg="pink", font=("Times New Roman", 9))
        lblo.grid(column=2, row=6)
        lbl3.configure(text="")
    elif not(int(txt2.get()) in pr):
        lblo = Label(window, text="Введено не простое число", fg="red", bg="pink", font=("Times New Roman", 9))
        lblo.grid(column=2, row=6)
        lbl3.configure(text = "")
    else:
        p = txt2.get()
        p = int(p)
    if  vir != "" and (p in pr) and txt2.get() != "":
        lblo = Label(window, text="                       \n                       ", fg="red", bg="pink", font=("Times New Roman", 9))
        lblo.grid(column=1, row=2)
        lblo1 = Label(window, text="                                      ", fg="red", bg="pink", font=("Times New Roman", 9))
        lblo1.grid(column=0, row=2)
        vir = vir.split()
        for i in range(len(vir)):
            if vir[i].isalnum() or (vir[i][0] == "-" and len(vir[i]) > 1):
                vir[i] = int(vir[i])
            nul = 0
            for i in range(len(vir)):
                if vir[i] == "/":
                    if vir[i + 1] == 0:
                        lblo1 = Label(window, text="Деление на нуль", fg="red", bg="pink", font=("Times New Roman", 9))
                        lblo1.grid(column=0, row=2)
                        lbl3.configure(text = "")
                        nul = 1
        if nul == 0:
            while "(" in vir or ")" in vir:
                sk = []
                z1 = 0
                for i in range(len(vir)):
                    if vir[i] == ")":
                        u += 1
                        break
                    elif vir[i] == "(":
                        sk = []
                        u = 1
                        z1 = 1
                    elif z1 == 1:
                        sk.append(vir[i])
                        u += 1
                k = i - u + 1
                sk = kalk(sk)
                sk = sk[0]
                vir[k] = sk
                for i in range(u - 1):
                    del vir[k + 1]
                #print(vir, ", выполнил скобки")
            kalk(vir)
            v = vir[0]
            lbl3.configure(text = v)

window = Tk()
window.title("Калькулятор полей")
window.geometry('385x300')
window["bg"] = "pink"

lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=0)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=1)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=2)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=3)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=4)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=5)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=6)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=7)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=8)
lbl5 = Label(window, text="           ", bg="pink", fg="red", font=("Gulim", 7))
lbl5.grid(column=1, row=9)



lbl1 = Label(window, text="Введите выражение", bg="pink", font=("Times New Roman", 14))
lbl1.grid(column=2, row=0)
lbl1 = Label(window, text="Введите поле", bg="pink", font=("Times New Roman", 14))
lbl1.grid(column=2, row=3)
txt1 = Entry(window,width=50)
txt1.grid(column=2, row=1)
txt2 = Entry(window,width=12)
txt2.grid(column=2, row=4)
btn = Button(window, text="Решить", command=clicked)
btn.grid(column=2, row=7)
lbl2 = Label(window, text="Результат:", bg="pink", font=("Times New Roman", 14))
lbl2.grid(column=2, row=8)
lbl3 = Label(window, text="", bg="pink", font=("Times New Roman", 14))
lbl3.grid(column=2, row=9)
lbl4 = Label(window, text="Поле должно быть простым числом.", bg="pink", font=("Times New Roman", 9))
lbl4.grid(column=2, row=5)

window.mainloop()