from tkinter import *

main = Tk()
main.title("Calculator")
main.iconbitmap("calculator.ico")

myFrame = Frame(main)
myFrame.pack()


#------------------------Screen-------------------------------

screenNumber = StringVar()

screen = Entry(myFrame, textvariable=screenNumber)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="gray", fg="#130FFA", justify="right")

#------------------------keystrokes---------------------------

def strokesNumber(num):
    screenNumber.set(screenNumber.get() + num)

#------------------------row 1------------------------------

button7 = Button(myFrame, text="7", width=3, command=lambda:strokesNumber("7"))
button7.grid(row=2, column=1)
button8 = Button(myFrame, text="8", width=3, command=lambda:strokesNumber("8"))
button8.grid(row=2, column=2)
button9 = Button(myFrame, text="9", width=3, command=lambda:strokesNumber("9"))
button9.grid(row=2, column=3)
buttonDiv = Button(myFrame, text="/", width=3)
buttonDiv.grid(row=2, column=4)

#------------------------row 2------------------------------

button4 = Button(myFrame, text="4", width=3, command=lambda:strokesNumber("4"))
button4.grid(row=3, column=1)
button5 = Button(myFrame, text="5", width=3, command=lambda:strokesNumber("5"))
button5.grid(row=3, column=2)
button6 = Button(myFrame, text="6", width=3, command=lambda:strokesNumber("6"))
button6.grid(row=3, column=3)
buttonMulti = Button(myFrame, text="x", width=3)
buttonMulti.grid(row=3, column=4)

#------------------------row 3------------------------------

button1 = Button(myFrame, text="1", width=3, command=lambda:strokesNumber("1"))
button1.grid(row=4, column=1)
button2 = Button(myFrame, text="2", width=3, command=lambda:strokesNumber("2"))
button2.grid(row=4, column=2)
button3 = Button(myFrame, text="3", width=3, command=lambda:strokesNumber("3"))
button3.grid(row=4, column=3)
buttonRest= Button(myFrame, text="-", width=3)
buttonRest.grid(row=4, column=4)

#------------------------row 4------------------------------

buttonPoint = Button(myFrame, text=".", width=3, command=lambda:strokesNumber("."))
buttonPoint.grid(row=5, column=1)
button0 = Button(myFrame, text="0", width=3, command=strokesNumber("0"))
button0.grid(row=5, column=2)
buttonEqual= Button(myFrame, text="=", width=3)
buttonEqual.grid(row=5, column=3)
buttonMore = Button(myFrame, text="+", width=3)
buttonMore.grid(row=5, column=4)



main.mainloop()