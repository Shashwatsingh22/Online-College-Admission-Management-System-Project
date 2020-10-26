from tkinter import *

root = Tk()
# setting the geometry(800x500)
root.geometry("800x500")
# setting the title
root.title(100*" "+"Student Dashboard")

# adding top frame
top_frame = Frame(bg = "#001f3f", borderwidth =4 )
top_frame.pack(fill = X)

# adding Label to top_frame
topText = Label(top_frame,text = "Singh University",bg = "#001f3f", fg = "white",font="Arial 14 bold")
topText.pack(pady = 10)

# global variables for the funcitons ---------------------------------
global count
count = 0
# -------------------------------------------------------------

def showStudentDetails():
        profileFrame = Frame(bg = "white")
        profileFrame.pack(pady = 40)
        profileHeading = Label(profileFrame, text="Profile Details", bg="#FFDC00", font="Arial 18 bold", pady=10)
        profileHeading.pack(fill=X)
        # declaring a new frame for the data
        dataFrame = Frame(profileFrame)
        dataFrame.pack(pady=10,padx=10)
        # ---------------- HERE WE WILL BE FETCHING THE DATA WITH THE HELP OF FILE AND INSERT ALL THE DATA INSIDE THE VARIABLES AND AFTER THAT WE WILL INSERT THAT VARIABLE IN THE STUDENT'S DETAILS.---------------------------------
        Name = Label(dataFrame, text = "Name :",width = 20, anchor=E).grid(row =0, column = 0)
        studentName = Label(dataFrame,width = 20, anchor=W).grid(row =0, column = 1)

        Reg = Label(dataFrame, text = "Rregistration Number :",width = 20, anchor=E).grid(row =1, column = 0)
        studentReg = Label(dataFrame,width = 20, anchor=W).grid(row =1, column = 1)

        Course = Label(dataFrame, text = "Course :",width = 20, anchor=E).grid(row =2, column = 0)
        studentCourse = Label(dataFrame,width = 20, anchor=W).grid(row =2, column = 1)

        Email = Label(dataFrame, text = "Email :",width = 20, anchor=E).grid(row =3, column = 0)
        studentEmail = Label(dataFrame,width = 20, anchor=W).grid(row =3, column = 1)

        Phone = Label(dataFrame, text = "Phone :",width = 20, anchor=E).grid(row =4, column = 0)
        studentPhone = Label(dataFrame,width = 20, anchor=W).grid(row =4, column = 1)

        ParentPhone = Label(dataFrame, text = "Parent's Phone :",width = 20, anchor=E).grid(row =5, column = 0)
        studentParentPhone = Label(dataFrame,width = 20, anchor=W).grid(row =5, column = 1)

        Address = Label(dataFrame, text = "Address :",width = 20, anchor=E).grid(row =6, column = 0)
        studentAddress = Label(dataFrame,width = 20, anchor=W).grid(row =6, column = 1)


# -------------------------------------------------contact us--------------
def contactUs():
        mainframe = Frame(root,bg = "#FF5733",bd=2)
        mainframe.pack(pady=40,padx=40)
        headingText = Label(mainframe,text="Contact Us",bg = "#FF5733", font="Arial 20 bold")
        headingText.pack()
        bodyFrame = Frame(mainframe, padx=10,pady=10)
        bodyFrame.pack()
        # Phone numbers of university
        phone = Label(bodyFrame, text="Phone:",font="Arial 15 bold").grid(row=0,column=0)
        Label(bodyFrame, text = "8928340197",font = "Arial 11 bold", width = 40, anchor=W).grid(row=1,column=1)
        Label(bodyFrame, text = "8928340197",font = "Arial 11 bold", width = 40, anchor=W).grid(row=2,column=1)
        Label(bodyFrame, text = "8928340197",font = "Arial 11 bold", width = 40, anchor=W).grid(row=3,column=1)

        # emails
        emails = Label(bodyFrame, text = "Email:", font="Arial 15 bold").grid(row=4, column = 0)
        email1 = Label(bodyFrame, text = "shashwatsingh@gmail.com",font = "Arial 11 bold", width = 40, anchor=W).grid(row=5,column=1)
        email2 = Label(bodyFrame, text = "vishnupsingh523@gmail.com",font = "Arial 11 bold", width = 40, anchor=W).grid(row=6,column=1)
        email3 = Label(bodyFrame, text = "adityasinghpratham@gmail.com",font = "Arial 11 bold", width = 40, anchor=W).grid(row=7,column=1)

        # websites
        websites = Label(bodyFrame, text = "Websites:",font = "Arial 15 bold").grid(row=8,column=0)
        website1 = Label(bodyFrame, text = "https://linkedin.com/shashwatsingh",font = "Arial 11 bold", width = 40, anchor=W).grid(row=9,column=1)
        website2 = Label(bodyFrame, text = "https://linkedin.com/vishwanathpratapsingh",font = "Arial 11 bold", width = 40, anchor=W).grid(row=10,column=1)
        website3 = Label(bodyFrame, text = "https://linkedin.com/adityasinghpratham",font = "Arial 11 bold", width = 40, anchor=W).grid(row=11,column=1)


# ------------------------------------ EXAMINATION FUNCTION ------------------------------------------------------------
def examination():
        mainframe = Frame(root, bg="#FF5733", bd=2)
        mainframe.pack(pady=40, padx=40)
        headingText = Label(mainframe, text="Examination Details", bg="#FF5733", font="Arial 20 bold")
        headingText.pack()
        bodyFrame = Frame(mainframe, padx=10, pady=10)
        bodyFrame.pack()

# examination()
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

# *----------------------------------------*** Defining Functions *** -------------------------------------------------*
# defining home function
def HomePage():
        text = Label(home_frame,text="Name",padx=10)
        text.pack()
HomePage()
# defining function to foreget the text
def forgetHome():
        home_frame.forget()
forgetHome()



root.mainloop()
