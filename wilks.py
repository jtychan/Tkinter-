from tkinter import *

root = Tk()
root.title("Wilks Calculator")

total = Entry(root, width=30, borderwidth=10)
labelText=StringVar()
labelText.set("Enter your total ")
labelDir = Label(root, textvariable=labelText, height=1)
labelDir.pack(side="left")
total_ans = total.get()
total.pack()

button_quit = Button(root, text= "Exit Program", command=root.quit)

weight = Entry(root, width=30, borderwidth=10)
labelText=StringVar()
labelText.set("weight ")
labelDir = Label(root, textvariable=labelText, height=4)
labelDir.pack(side="left")
weight_ans = weight.get()
weight.pack()




genderz = Entry(root, width=30, borderwidth=10)
labelText = StringVar()
labelText.set("are you male or female?  ")
labelDir = Label(root, textvariable=labelText, height=4)
labelDir.pack(side="left")
genderz.pack()









def myclick():
    if gender.get() == "male":
        a = -216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 7.01863E-06
        f = -1.291E-08

    else:
        a = 594.31747775582
        b = -27.23842536447
        c = 0.82112226871
        d = -0.00930733913
        e = 4.731582E-05
        f = -9.054E-08

    answer = (total.get() * 500 / (a + b * weight.get() + c * weight.get() ** 2 + d * weight.get() ** 3
                                   + e * weight.get() ** 4 + f * weight.get() ** 5))

    wilks = "Wilks: " + answer
    mywilks = Label(root, text=wilks)
    mywilks.pack()



myButton = Button(root, text="Calculate ", command=myclick)
myButton.pack()

root.mainloop()
