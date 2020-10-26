from tkinter import *
import tkinter.font as font
import time
import os

root=Tk()
root.title("Login Page")
root.geometry("850x500")


# ------------------------------------------ LOADING PAGE GIF EDITING---------------------------------------------------
# gifframe = Frame().pack()
# frames = [PhotoImage(gifframe,file='images/loading.gif',format = 'gif -index %i' %(i)) for i in range(100)]
#
# def update(ind):
#
#     frame = frames[ind]
#     count = 0
#     if ind == 99:
#         ind = 0
#         count = count +1
#     else:
#         ind = ind + 3
#     label.configure(image=frame)
#     root.after(100, update, ind)
#     if count == 2:
#         gifframe.forget()
#
#
# label = Label(root)
# label.pack()
# root.after(0, update, 0)

# ---------------------------------------- STUDENT DASHBOARD FUNCTIONS--------------------------------------------------
# ---------------------------------------- EXAMINATION FUNCTION ------------------------------------------------------------
def examination():
        mainframe = Frame(root, bg="#FF5733", bd=2)
        mainframe.pack(pady=40, padx=40)
        headingText = Label(mainframe, text="Examination Details", bg="#FF5733", font="Arial 20 bold")
        headingText.pack()
        bodyFrame = Frame(mainframe, padx=10, pady=10)
        bodyFrame.pack()

# examination()
def showStudentDetails():
    profileFrame = Frame(bg="white")
    profileFrame.pack(pady=40)
    profileHeading = Label(profileFrame, text="Profile Details", bg="#FFDC00", font="Arial 18 bold", pady=10)
    profileHeading.pack(fill=X)
    # declaring a new frame for the data
    dataFrame = Frame(profileFrame)
    dataFrame.pack(pady=10, padx=10)
    # ---------------- HERE WE WILL BE FETCHING THE DATA WITH THE HELP OF FILE AND INSERT ALL THE DATA INSIDE THE VARIABLES AND AFTER THAT WE WILL INSERT THAT VARIABLE IN THE STUDENT'S DETAILS.---------------------------------
    Name = Label(dataFrame, text="Name :", width=20, anchor=E).grid(row=0, column=0)
    studentName = Label(dataFrame, width=20, anchor=W).grid(row=0, column=1)

    Reg = Label(dataFrame, text="Rregistration Number :", width=20, anchor=E).grid(row=1, column=0)
    studentReg = Label(dataFrame, width=20, anchor=W).grid(row=1, column=1)

    Course = Label(dataFrame, text="Course :", width=20, anchor=E).grid(row=2, column=0)
    studentCourse = Label(dataFrame, width=20, anchor=W).grid(row=2, column=1)

    Email = Label(dataFrame, text="Email :", width=20, anchor=E).grid(row=3, column=0)
    studentEmail = Label(dataFrame, width=20, anchor=W).grid(row=3, column=1)

    Phone = Label(dataFrame, text="Phone :", width=20, anchor=E).grid(row=4, column=0)
    studentPhone = Label(dataFrame, width=20, anchor=W).grid(row=4, column=1)

    ParentPhone = Label(dataFrame, text="Parent's Phone :", width=20, anchor=E).grid(row=5, column=0)
    studentParentPhone = Label(dataFrame, width=20, anchor=W).grid(row=5, column=1)

    Address = Label(dataFrame, text="Address :", width=20, anchor=E).grid(row=6, column=0)
    studentAddress = Label(dataFrame, width=20, anchor=W).grid(row=6, column=1)


