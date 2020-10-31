#-- -----Importing Library------------
from tkinter import *
import tkinter.font as font
import mysql.connector as msql
import tkinter.messagebox as tmsg

#------------------Database Connection---------------------------------------------------
mydb=msql.connect(host="localhost",user="Mahakaal",passwd="Ma4akaa1#@",database="reg_stud")

#--------------Initialization---------------
root=Tk()
root.title("Login Page")
root.geometry("850x400")

#--------Registration Form Variables----------

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
set_pass = StringVar()
income = StringVar()

#--------------Login Variable --------------

#------Student-------
stud_user = StringVar()
stud_pass = StringVar()

#------Admin---------
UniqueID = StringVar()
admin_pass = StringVar()

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

def call_admin_dashboard():
    admin_login().forget()
    Admin_dashboard()


def call_student_Dashboard():
    student_login_page.forget()
    f1.forget()
    fbmain.forget()
    student_dashboard()

#def call_home():


#-------------Functions for Database------------

#------Save to database -----------
def save_to_database():
    mycurss = mydb.cursor()

    sqlForm = "Insert into student (fname ,lname ,fat_fname, fat_lname ,mot_fname  ,mot_lname  ,phn ,email  ,per ,course ,username  ,pass ,income) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    student1 = (fName.get(),lName.get(),Fat_fName.get(),Fat_lName.get(),Mot_fName.get(),Mot_lName.get(),phn.get(),email.get(),per.get(),Course.get(),set_user.get(),set_pass.get(),income.get())
    mycurss.execute(sqlForm, student1)

    mydb.commit()


fon=font.Font(size=14,weight="bold")

#-------------Extra --------------
def check_pass_admin():
    mydb1 = msql.connect(host="localhost", user="Mahakaal", passwd="Ma4akaa1#@", database="reg_admin")
    str = UniqueID.get()
    mycurss = mydb1.cursor()
    sqlform = "SELECT * FROM admin WHERE uniqueID=" + "'" + str + "'"
    mycurss.execute(sqlform)
    myresult = mycurss.fetchall()
    for i in myresult:
        #Todo ----Mention Here index of the admin pass varible
        if i[4] ==admin_pass.get():
            call_admin_dashboard()
        else:
            tmsg.showinfo("Error,Wrong Password os Username Try Again")


def check_pass_student():
    str = stud_user.get()
    mycurss = mydb.cursor()
    sqlform = "SELECT * FROM student WHERE uname=" + "'" + str + "'"
    mycurss.execute(sqlform)
    myresult = mycurss.fetchall()
    for i in myresult:
        if i[12] == stud_pass.get():
            call_student_Dashboard()
        else:
            tmsg.showinfo("Error,Wrong Password os Username Try Again")


#------------------Dashboard Functions-------------------

def showStudentDetails():
    profileFrame = Frame(bg="white")
    profileFrame.pack(pady=40)
    profileHeading = Label(profileFrame, text="Profile Details", bg="#FFDC00", font="Arial 18 bold", pady=10)
    profileHeading.pack(fill=X)
    # declaring a new frame for the data
    dataFrame = Frame(profileFrame)
    dataFrame.pack(pady=10, padx=10)

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
    email1 = Label(bodyFrame, text="shashwatsingh71@gmail.com", font="Arial 11 bold", width=40, anchor=W).grid(row=5,
                                                                                                         column=1)
    email2 = Label(bodyFrame, text="vishnupsingh523@gmail.com", font="Arial 11 bold", width=40, anchor=W).grid(
    row=6, column=1)
    email3 = Label(bodyFrame, text="adityasinghpratham@gmail.com", font="Arial 11 bold", width=40, anchor=W).grid(
    row=7, column=1)

# websites
    websites = Label(bodyFrame, text="Websites:", font="Arial 15 bold").grid(row=8, column=0)
    website1 = Label(bodyFrame, text="https://linkedin.com/shashwatsingh", font="Arial 11 bold", width=40,
                 anchor=W).grid(row=9, column=1)
    website2 = Label(bodyFrame, text="https://linkedin.com/vishwanathpratapsingh", font="Arial 11 bold", width=40,
                 anchor=W).grid(row=10, column=1)
    website3 = Label(bodyFrame, text="https://linkedin.com/adityasinghpratham", font="Arial 11 bold", width=40,
                 anchor=W).grid(row=11, column=1)



