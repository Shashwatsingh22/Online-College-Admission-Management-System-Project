from tkinter import *
import tkinter.font as font
import mysql.connector as msql
import tkinter.messagebox as tmsg


#--------------Intialization Of the Tkinter---------------
main_root = Tk()

#------------------Database Connection---------------------------------------------------
mydb=msql.connect(host="localhost",user="Mahakaal",passwd="Ma4akaa1#@",database="reg_stud")

#---------Variables for the registration Form---------------
fName = StringVar()
lName = StringVar()
Fat_fName = StringVar()
Fat_lName = StringVar()
Mot_fName = StringVar()
Mot_lName = StringVar()
phn = IntVar()
email = StringVar()
per = StringVar()
Course = StringVar()
set_user = StringVar()
set_pass = StringVar()
income=IntVar()

#-----------------Variables for the Login of Admin-----------
UniqueID = StringVar()
passwrd = StringVar()

#------------------Variables for the Login of Registered Student-----------
Studentuser = StringVar()
Studentpasswrd = StringVar()

#---------------Frames Variable----------------------------------------
student_login = Frame(main_root)
student_login.pack( fill = BOTH)

admin_login_frame = Frame(main_root)
admin_login_frame.pack(fill = BOTH)

#--------------------------------This will help us to take the student addmission or Not------------
def isAddmissionPossible(c12thmarks,famIncome):
    if c12thmarks >= 75 and famIncome <= 250000:
        return "Pass"
    elif c12thmarks < 75 and c12thmarks >= 65 and famIncome <= 250000:
        return "Waiting List"
    elif c12thmarks < 80 and c12thmarks >= 70 and famIncome <= 25000:
        return "Pass"
    else:
        return "Fail"

#-------------------Registration of the New Student ---->>>>Save to database ------------------

def save_to_database():
    mycurss = mydb.cursor()
    result=isAddmissionPossible(int(per.get()),int(income.get()))
    sqlForm = "Insert into student (fname ,lname ,fat_fname, fat_lname ,mot_fname  ,mot_lname  ,phn ,email  ,per ,course ,username  ,pass ,income,result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    student1 = (fName.get(),lName.get(),Fat_fName.get(),Fat_lName.get(),Mot_fName.get(),Mot_lName.get(),phn.get(),email.get(),per.get(),Course.get(),set_user.get(),set_pass.get(),income.get(),result)
    mycurss.execute(sqlForm, student1)
    mydb.commit()

#-----------------Credential Check--------------------
def check_pass_admin():
    str = UniqueID.get()
    mycurss = mydb.cursor()
    sqlform = "SELECT * FROM admin WHERE uniqueID=" + "'" + str + "'"
    mycurss.execute(sqlform)
    myresult = mycurss.fetchall()

    for i in myresult:
        #Todo ----Mention Here index of the admin pass varible
        if i[4] ==passwrd.get():
            #Here we need to call the function of the page of the Admin Dashboard
            adminDashboard()
        else:
            tmsg.showinfo("Error","Wrong Password os Username Try Again")


def check_pass_student():
    str = Studentuser.get()
    mycurss = mydb.cursor()
    sqlform = "SELECT * FROM student WHERE username=" + "'" + str + "'"
    mycurss.execute(sqlform)
    myresult = mycurss.fetchall()
    for i in myresult:
        if i[11] == Studentpasswrd.get():
            studentDashboard()

        else:
            tmsg.showinfo("Error","Wrong Password or Username Try Again")


