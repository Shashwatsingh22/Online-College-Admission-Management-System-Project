from tkinter import *
import tkinter.font as font

root=Tk()
root.title("Login Page")
root.geometry("840x350")
#-----------------Functions---------------------------------

#-------------------------------Heading---------------------
f1=Frame(relief=SUNKEN,bg = "black", borderwidth =4 )
Label(f1,text="Welcome To Rajputana University",bg = "Black", fg = "white",font="lucida 24 bold").pack()
f1.pack(fill="x")

#-------------------------Body----------------------------
fbmain=Frame(relief=SUNKEN,borderwidth=4,bg="orange",width=900)
Label(fbmain,text = "Student Credentials",bg = "orange",font = "Arial 18 bold",fg="white", padx = 20,pady = 10,borderwidth=4).pack()

f_1=Frame(fbmain,borderwidth=8,bg="orange")
Label(f_1,text="Username",font="comicsansms 12 bold",bg="orange",fg="white").pack(pady=5,side="left")
user=StringVar()
userEnt=Entry(f_1,textvariable=user,bg="#ffe05d",fg="white",font="Arial 12 bold").pack(ipady=5,ipadx=5,padx=10,pady=10)
f_1.pack(anchor="w")

f_2=Frame(fbmain,borderwidth=8,bg="orange")
Label(f_2,text="Password",font="comicsansms 12 bold",bg="orange",fg="white").pack(pady=5,side="left")
passwrd=StringVar()
pass_=Entry(f_2,textvariable=passwrd,bg="#ffe05d",fg="white",font="Arial 12 bold").pack(ipady=5,ipadx=5,padx=10,pady=10)
f_2.pack(anchor="w")


Button(fbmain,text = "Connect", cursor = "hand2", bg = "#0074D9",fg= "white", relief = SUNKEN,font="Arial 12 bold").pack()

fbmain.pack(anchor="w",padx=250,pady=20,fill="x")


root.mainloop()