# ------------------------------------ EXAMINATION FUNCTION ------------------------------------------------------------
def examination():
    mainframe = Frame(root, bg="#FF5733", bd=2)
    mainframe.pack(pady=40, padx=40)
    headingText = Label(mainframe, text="Examination Details", bg="#FF5733", font="Arial 20 bold")
    headingText.pack()
    bodyFrame = Frame(mainframe, padx=10, pady=10)
    bodyFrame.pack()


#-------------------Student DashBoard -------------------
def student_dashboard():

    root.title(100 * " " + "Student Dashboard")

    # adding top frame
    top_frame = Frame(bg="#001f3f", borderwidth=4)
    top_frame.pack(fill=X)

    # adding Label to top_frame
    topText = Label(top_frame, text="Rajputana University", bg="#001f3f", fg="white", font="Arial 14 bold")
    topText.pack(pady=10)

    # global variables for the funcitons ---------------------------------
    global count
    count = 0

    # -------------------------------------------------------------

    # examination()
    # -------------------------------------------------------- CREATING BUTTONS ----------------------------------------
    # frame for menuTab
    menuTab = Frame(bg="orange", borderwidth=0)
    menuTab.pack(fill=Y, side=LEFT)
    # inserting the buttons to the menuTab
    home = Button(menuTab, text="Home", cursor="hand2", borderwidth=0)
    home.pack(fill=X, padx=10, pady=20)

    cources = Button(menuTab, text="Cources", cursor="hand2", borderwidth=0)
    cources.pack(fill=X, padx=10, pady=20)

    examination = Button(menuTab, text="Examination", cursor="hand2", borderwidth=0)
    examination.pack(fill=X, padx=10, pady=20)

    contact = Button(menuTab, text="Contact Us", cursor="hand2", borderwidth=0, command=contactUs)
    contact.pack(fill=X, padx=10, pady=20)

    profile = Button(menuTab, text="Profile", cursor="hand2", borderwidth=0, command=showStudentDetails)
    profile.pack(fill=X, padx=10, pady=20)

    logout = Button(menuTab, text="Logout", cursor="hand2", borderwidth=0)
    profile.pack(fill=X, padx=10)

    home_frame = Frame(padx=20, pady=20, borderwidth=3, bg="red")
    home_frame.pack(fill=X)