# -------------------------------------------------contact us--------------
def contactUs():
    mainframe = Frame(root, bg="#FF5733", bd=2)
    mainframe.pack(pady=40, padx=40)
    headingText = Label(mainframe, text="Contact Us", bg="#FF5733", font="Arial 20 bold")
    headingText.pack()
    bodyFrame = Frame(mainframe, padx=10, pady=10)
    bodyFrame.pack()
    # Phone numbers of university
    phone = Label(bodyFrame, text="Phone:", font="Arial 15 bold").grid(row=0, column=0)
    Label(bodyFrame, text="8928340197", font="Arial 11 bold", width=40, anchor=W).grid(row=1, column=1)
    Label(bodyFrame, text="8928340197", font="Arial 11 bold", width=40, anchor=W).grid(row=2, column=1)
    Label(bodyFrame, text="8928340197", font="Arial 11 bold", width=40, anchor=W).grid(row=3, column=1)

    # emails
    emails = Label(bodyFrame, text="Email:", font="Arial 15 bold").grid(row=4, column=0)
    email1 = Label(bodyFrame, text="shashwatsingh@gmail.com", font="Arial 11 bold", width=40, anchor=W).grid(row=5,
                                                                                                             column=1)
    email2 = Label(bodyFrame, text="vishnupsingh523@gmail.com", font="Arial 11 bold", width=40, anchor=W).grid(row=6,
                                                                                                               column=1)
    email3 = Label(bodyFrame, text="adityasinghpratham@gmail.com", font="Arial 11 bold", width=40, anchor=W).grid(row=7,
                                                                                                                  column=1)

    # websites
    websites = Label(bodyFrame, text="Websites:", font="Arial 15 bold").grid(row=8, column=0)
    website1 = Label(bodyFrame, text="https://linkedin.com/shashwatsingh", font="Arial 11 bold", width=40,
                     anchor=W).grid(row=9, column=1)
    website2 = Label(bodyFrame, text="https://linkedin.com/vishwanathpratapsingh", font="Arial 11 bold", width=40,
                     anchor=W).grid(row=10, column=1)
    website3 = Label(bodyFrame, text="https://linkedin.com/adityasinghpratham", font="Arial 11 bold", width=40,
                     anchor=W).grid(row=11, column=1)


# ----------------------------------------------------STUDENT DASHBOARD ---------------------------------------------------------------
def studentDashboard():

    root.title(100*" "+"Student Dashboard")

# adding top frame
    top_frame = Frame(bg = "#001f3f", borderwidth =4 )
    top_frame.pack(fill = X)

# adding Label to top_frame
    topText = Label(top_frame,text = "Rajputana University - Student Dashboard",bg = "#001f3f", fg = "white",font="Arial 14 bold")
    topText.pack(pady = 10)

# -------------------------------------------------------------


# -------------------------------------------------------- CREATING BUTTONS ----------------------------------------
# frame for menuTab
    menuTab = Frame(bg = "orange",borderwidth = 0)
    menuTab.pack(fill=Y , side = LEFT)
# inserting the buttons to the menuTab
    home = Button(menuTab, text = "Home",cursor = "hand2",borderwidth = 0)
    home.pack(fill =X,padx=10, pady=20)

    cources = Button(menuTab, text = "Cources", cursor = "hand2",borderwidth = 0)
    cources.pack(fill =X,padx=10, pady=20)

    examination = Button(menuTab, text = "Examination",cursor = "hand2",borderwidth = 0)
    examination.pack(fill =X,padx=10, pady=20)

    contact = Button(menuTab, text = "Contact Us",cursor = "hand2",borderwidth = 0, command = contactUs)
    contact.pack(fill =X,padx=10, pady=20)

    profile = Button(menuTab, text = "Profile",cursor = "hand2",borderwidth = 0, command= showStudentDetails)
    profile.pack(fill =X,padx=10, pady=20)

    logout = Button(menuTab, text = "Logout", cursor="hand2",borderwidth = 0)
    profile.pack(fill= X, padx = 10)


    home_frame = Frame(padx = 20,pady = 20,borderwidth = 3, bg = "red")
    home_frame.pack(fill = X)


#--------Variables----------

fName = StringVar()
lName = StringVar()
Fat_fName = StringVar()
Fat_lName = StringVar()
Mot_fName = StringVar()
Mot_lName = StringVar()
per = StringVar()
phn = IntVar()
email = StringVar()
Course = StringVar()
set_user = StringVar()

#-----------------Call Pages Functions--------

def call_admin_page():
    main_login_frame.forget()
    admin_login()

def call_student_page():
    main_login_frame.forget()
    student_login_page()

def call_reg_page():
    main_login_frame.forget()
    reg_page()




def save_data():
    with open("Data\data.txt","w") as file:
        file.write(f"{fName.get(),lName.get(),Fat_fName.get(),Fat_lName.get(),Mot_fName.get(),Mot_lName.get(),phn.get(),email.get(),per.get(),Course.get(),set_user.get(),set_pass.get()}\n")

