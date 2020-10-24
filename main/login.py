from tkinter import *
import tkinter.font as font


#-------------------------------------Root-----------------
root=Tk()
root.title("Login Page")
root.geometry("850x400")
#--------------------SomeWidgets & Functions----------


fon=font.Font(size=14,weight="bold")


#-------------------------------Heading---------------------
f1=Frame(relief=SUNKEN,bg = "black", borderwidth =4 )
Label(f1,text="Welcome To Rajputana University",bg = "Black", fg = "white",font="lucida 24 bold").pack()
f1.pack(fill="x")

#-------------------------Body-------------------------
fbmain=Frame(relief=SUNKEN,bg="#ffe05d")

Label(fbmain,text = "LoginAs",bg ="#ffe05d",fg="white",font = "Arial 18 bold", padx = 20,pady = 10,borderwidth=4).pack()

f_1=Frame(fbmain,borderwidth=8,bg="#ffe05d")
Label(f_1,text="Admin",font="comicsansms 12 bold").pack(pady=5,side="left")

but=Button(f_1,text=">>",cursor = "hand2", bg = "#ff9642",fg= "white")
but['font']=fon
but.pack(pady=5,padx=102)

f_1.pack(anchor="w")

f_2=Frame(fbmain,borderwidth=8,bg="#ffe05d")

Label(f_2,text="Check Status",font="comicsansms 12 bold").pack(pady=5,side="left")

but=Button(f_2,text=">>",cursor = "hand2", bg = "#ff9642",fg= "white")
but['font']=fon
but.pack(pady=5,padx=50)

f_2.pack(anchor="w")


#-----NEW Registration-----
f_3=Frame(fbmain,borderwidth=8,bg="#ffe05d")

Label(f_3,text="New Registration",font="comicsansms 12 bold").pack(pady=5,side="left")

but=Button(f_3,text=">>",cursor = "hand2", bg = "#ff9642",fg= "white")
but['font']=fon
but.pack(pady=5,padx=20)

f_3.pack(anchor="w")
#-----------------------------

fbmain.pack(anchor="w",padx=250,pady=20,fill="x")


root.mainloop()