#-------------------Admin Panal DashBoard -------------------
def Admin_dashboard():

    root.title(100 * " " + "Admin Dashboard")

    # adding top frame
    top_frame = Frame(bg="#001f3f", borderwidth=4)
    top_frame.pack(fill=X)

    # adding Label to top_frame
    topText = Label(top_frame, text="Rajputana University", bg="#001f3f", fg="white", font="Arial 14 bold")
    topText.pack(pady=10)


    menuTab = Frame(bg="orange", borderwidth=0)
    menuTab.pack(fill=Y, side=LEFT)
    # inserting the buttons to the menuTab
    home = Button(menuTab, text="Home", cursor="hand2", borderwidth=0,)#command=call_home)
    home.pack(fill=X, padx=10, pady=20)

    TotalStudents = Button(menuTab, text="Total Number Of New Registration", cursor="hand2", borderwidth=0)
    TotalStudents.pack(fill=X, padx=10, pady=20)

    examination = Button(menuTab, text="Examination", cursor="hand2", borderwidth=0)
    examination.pack(fill=X, padx=10, pady=20)

    contact = Button(menuTab, text="Contact Us", cursor="hand2", borderwidth=0, command=contactUs)
    contact.pack(fill=X, padx=10, pady=20)

    profile = Button(menuTab, text="Profile", cursor="hand2", borderwidth=0, command=showStudentDetails)
    profile.pack(fill=X, padx=10, pady=20)

    logout = Button(menuTab, text="Logout", cursor="hand2", borderwidth=0)
    profile.pack(fill=X, padx=10)

    home_frame = Frame(padx=20, pady=20, borderwidth=3, bg="red")
    home_frame.pack(fill=X)



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
    userEnt =Entry(f_1, textvariable=UniqueID,bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                 padx=10, pady=10)
    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="orange")

    Label(f_2, text="Password", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    pass_ = Entry(f_2, textvariable=admin_pass, show="*", bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                  padx=10, pady=10)
    f_2.pack(anchor="w")

    Button(fbmain, text="Connect", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold",command=check_pass_admin).pack()

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
    userEnt = Entry(f_1, textvariable=stud_user, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                 padx=10, pady=10)
    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="orange")
    Label(f_2, text="Password", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    pass_ = Entry(f_2, textvariable=stud_pass, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                  padx=10, pady=10)
    f_2.pack(anchor="w")

    Button(fbmain, text="Connect", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold",command=call_student_Dashboard).pack()#check_pass_student).pack()

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
    Label(fbmain, text="Registration Form", bg="orange", font="Arial 12 bold", fg="white", padx=20,
          borderwidth=4).pack()
    f_m1 = Frame(fbmain, bg="orange")

    f_1 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_1, text="First Name", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=2)

    fn = Entry(f_1, textvariable=fName, bg="#ffe05d", fg="black", font="Arial 10 bold")
    fn.grid(row=0, column=3, ipady=5, ipadx=5)

    Label(f_1, text="Last Name", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=5)

    ln = Entry(f_1, textvariable=lName, bg="#ffe05d", fg="black", font="Arial 10 bold")
    ln.grid(row=0, column=6, ipady=5, ipadx=5)
    f_1.grid(row=1, column=1)

    f_2 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_2, text="Father First Name", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=2)

    ffn = Entry(f_2, textvariable=Fat_fName, bg="#ffe05d", fg="black", font="Arial 10 bold")
    ffn.grid(row=0, column=3, ipady=5, ipadx=5)

    Label(f_2, text="Father Last Name", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=5)

    fln = Entry(f_2, textvariable=Fat_lName, bg="#ffe05d", fg="black", font="Arial 10 bold")
    fln.grid(row=0, column=6, ipady=5, ipadx=5, )
    f_2.grid(row=2, column=1)

    f_3 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_3, text="Mother First Name", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=2)

    mfn = Entry(f_3, textvariable=Mot_fName, bg="#ffe05d", fg="black", font="Arial 10 bold")
    mfn.grid(row=0, column=3, ipady=5, ipadx=5)

    Label(f_3, text="Mother Last Name", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=5)

    mln = Entry(f_3, textvariable=Mot_lName, bg="#ffe05d", fg="black", font="Arial 10 bold")
    mln.grid(row=0, column=6, ipady=5, ipadx=5, )
    f_3.grid(row=3, column=1)

    f_4 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_4, text="Phone Number", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=1)

    pn = Entry(f_4, textvariable=phn, bg="#ffe05d", fg="black", font="Arial 10 bold")
    pn.grid(row=0, column=2, ipady=5, ipadx=20)
    f_4.grid(row=4, column=1)

    f_5 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_5, text="Email ID", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=1)

    ee = Entry(f_5, textvariable=email, bg="#ffe05d", fg="black", font="Arial 10 bold")
    ee.grid(row=0, column=2, ipady=5, ipadx=10)
    f_5.grid(row=5, column=1)

    f_6 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_6, text="How % You Got In Class 12th(PCM) ?", font="comicsansms 10 bold", bg="orange", fg="white").grid(
        row=0, column=1)

    pe = Entry(f_6, textvariable=per, bg="#ffe05d", fg="black", font="Arial 10 bold")
    pe.grid(row=0, column=2, ipady=5, ipadx=10)
    f_6.grid(row=7, column=1)

    f_7 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_7, text="Which Course You Wants to Opt ?", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0,
                                                                                                                 column=1)

    co = Entry(f_7, textvariable=Course, bg="#ffe05d", fg="black", font="Arial 10 bold")
    co.grid(row=0, column=2, ipady=5, ipadx=10)
    f_7.grid(row=8, column=1)

    f_8 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_8, text="Set Your Username", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=1)

    Suser = Entry(f_8, textvariable=set_user, bg="#ffe05d", fg="black", font="Arial 10 bold")
    Suser.grid(row=0, column=2, ipady=5, ipadx=10)
    f_8.grid(row=9, column=1)

    f_9 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_9, text="Set Your Password", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=1)
    Spass = Entry(f_9, textvariable=set_pass, bg="#ffe05d", fg="black", font="Arial 10 bold")
    Spass.grid(row=0, column=2, ipady=5, ipadx=10)
    f_9.grid(row=10, column=1)

    f_10 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_10, text="Family Annual Income", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=1)

    Spass = Entry(f_10, textvariable=income, bg="#ffe05d", fg="black", font="Arial 10 bold")
    Spass.grid(row=0, column=2, ipady=5, ipadx=10)
    f_10.grid(row=11, column=1)

    f_m1.pack()

    Button(fbmain, text="Submit", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 10 bold",
           command=save_to_database).pack()

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