fon=font.Font(size=14,weight="bold")

def admin_login():
    # -------------------------------Heading---------------------
    f1 = Frame(relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body-------------------------
    fbmain = Frame(relief=SUNKEN, borderwidth=4, bg="orange", width=900)
    Label(fbmain, text="Admin Credentials", bg="orange", font="Arial 18 bold", fg="white", padx=20, pady=10,
          borderwidth=4).pack()

    f_1 = Frame(fbmain, borderwidth=8, bg="orange")

    Label(f_1, text="UniqueID", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    user = StringVar()
    userEnt = Entry(f_1, textvariable=user, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                 padx=10, pady=10)
    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="orange")

    Label(f_2, text="Password", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    passwrd = StringVar()
    pass_ = Entry(f_2, textvariable=passwrd, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                  padx=10, pady=10)
    f_2.pack(anchor="w")

    Button(fbmain, text="Connect", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold").pack()

    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")

def student_login_page():
    f1 = Frame(relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body----------------------------
    fbmain = Frame(relief=SUNKEN, borderwidth=4, bg="orange", width=900)
    Label(fbmain, text="Student Credentials", bg="orange", font="Arial 18 bold", fg="white", padx=20, pady=10,
          borderwidth=4).pack()

    f_1 = Frame(fbmain, borderwidth=8, bg="orange")
    Label(f_1, text="Username", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    user = StringVar()
    userEnt = Entry(f_1, textvariable=user, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                 padx=10, pady=10)
    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="orange")
    Label(f_2, text="Password", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    passwrd = StringVar()
    pass_ = Entry(f_2, textvariable=passwrd, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                  padx=10, pady=10)
    f_2.pack(anchor="w")

    # Forget function for the student dashboard--------------------------------------------------------------------
    def studentDashboardPage():
        f1.forget()
        fbmain.forget()
        studentDashboard()
    Button(fbmain, text="Connect", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold", command = studentDashboardPage).pack()

    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")


def reg_page():
    def call_main_page():
        reg_page.forget()
        main_login_frame()

    root.geometry("1580x700")
    fon = font.Font(size=14, weight="bold")

    # -------------------------------Heading---------------------
    f1 = Frame(relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    Label(f1, text="Est 1996", bg="Black", fg="white", font="lucida 12 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body-------------------------
    fbmain = Frame(relief=SUNKEN, borderwidth=4, bg="orange", width=950, height=900)
    Button(fbmain, text="Back", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold",
           command=main_login_frame).pack(anchor='w',padx=10,pady=5)


    root.title("Login Page")
    Label(fbmain, text="Registration Form", bg="orange", font="Arial 18 bold", fg="white", padx=20, pady=10,
          borderwidth=4).pack()
    f_m1 = Frame(fbmain, bg="orange")

    f_1 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_1, text="First Name", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=2)

    fn = Entry(f_1, textvariable=fName, bg="#ffe05d", fg="black", font="Arial 12 bold")
    fn.grid(row=0, column=3, ipady=5, ipadx=5)

    Label(f_1, text="Last Name", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=5)

    ln = Entry(f_1, textvariable=lName, bg="#ffe05d", fg="black", font="Arial 12 bold")
    ln.grid(row=0, column=6, ipady=5, ipadx=5)
    f_1.grid(row=1, column=1)

    f_2 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_2, text="Father First Name", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=2)

    ffn = Entry(f_2, textvariable=Fat_fName, bg="#ffe05d", fg="black", font="Arial 12 bold")
    ffn.grid(row=0, column=3, ipady=5, ipadx=5)

    Label(f_2, text="Father Last Name", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=5)

    fln = Entry(f_2, textvariable=Fat_lName, bg="#ffe05d", fg="black", font="Arial 12 bold")
    fln.grid(row=0, column=6, ipady=5, ipadx=5, )
    f_2.grid(row=2, column=1)

    f_3 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_3, text="Mother First Name", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=2)

    mfn = Entry(f_3, textvariable=Mot_fName, bg="#ffe05d", fg="black", font="Arial 12 bold")
    mfn.grid(row=0, column=3, ipady=5, ipadx=5)

    Label(f_3, text="Mother Last Name", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=5)

    mln = Entry(f_3, textvariable=Mot_lName, bg="#ffe05d", fg="black", font="Arial 12 bold")
    mln.grid(row=0, column=6, ipady=5, ipadx=5, )
    f_3.grid(row=3, column=1)

    f_4 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_4, text="Phone Number", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=1)

    pn = Entry(f_4, textvariable=phn, bg="#ffe05d", fg="black", font="Arial 12 bold")
    pn.grid(row=0, column=2, ipady=5, ipadx=20)
    f_4.grid(row=4, column=1)

    f_5 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_5, text="Email ID", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=1)

    ee = Entry(f_5, textvariable=email, bg="#ffe05d", fg="black", font="Arial 12 bold")
    ee.grid(row=0, column=2, ipady=5, ipadx=10)
    f_5.grid(row=5, column=1)

    f_6 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_6, text="How % You Got In Class 12th(PCM) ?", font="comicsansms 12 bold", bg="orange", fg="white").grid(
        row=0, column=1)

    pe = Entry(f_6, textvariable=per, bg="#ffe05d", fg="black", font="Arial 12 bold")
    pe.grid(row=0, column=2, ipady=5, ipadx=10)
    f_6.grid(row=7, column=1)

    f_7 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_7, text="Which Course You Wants to Opt ?", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0,
                                                                                                                 column=1)

    co = Entry(f_7, textvariable=Course, bg="#ffe05d", fg="black", font="Arial 12 bold")
    co.grid(row=0, column=2, ipady=5, ipadx=10)
    f_7.grid(row=8, column=1)

    f_8 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_8, text="Set Your Username", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=1)

    Suser = Entry(f_8, textvariable=set_user, bg="#ffe05d", fg="black", font="Arial 12 bold")
    Suser.grid(row=0, column=2, ipady=5, ipadx=10)
    f_8.grid(row=9, column=1)

    f_9 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_9, text="Set Your Password", font="comicsansms 12 bold", bg="orange", fg="white").grid(row=0, column=1)
    set_pass = StringVar()
    Spass = Entry(f_9, textvariable=set_pass, bg="#ffe05d", fg="black", font="Arial 12 bold")
    Spass.grid(row=0, column=2, ipady=5, ipadx=10)
    f_9.grid(row=10, column=1)

    f_m1.pack()

    Button(fbmain, text="Submit", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold",
           command=save_data).pack()

    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")

