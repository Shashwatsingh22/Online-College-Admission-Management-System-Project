# here is the main file of the student Dashboard for the project " ONLINE INTERACTIVE SYSTEM FOR COLLAGE ADMISSION PURPOSES

from tkinter import *

root = Tk()
# setting the geometry(800x500)
root.geometry("800x500")

# adding top frame
top_frame = Frame(bg = "#001f3f", borderwidth =4 )
top_frame.pack(fill = X)

# adding Label to top_frame
topText = Label(top_frame,text = "Student Dashboard",bg = "#001f3f", fg = "white",font="Arial 14 bold")
topText.pack(pady = 10)

# variables for the funcitons ---------------------------------
count = 0
# -------------------------------------------------------------
def showStudentDetails():
    if count == 0:
        count = count + 1
        profileFrame = Frame(bg = "white")
        profileFrame.pack(pady = 40)
        profileHeading = Label(profileFrame,text = "Profile Details",bg = "#FFDC00",font = "Arial 18 bold", padx = 20,pady = 10)
        profileHeading.pack(fill = X)
        studentName = Label(profileFrame, text = "Name: Vishwanath Pratap Singh", bg = "grey")
        studentName.pack(pady= 40)

#     update profile button
        updateButton = Button(text = "Update Profile", cursor = "hand2", bg = "#0074D9",fg= "white", relief = SUNKEN)
        updateButton.pack()


# ------------------------------------------------------------
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

contact = Button(menuTab, text = "Contact Us",cursor = "hand2",borderwidth = 0)
contact.pack(fill =X,padx=10, pady=20)

profile = Button(menuTab, text = "Profile",cursor = "hand2",borderwidth = 0, command= showStudentDetails)
profile.pack(fill =X,padx=10, pady=20)

logout = Button(menuTab, text = "Logout", cursor="hand2",borderwidth = 0)
profile.pack(fill= X, padx = 10)


root.mainloop()
