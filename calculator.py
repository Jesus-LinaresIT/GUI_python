from tkinter import *

main = Tk()
main.title("Calculator")
main.iconbitmap("calculator.ico")

myFrame = Frame(main)
myFrame.pack()


#------------------------Screen-------------------------------

screen = Entry(myFrame)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="gray", fg="#03f943", justify="right")



main.mainloop()