#---------- Main Login Page ----------

main_login_frame=Frame(root)
main_login_frame.pack()


fon = font.Font(size=14, weight="bold")

# -------------------------------Heading---------------------
f1 = Frame(main_login_frame, bg="black", borderwidth=4)
Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
f1.pack(fill="x")

    # -------------------------Body-------------------------
fbmain = Frame(main_login_frame,relief=SUNKEN, bg="#ffe05d")

Label(fbmain, text="LoginAs", bg="#ffe05d", fg="white", font="Arial 18 bold", padx=20, pady=10,borderwidth=4).pack()

f_1 = Frame(fbmain, borderwidth=8, bg="#ffe05d")
Label(f_1, text="Admin", font="comicsansms 12 bold").pack(pady=5, side="left")

but = Button(f_1, text=">>", cursor="hand2", bg="#ff9642", fg="white",command=call_admin_page)
but['font'] = fon
but.pack(pady=5, padx=102)

f_1.pack(anchor="w")

f_2 = Frame(fbmain, borderwidth=8, bg="#ffe05d")

Label(f_2, text="Check Status", font="comicsansms 12 bold").pack(pady=5, side="left")

but = Button(f_2, text=">>", cursor="hand2", bg="#ff9642", fg="white",command=call_student_page)
but['font'] = fon
but.pack(pady=5, padx=50)

f_2.pack(anchor="w")

    # -----NEW Registration-----
f_3 = Frame(fbmain, borderwidth=8, bg="#ffe05d")

Label(f_3, text="New Registration", font="comicsansms 12 bold").pack(pady=5, side="left")

but = Button(f_3, text=">>", cursor="hand2", bg="#ff9642", fg="white",command=call_reg_page)
but['font'] = fon
but.pack(pady=5, padx=20)

f_3.pack(anchor="w")
    # -----------------------------

fbmain.pack(anchor="w", padx=250, pady=20, fill="x")


root.mainloop()
