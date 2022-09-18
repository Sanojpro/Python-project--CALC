from tkinter import*

main=Tk()
e=""
magicbox= StringVar()
magicbox.set("Hello")
label=Label(main,textvariable=magicbox)
label.grid(columnspan=4)

def labelupdate(num):
    global e
    e=e+str(num)
    magicbox.set(e)

def equal():
    global e
    total= str(eval(e))
    magicbox.set(total)
    e=""

def clear():
    global e
    magicbox.set("")
    e=""

button0=Button(main,text="0",command=lambda:labelupdate(0))
button0.grid(row=1,column=0)
button1=Button(main,text="1",command=lambda:labelupdate(1))
button1.grid(row=1,column=1)
button2=Button(main,text="2",command=lambda:labelupdate(2))
button2.grid(row=1,column=2)
button3=Button(main,text="3",command=lambda:labelupdate(3))
button3.grid(row=2,column=0)
buttonx=Button(main,text="x",command=lambda:labelupdate("*"))
buttonx.grid(row=1,column=3)
buttonsub=Button(main,text="-",command=lambda:labelupdate("-"))
buttonsub.grid(row=2,column=3)
buttondiv=Button(main,text="/",command=lambda:labelupdate("/"))
buttondiv.grid(row=3,column=3)
buttonsum=Button(main,text="+",command=lambda:labelupdate("+"))
buttonsum.grid(row=4,column=3)
buttonmod=Button(main,text="%",command=lambda:labelupdate("%"))
buttonmod.grid(row=4,column=2)
buttoneq=Button(main,text="=",command=equal)
buttoneq.grid(row=4,column=1)
button4=Button(main,text="4",command=lambda:labelupdate(4))
button4.grid(row=2,column=1)
button5=Button(main,text="5",command=lambda:labelupdate(5))
button5.grid(row=2,column=2)
button6=Button(main,text="6",command=lambda:labelupdate(6))
button6.grid(row=3,column=0)
button7=Button(main,text="7",command=lambda:labelupdate(7))
button7.grid(row=3,column=1)
button8=Button(main,text="8",command=lambda:labelupdate(8))
button8.grid(row=3,column=2)
buttonclear=Button(main,text="AC",command=clear)
buttonclear.grid(row=4,column=0)

main.mainloop()