# ------------------------------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# **************************************ADMIN DASHBOARD PAGE ***************************************
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ------------------------------------------------------------------------------------------------------------------------
adminDashboardRoot = Frame(main_root)
adminDashboardRoot.pack(fill = BOTH)
def adminDashboard():
    #Making Connection With Database to fetch the data  by the help of the username provide by the Admin at time login
        str = UniqueID.get()
        mycurss = mydb.cursor()
        sqlform = "SELECT * FROM admin WHERE uniqueID=" + "'" + str + "'"
        mycurss.execute(sqlform)
        myresult = mycurss.fetchall()

    # --------------------variables here we are fetching the data from the database and storing in variables-------------------
        adminname = myresult[0][0]
        adminjobdetail = myresult[0][1]
        adminphone = myresult[0][2]
        adminUniqueID1 = myresult[0][3]
  #---------------------------------------------------------------------------------------------------
        main_root.geometry("800x500")
        # setting the title
        main_root.title(100 * " " + "Admin Dashboard")
        # adding top frame
        top_frame = Frame(adminDashboardRoot, bg="#001f3f", borderwidth=4)
        top_frame.pack(fill=X)

        # adding Label to top_frame
        topText = Label(top_frame, text="Rajputana University", bg="#001f3f", fg="white", font="Arial 14 bold")
        topText.pack(pady=10)
        # frame for menuTab
        menuTab = Frame(adminDashboardRoot, bg="orange", borderwidth=0)
        menuTab.pack(fill=Y, side=LEFT)
        # -------------------------------------------------------------
        # defining home function

        home_frame = Frame(adminDashboardRoot, borderwidth=3, bg="light grey")
        home_frame.pack(fill=BOTH)

        def HomePage():

                imageCanvas = Canvas(home_frame, width=100, height=120, bg="lightgrey")
                imageCanvas.pack(side=LEFT, anchor=NW)
                imageCanvas.create_rectangle(2, 2, 100, 120, fill="white")

                detailFrame = Frame(home_frame, bd=3, padx=20, pady=40)
                detailFrame.pack(padx=20, pady=40, fill=X)

                # --------------------using the variables here-------------
                font = "Arial 15 bold"
                Label(detailFrame, text="Name", width=20, anchor=W, font=font).grid(row=0, column=0)
                Label(detailFrame, text="UniqueID", width=20, anchor=W, font=font).grid(row=1, column=0)

                Label(detailFrame, text=":", font=font).grid(row=0, column=1)
                Label(detailFrame, text=":", font=font).grid(row=1, column=1)

                Label(detailFrame, text=adminname, font=font, width=20, anchor=W).grid(row=0, column=2)
                Label(detailFrame, text=adminUniqueID1, font=font, width=20, anchor=W).grid(row=1, column=2)

                # news frame for giving the news for the administrator
                newsFrame = Frame(home_frame, bd=2, bg="black")
                newsFrame.pack(side=BOTTOM)

                newsHeading = Label(newsFrame, text=" Everything about Today :", font="Arial 20 bold")
                newsHeading.pack(fill=X)
                mainNews = Label(newsFrame,
                                 text="The curriculum and syllabus for B.Tech programs (2013) conform to outcome based teaching learning process. In general, ELEVEN \nSTUDENT OUTCOMES (a-k) have been identified and the curriculum and syllabus have been structured in such a  way that each of \nthe courses meets one or more of these outcomes. Student outcomes describe what students are expected to know and be able to \ndo by the time of graduation. These relate to the skills, knowledge, and behaviors that students acquire as they progress through the \nprogram. Further each course in the program spells out clear instructional objectives which are mapped to the student outcomes. ",
                                 anchor=W, justify=LEFT, pady=30)
                mainNews.pack()

        # ---------------------------------------------------------------------------------
        profileFrame = Frame(adminDashboardRoot, bg="white")
        profileFrame.pack(pady=40)

        def adminDetails():
                profileHeading = Label(profileFrame, text="Profile Details", bg="#FFDC00", font="Arial 18 bold",
                                       pady=10)
                profileHeading.pack(fill=X)
                # declaring a new frame for the data
                dataFrame = Frame(profileFrame)
                dataFrame.pack(pady=10, padx=10)
                # ---------------- HERE WE WILL BE FETCHING THE DATA WITH THE HELP OF FILE AND INSERT ALL THE DATA INSIDE THE VARIABLES AND AFTER THAT WE WILL INSERT THAT VARIABLE IN THE STUDENT'S DETAILS.---------------------------------
                Label(dataFrame, text="Name :", width=20, anchor=E).grid(row=0, column=0)
                Label(dataFrame,text=adminname ,width=20, anchor=W).grid(row=0, column=1)

                Label(dataFrame, text="UniqueID :", width=20, anchor=E).grid(row=1, column=0)
                Label(dataFrame,text=adminUniqueID1, width=20, anchor=W).grid(row=1, column=1)

                Label(dataFrame, text="Job Detail :", width=20, anchor=E).grid(row=3, column=0)
                Label(dataFrame,text=adminjobdetail ,width=20, anchor=W).grid(row=3, column=1)

                Label(dataFrame, text="Phone :", width=20, anchor=E).grid(row=4, column=0)
                Label(dataFrame,text=adminphone, width=20, anchor=W).grid(row=4, column=1)

