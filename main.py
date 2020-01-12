from tkinter import *
import csv
import random

home = None

e1_val = None
tries = 0
NumList = []
SymList = []
elNo = 0
elSym = ''

def SubmitFunc():
    global e1_val
    ans = e1_val.get()
    global elSym
    global SymList
    i = 0
    for el in SymList:
        if ans.lower() == el.lower():
            i = i + 1

    if i == 0:
        win = Tk()
        win.title("Result")
        l = Label(win, text = "Element name does not exist...")
        l.pack()
        win.mainloop()

    elif elSym.lower() == ans.lower():
        win = Tk()
        win.title('Result')
        l = Label(win,text = "You are right!!")
        l.grid(row = 0,column =0)
        global home
        home.destroy()
        start()
        win.mainloop()
    else:
        win = Tk()
        win.title('Result')
        global tries
        tries = tries + 1
        ans = ans.capitalize()
        indexOfAns = SymList.index(ans)
        indexOfSym = SymList.index(elSym)

        if tries == 5:
            t = "Game Over!"
            home.destroy()
        elif indexOfAns > indexOfSym:
            t = "Not quite... The element is on the left side of the entered element."
        else:
            t = "Not quite... The element is on the right side of the entered element."

        l = Label(win,text = t)
        l.grid(row = 0,column =0)
        win.mainloop()

def ShowFunc():
    win = Tk()
    win.title("Answer")
    global elNo
    global elSym
    t = "The symbol for element no. "+str(elNo)+" is "+elSym
    label = Label(win, text = t)
    label.pack()
    win.mainloop()

def NewFunc():
    global home
    home.destroy()
    start()

def start():
    global home
    home = Tk()
    home.title("Periodic Table Game")
    with open('elementlist.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        for row in reader:
            global NumList
            global SymList
            NumList.append(int(row[0]))
            SymList.append(row[1])

    global elNo
    global elSym
    elNo = random.choice(NumList)
    elSym = SymList[elNo-1]

    l1 = Label(home,text = elNo)
    l1.grid(row = 0,column = 0,columnspan = 2)
    l1.config(font = ('Courier','125'))

    global e1_val
    e1_val = StringVar(home)
    e1 = Entry(home, textvariable = e1_val)
    e1.grid(column = 0,row = 1,columnspan = 2)

    b1 = Button(home, text = "Submit", command = SubmitFunc)
    b1.grid(column = 0,row = 2)

    b2 = Button(home, text = "Show", command = ShowFunc)
    b2.grid(column = 1,row = 2)

    b3 = Button(home, text = "Quit", command = home.destroy)
    b3.grid(column = 0,row = 3)

    b4 = Button(home, text = "New", command = NewFunc)
    b4.grid(column = 1,row = 3)

    home.mainloop()
start()