#---------------Geting the detail for the registered student-------------------

        StudentFrame = Frame(adminDashboardRoot, bg="white")
        StudentFrame.pack(pady=40)

#TODO
        def studentDataFetch():
            profileHeading = Label(StudentFrame, text="Registered Student With Result", bg="#FFDC00",
                                   font="Arial 18 bold",
                                   pady=10)
            profileHeading.pack(fill=X)
            # declaring a new frame for the data
            dataFrame = Frame(StudentFrame)
            dataFrame.pack(pady=10, padx=10)
            # --------------

            mycurss = mydb.cursor()
            sqlform = "SELECT * FROM student"
            mycurss.execute(sqlform)
            myresult = mycurss.fetchall()

            count = 0

            for i in myresult:
                count += 1
            r=0
            for j in range(count):
                col=0
                Label(dataFrame, text="Name :", width=20, anchor=E).grid(row=r, column=col)
                col+=1
                Label(dataFrame, text=myresult[j][0]+" "+myresult[j][1], width=20, anchor=W).grid(row=r, column=col)
                col+=1
                Label(dataFrame, text="Phone Number :", width=20, anchor=E).grid(row=r, column=col)
                col+=1
                Label(dataFrame, text=myresult[j][6], width=20, anchor=W).grid(row=r, column=col)
                col+=1
                Label(dataFrame, text="Result :", width=20, anchor=E).grid(row=r, column=col)
                col+=1
                Label(dataFrame, text=myresult[j][13], width=20, anchor=W).grid(row=r, column=col)
                r+=1


                #-- HERE WE WILL BE FETCHING THE DATA WITH THE HELP OF FILE AND INSERT ALL THE DATA INSIDE THE VARIABLES AND AFTER THAT WE WILL INSERT THAT VARIABLE IN THE STUDENT'S DETAILS.---------------------------------

# -------------------------------------------------contact us--------------
        mainframe = Frame(adminDashboardRoot, bg="#FF5733", bd=2)
        mainframe.pack(pady=40, padx=40)

        def contactUs():
                headingText = Label(mainframe, text="Contact Us", bg="#FF5733", font="Arial 20 bold")
                headingText.pack()
                bodyFrame = Frame(mainframe, padx=10, pady=10)
                bodyFrame.pack()
                # Phone numbers of university
                phone = Label(bodyFrame, text="Phone:", font="Arial 15 bold").grid(row=0, column=0)
                Label(bodyFrame, text="123456897", font="Arial 11 bold", width=40, anchor=W).grid(row=1, column=1)
                Label(bodyFrame, text="8928340197", font="Arial 11 bold", width=40, anchor=W).grid(row=2, column=1)
                Label(bodyFrame, text="4853389726", font="Arial 11 bold", width=40, anchor=W).grid(row=3, column=1)

                # emails
                emails = Label(bodyFrame, text="Email:", font="Arial 15 bold").grid(row=4, column=0)
                email1 = Label(bodyFrame, text="shashwatsingh71@gmail.com", font="Arial 11 bold", width=40,
                               anchor=W).grid(row=5, column=1)
                email2 = Label(bodyFrame, text="vishnupsingh523@gmail.com", font="Arial 11 bold", width=40,
                               anchor=W).grid(row=6, column=1)
                email3 = Label(bodyFrame, text="adityasinghpratham@gmail.com", font="Arial 11 bold", width=40,
                               anchor=W).grid(row=7, column=1)

                # websites
                websites = Label(bodyFrame, text="Websites:", font="Arial 15 bold").grid(row=8, column=0)
                website1 = Label(bodyFrame, text="https://linkedin.com/shashwatsingh", font="Arial 11 bold", width=40,
                                 anchor=W).grid(row=9, column=1)
                website2 = Label(bodyFrame, text="https://linkedin.com/vishwanathpratapsingh", font="Arial 11 bold",
                                 width=40, anchor=W).grid(row=10, column=1)
                website3 = Label(bodyFrame, text="https://linkedin.com/adityasinghpratham", font="Arial 11 bold",
                                 width=40, anchor=W).grid(row=11, column=1)

        # ------------======================================================================
        # ==================  ALTERNATE FUNCTIONS  ==========================================
        # ====================================================================================
        def useHome():
                mainframe.forget()
                profileFrame.forget()

                home_frame.pack(fill=X)

        def useAdminDetails():
                mainframe.forget()
                home_frame.forget()

                profileFrame.pack(pady=40)

        def useContactUs():
                profileFrame.forget()
                home_frame.forget()
                mainframe.pack(pady=40, padx=40)

        def useStudentgetdetail():
            StudentFrame.forget()

        # -------------------------------------------------------- CREATING BUTTONS ----------------------------------------

        # inserting the buttons to the menuTab
        home = Button(menuTab, text="Home", cursor="hand2", borderwidth=0, command=useHome)
        home.pack(fill=X, padx=5, pady=70)

        contact = Button(menuTab, text="Contact Us", cursor="hand2", borderwidth=0, command=useContactUs)
        contact.pack(fill=X, padx=5, pady=50)

        profile = Button(menuTab, text="Profile", cursor="hand2", borderwidth=0, command=useAdminDetails)
        profile.pack(fill=X, padx=5, pady=70)


        studentdetail = Button(menuTab, text="Student List", cursor="hand2", borderwidth=0, command=studentDataFetch)
        studentdetail.pack(fill=X, padx=5, pady=70)

# logout = Button(menuTab, text = "Logout", cursor="hand2",borderwidth = 0)
        # logout.pack(fill= X, padx = 10, pady = 50)

        contactUs()
        adminDetails()
        HomePage()

        menuTab.lift()
        mainframe.forget()
        profileFrame.forget()

# ------------------------------------------------------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# ------------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# ************************************** ADMIN LOGIN PAGE ****************************************
# --------------------------------------------------------------------------------------------------


def adminLoginPage():
    # -----------------Functions--------


    fon = font.Font(size=14, weight="bold")

    # -------------------------------Heading---------------------
    f1 = Frame(admin_login_frame, relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body-------------------------
    fbmain = Frame(admin_login_frame, relief=SUNKEN, borderwidth=4, bg="orange", width=900)
    Label(fbmain, text="Admin Credentials", bg="orange", font="Arial 18 bold", fg="white", padx=20, pady=10,
          borderwidth=4).pack()

    f_1 = Frame(fbmain, borderwidth=8, bg="orange")

    Label(f_1, text="UniqueID", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    Entry(f_1, textvariable=UniqueID, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                 padx=10, pady=10)
    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="orange")

    Label(f_2, text="Password", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    Entry(f_2, textvariable=passwrd, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                  padx=10, pady=10)
    f_2.pack(anchor="w")

    Button(fbmain, text="Connect", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold",command = check_pass_admin).pack()

    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")
# -----------------------------------------------------------------------------------------------------------
# ***************************************************************xxxxxxxxxxxxxx***********************************
# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------
# ************************************************** STUDENT DASHBOARD ******************************************
# ----------------------------------------------------------------------------------------------------------------

root = Frame(main_root)
root.pack(fill= BOTH)
def studentDashboard():
    # Making Connection With Database to fetch the data  by the help of the username provide by the Student at time login
        str = Studentuser.get()
        mycurss = mydb.cursor()
        sqlform = "SELECT * FROM student WHERE username=" + "'" + str + "'"
        mycurss.execute(sqlform)
        myresult = mycurss.fetchall()

    # --------------------variables here we are fetching the data from the database and storing in variables-------------------
        studentName = myresult[0][0]+" "+myresult[0][1]
        studentFatName = myresult[0][2]+" "+myresult[0][3]
        studentMotName = myresult[0][4]+" "+myresult[0][5]
        studentPhoneNum = myresult[0][6]
        studentEmail = myresult[0][7]
        studentCourse=myresult[0][9]
        studentUsername=myresult[0][11]
        studentResult=myresult[0][13]
        # ---------------------------------------------------------------------------------------------------

        # adding top frame
        top_frame = Frame(root, bg="#001f3f", borderwidth=4)
        top_frame.pack(fill=X)

        # adding Label to top_frame
        topText = Label(top_frame, text="Rajputana University", bg="#001f3f", fg="white", font="Arial 14 bold")
        topText.pack(pady=10)
        # --------------------------------------frame for menuTab ----------------------------
        menuTab = Frame(root, bg="orange", borderwidth=0)
        menuTab.pack(fill=Y, side=LEFT)

        # ---------------------------------------HOME PAGE -----------------------------------
        home_frame = Frame(root, borderwidth=3, bg="light grey")
        home_frame.pack(fill=BOTH)

        def HomePage():
                imageCanvas = Canvas(home_frame, width=100, height=120, bg="lightgrey")
                imageCanvas.pack(side=LEFT, anchor=NW)
                imageCanvas.create_rectangle(2, 2, 100, 120, fill="white")

                detailFrame = Frame(home_frame, bd=3, padx=20, pady=40)
                detailFrame.pack(padx=20, pady=40, fill=X)

                # --------------------using the variables here-------------
                font = "Arial 15 bold"
                Label(detailFrame, text="Name", width=20, anchor=W, font=font).grid(row=0, column=0)
                Label(detailFrame, text="Course", width=20, anchor=W, font=font).grid(row=1, column=0)
                Label(detailFrame, text="Phone Number", width=20, anchor=W, font=font).grid(row=2, column=0)

                Label(detailFrame, text=":", font=font).grid(row=0, column=1)
                Label(detailFrame, text=":", font=font).grid(row=1, column=1)
                Label(detailFrame, text=":", font=font).grid(row=2, column=1)

                Label(detailFrame, text=studentName, font=font, width=20, anchor=W).grid(row=0, column=2)
                Label(detailFrame, text=studentCourse, font=font, width=20, anchor=W).grid(row=1, column=2)
                Label(detailFrame, text=studentPhoneNum, font=font, width=20, anchor=W).grid(row=2, column=2)

                # news frame for giving the news for the administrator
                newsFrame = Frame(home_frame, bd=2, bg="black")
                newsFrame.pack(side=BOTTOM)

                newsHeading = Label(newsFrame, text=" Everything about Today :", font="Arial 20 bold")
                newsHeading.pack(fill=X)
                mainNews = Label(newsFrame,
                                 text="The curriculum and syllabus for B.Tech programs (2013) conform to outcome based teaching learning process. In general, ELEVEN \nSTUDENT OUTCOMES (a-k) have been identified and the curriculum and syllabus have been structured in such a  way that each of \nthe courses meets one or more of these outcomes. Student outcomes describe what students are expected to know and be able to \ndo by the time of graduation. These relate to the skills, knowledge, and behaviors that students acquire as they progress through the \nprogram. Further each course in the program spells out clear instructional objectives which are mapped to the student outcomes. ",
                                 anchor=W, justify=LEFT, width=800)
                mainNews.pack()

        #    -------------------------------------------STUDENT DETALIS-----------------------
        profileFrame = Frame(root, bg="white")
        profileFrame.pack(pady=40)

        def showStudentDetails():
                profileHeading = Label(profileFrame, text="Profile Details", bg="#FFDC00", font="Arial 18 bold",
                                       pady=10)
                profileHeading.pack(fill=X)
                # declaring a new frame for the data
                dataFrame = Frame(profileFrame)
                dataFrame.pack(pady=10, padx=10)
                # ---------------- HERE WE WILL BE FETCHING THE DATA WITH THE HELP OF FILE AND INSERT ALL THE DATA INSIDE
                # -----THE VARIABLES AND AFTER THAT WE WILL INSERT THAT VARIABLE IN THE STUDENT'S DETAILS.----------------------

                Label(dataFrame, text="Name", width=20, anchor=W).grid(row=0, column=0)
                Label(dataFrame, text="Father Name", width=20, anchor=W).grid(row=1, column=0)
                Label(dataFrame, text="Mother Name", width=20, anchor=W).grid(row=2, column=0)
                Label(dataFrame, text="Email", width=20, anchor=W).grid(row=3, column=0)
                Label(dataFrame, text="Phone", width=20, anchor=W).grid(row=4, column=0)
                Label(dataFrame, text="Course", width=20, anchor=W).grid(row=5, column=0)
                Label(dataFrame, text="Username", width=20, anchor=W).grid(row=6, column=0)
                Label(dataFrame, text="Result", width=20, anchor=W).grid(row=7, column=0)

                Label(dataFrame, text=":").grid(row=0, column=1)
                Label(dataFrame, text=":").grid(row=1, column=1)
                Label(dataFrame, text=":").grid(row=2, column=1)
                Label(dataFrame, text=":").grid(row=3, column=1)
                Label(dataFrame, text=":").grid(row=4, column=1)
                Label(dataFrame, text=":").grid(row=5, column=1)
                Label(dataFrame, text=":").grid(row=6, column=1)
                Label(dataFrame, text=":").grid(row=7, column=1)

                Label(dataFrame, text=studentName,width=20, anchor=W).grid(row=0, column=2)
                Label(dataFrame,text=studentFatName, width=20, anchor=W).grid(row=1, column=2)
                Label(dataFrame,text=studentMotName, width=20, anchor=W).grid(row=2, column=2)
                Label(dataFrame,text=studentEmail, width=20, anchor=W).grid(row=3, column=2)
                Label(dataFrame,text=studentPhoneNum, width=20, anchor=W).grid(row=4, column=2)
                Label(dataFrame,text=studentCourse, width=20, anchor=W).grid(row=5, column=2)
                Label(dataFrame, text=studentUsername,width=20, anchor=W).grid(row=6, column=2)
                Label(dataFrame, text=studentResult, width=20, anchor=W).grid(row=7, column=2)

    # ----------------------------------------------------------------------------------------
        # -------------------------------------------------contact us--------------------------------
        # ----------------------------------------------------------------------------------------
        mainframe = Frame(root, bg="#FF5733", bd=2)
        mainframe.pack(pady=40, padx=40)

        def contactUs():
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
                email1 = Label(bodyFrame, text="shashwatsingh@gmail.com", font="Arial 11 bold", width=40,
                               anchor=W).grid(row=5, column=1)
                email2 = Label(bodyFrame, text="vishnupsingh523@gmail.com", font="Arial 11 bold", width=40,
                               anchor=W).grid(row=6, column=1)
                email3 = Label(bodyFrame, text="adityasinghpratham@gmail.com", font="Arial 11 bold", width=40,
                               anchor=W).grid(row=7, column=1)

                # websites
                websites = Label(bodyFrame, text="Websites:", font="Arial 15 bold").grid(row=8, column=0)
                website1 = Label(bodyFrame, text="https://linkedin.com/shashwatsingh", font="Arial 11 bold", width=40,
                                 anchor=W).grid(row=9, column=1)
                website2 = Label(bodyFrame, text="https://linkedin.com/vishwanathpratapsingh", font="Arial 11 bold",
                                 width=40, anchor=W).grid(row=10, column=1)
                website3 = Label(bodyFrame, text="https://linkedin.com/adityasinghpratham", font="Arial 11 bold",
                                 width=40, anchor=W).grid(row=11, column=1)

        # ------------------------------------ EXAMINATION FUNCTION ------------------------------------------------------------
        examFrame = Frame(root, bg="#FF5733", bd=2)
        examFrame.pack(pady=40, padx=40)

        def examination():
                headingText = Label(examFrame, text="Examination Details", bg="#FF5733", font="Arial 20 bold")
                headingText.pack(fill=X)
                Label(examFrame,
                      text="You have been selected for the your chosen\n degree or course and for the further process\n you have to come to the RAJPUTANA\n UNIVERSITY with your parents to check the\n hostels and other requirements for you in this\n University.",
                      bg="lightgreen", font="Arial 15 bold", anchor=W, justify=LEFT).pack(fill=BOTH)
                Label(examFrame,
                      text="Reporting date : 22nd November, 2020 Monday\nVenue : Block - 30 : Admission Block(for further Processes.\n\n\nRegards Admission Department\nRajputana University",
                      bg="lightyellow", font="Arial 10 bold", anchor=W, justify=LEFT, padx=5, pady=10).pack(fill=BOTH)

        # ------------------------ DEFINING SOME FUNCTIONS TO MANAGE THE PAGES -------------------
        def useHome():
                mainframe.forget()
                examFrame.forget()
                mainframe.forget()

                home_frame.pack(fill=BOTH)

        def useCources():
                mainframe.forget()
                examFrame.forget()
                home_frame.forget()
                profileFrame.forget()

        def useExamination():
                mainframe.forget()
                profileFrame.forget()
                home_frame.forget()

                examFrame.pack(pady=40, padx=40)

        def useContact():
                profileFrame.forget()
                examFrame.forget()
                home_frame.forget()

                mainframe.pack(pady=40, padx=40)

        def useProfile():
                mainframe.forget()
                examFrame.forget()
                home_frame.forget()

                profileFrame.pack(pady=40)

        def useLogout():
                mainframe.forget()
                examFrame.forget()
                home_frame.forget()
                profileFrame.forget()

        # -----------------------------------CREATING BUTTONS -----------------------------------

        # inserting the buttons to the menuTab
        home = Button(menuTab, text="Home", cursor="hand2", borderwidth=0, command=useHome)
        home.pack(fill=X, padx=10, pady=25)

        cources = Button(menuTab, text="Cources", cursor="hand2", borderwidth=0, command=useCources)
        cources.pack(fill=X, padx=10, pady=25)

        exam = Button(menuTab, text="Examination", cursor="hand2", borderwidth=0, command=useExamination)
        exam.pack(fill=X, padx=10, pady=30)

        contact = Button(menuTab, text="Contact Us", cursor="hand2", borderwidth=0, command=useContact)
        contact.pack(fill=X, padx=10, pady=25)

        profile = Button(menuTab, text="Profile", cursor="hand2", borderwidth=0, command=useProfile)
        profile.pack(fill=X, padx=10, pady=25)

        logout = Button(menuTab, text="Logout", cursor="hand2", borderwidth=0, command=useLogout)
        logout.pack(fill=X, padx=10, pady=25)

        # -------------------------calling all the functions here------------------------------
        HomePage()
        examination()
        showStudentDetails()
        contactUs()

        # HIDING THE FUNCTION'S FRAMES
        mainframe.forget()
        examFrame.forget()
        profileFrame.forget()
        # ------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
# *************************************************************** STUDENT LOGIN PAGE ***********************************
# -----------------------------------------------------------------------------------------------------------



def studentLoginPage():
    main_root.geometry("800x500")
    # setting the title
    main_root.title(100 * " " + "Student Dashboard")

    # -----------------Functions---------------------------------

    # -------------------------------Heading---------------------
    f1 = Frame(student_login, relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body----------------------------
    fbmain = Frame(student_login, relief=SUNKEN, borderwidth=4, bg="orange", width=900)
    Label(fbmain, text="Student Credentials", bg="orange", font="Arial 18 bold", fg="white", padx=20, pady=10,
          borderwidth=4).pack()

    f_1 = Frame(fbmain, borderwidth=8, bg="orange")
    Label(f_1, text="Username", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    Entry(f_1, textvariable=Studentuser, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                 padx=10, pady=10)
    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="orange")
    Label(f_2, text="Password", font="comicsansms 12 bold", bg="orange", fg="white").pack(pady=5, side="left")
    Entry(f_2, textvariable=Studentpasswrd, bg="#ffe05d", fg="white", font="Arial 12 bold").pack(ipady=5, ipadx=5,
                                                                                                  padx=10, pady=10)
    f_2.pack(anchor="w")

    Button(fbmain, text="Connect", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold",command= check_pass_student).pack()

    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")


# -----------------------------------------------------------------------------------------------------------
# ***************************************************************xxxxxxxxxxxxxx***********************************
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# *************************************************************** REGISTRATION PAGE ***********************************
# -----------------------------------------------------------------------------------------------------------
main_reg = Frame(main_root)
main_reg.pack(fill=BOTH)

def registrationPage():
    fon = font.Font(size=14, weight="bold")

    # -------------------------------Heading---------------------
    f1 = Frame(main_reg, relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    Label(f1, text="Est 1996", bg="Black", fg="white", font="lucida 12 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body-------------------------
    fbmain = Frame(main_reg, relief=SUNKEN, borderwidth=4, bg="orange", width=950, height=900)
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
    Spass = Entry(f_9, textvariable=set_pass, bg="#ffe05d", fg="black", font="Arial 12 bold")
    Spass.grid(row=0, column=2, ipady=5, ipadx=10)
    f_9.grid(row=10, column=1)

    f_10 = Frame(f_m1, borderwidth=8, bg="orange")
    Label(f_10, text="Family Annual Income", font="comicsansms 10 bold", bg="orange", fg="white").grid(row=0, column=1)
    Spass = Entry(f_10, textvariable=income, bg="#ffe05d", fg="black", font="Arial 10 bold")
    Spass.grid(row=0, column=2, ipady=5, ipadx=10)
    f_10.grid(row=11, column=1)

    f_m1.pack()

    Button(fbmain, text="Submit", cursor="hand2", bg="#0074D9", fg="white", relief=SUNKEN, font="Arial 12 bold", command =save_to_database).pack()
    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")
# -----------------------------------------------------------------------------------------------------------
# ***************************************************************xxxxxxxxxxxxxx***********************************
# -----------------------------------------------------------------------------------------------------------

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++ FUNCTIONS FOR THE COMMANDS IN MAIN LOGIN PAGE +++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def backToMain():
    main_reg.forget()
    student_login.forget()
    admin_login_frame.forget()

    main_login.pack(fill= BOTH)
    main_root.title("Login Page")
    main_root.geometry("850x400")

def useStudent_login():
    main_reg.forget()
    admin_login_frame.forget()
    main_login.forget()

    student_login.pack(fill = BOTH)

    main_root.title("Student Login Page")
    main_root.geometry("840x350")
    backButton = Button(student_login, text = "Back to Main",command = backToMain).pack(side = LEFT, anchor = NW)


def useAdmin_login():
    main_reg.forget()
    main_login.forget()
    student_login.forget()

    admin_login_frame.pack(fill= BOTH)

    main_root.title("Admin Login Page")
    main_root.geometry("840x350")
    backButton = Button(admin_login_frame, text = "Back to Main",command = backToMain).pack(side = LEFT, anchor = NW)


def useRegistration_Page():
    main_login.forget()
    student_login.forget()
    admin_login_frame.forget()

    main_reg.pack(fill=BOTH)

    #     geometry
    main_root.title("Registration Form")
    main_root.geometry("1500x700")
    backButton = Button(main_reg, text = "Back to Main",command = backToMain).pack(side = LEFT, anchor = NW)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# *******************************************************************************************************************
# ********************************************* MAIN LOGIN PAGE *****************************************************
# *******************************************************************************************************************

#-------------------------------------Root-----------------
main_login=Frame()
main_login.pack(fill = BOTH)

def mainLoginForm():
    main_root.title("Login Page")
    main_root.geometry("850x400")
    # --------------------SomeWidgets & Functions----------

    fon = font.Font(size=14, weight="bold")

    # -------------------------------Heading---------------------
    f1 = Frame(main_login, relief=SUNKEN, bg="black", borderwidth=4)
    Label(f1, text="Welcome To Rajputana University", bg="Black", fg="white", font="lucida 24 bold").pack()
    f1.pack(fill="x")

    # -------------------------Body-------------------------
    fbmain = Frame(main_login, relief=SUNKEN, bg="#ffe05d")

    Label(fbmain, text="LoginAs", bg="#ffe05d", fg="white", font="Arial 18 bold", padx=20, pady=10,
          borderwidth=4).pack()

    f_1 = Frame(fbmain, borderwidth=8, bg="#ffe05d")
    Label(f_1, text="Admin", font="comicsansms 12 bold").pack(pady=5, side="left")

    but = Button(f_1, text=">>", cursor="hand2", bg="#ff9642", fg="white", command = useAdmin_login)
    but['font'] = fon
    but.pack(pady=5, padx=102)

    f_1.pack(anchor="w")

    f_2 = Frame(fbmain, borderwidth=8, bg="#ffe05d")

    Label(f_2, text="Student Login", font="comicsansms 12 bold").pack(pady=5, side="left")

    but = Button(f_2, text=">>", cursor="hand2", bg="#ff9642", fg="white", command = useStudent_login)
    but['font'] = fon
    but.pack(pady=5, padx=50)

    f_2.pack(anchor="w")

    # -----NEW Registration-----
    f_3 = Frame(fbmain, borderwidth=8, bg="#ffe05d")

    Label(f_3, text="New Registration", font="comicsansms 12 bold").pack(pady=5, side="left")

    but = Button(f_3, text=">>", cursor="hand2", bg="#ff9642", fg="white", command = useRegistration_Page)
    but['font'] = fon
    but.pack(pady=5, padx=20)

    f_3.pack(anchor="w")
    # -----------------------------

    fbmain.pack(anchor="w", padx=250, pady=20, fill="x")


mainLoginForm()
studentLoginPage()
adminLoginPage()
registrationPage()
student_login.forget()
admin_login_frame.forget()
main_reg.forget()

main_root.mainloop()
