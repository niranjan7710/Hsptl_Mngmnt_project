import mysql.connector
from tkinter import *
from tkinter import messagebox
import sqlalchemy

# =================================================================Tkinter Window=====================================================================
root = Tk()
root.state('zoomed')
root.title("Hospital Management System")
root.geometry("1920x1080")
root.resizable(False, False)
# ===================================================================================================================================================


def swap(frame):
    frame.tkraise()



# ======================================================================PATIENT DETAILS-Delete=========================================================================================

F_pd_del = Frame(root, border=8, background="#212121", relief=RIDGE)
F_pd_del.place(x=0, y=0, width=1920, height=1080)


Label(F_pd_del, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)

label_title = Label(F_pd_del, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pd_del, bd=5, relief=RIDGE, text="DISCHARGE SUMMARY",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


frame = Frame(F_pd_del,bd=8, bg="#2b2d42")
frame.place(x=400, y=225, width=1180, height=620)



engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:vyasa@localhost/hospital_management')
con = engine.connect()
con.execute("use hospital_management")



Label(frame, fg="white",bg="#2b2d42", text="Patient ID", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
Patient_ID = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
Patient_ID.place(x=550, y=50, width=290, height=33)


def del_data():
    flag_validation = True  # set the flag
    ID = Patient_ID.get()  # read ID

    if (len(ID) < 1):
        flag_validation = False
    try:
        val = int(ID)
    except:
        flag_validation = False

    if (flag_validation):

        query = f"DELETE FROM patient_details WHERE Patient_ID ={ID}"
        
        id = engine.execute(query)
        messagebox.showinfo("Success", "record deleted successfully")

        swap(F_pdetails)
            
    else:
        l5.config(fg='red', bg='yellow')
        chk_str.set("Check inputs")

def conf_del():
    frame1 = Frame(F_pd_del,bd=5,bg="#2b2d42") 
    frame1.place(x=400, y=425, width=1180, height=250)

    id = Patient_ID.get()

    if id == '' or id == ' ':
        messagebox.showerror("Error","Enter an ID")

    else:
        query = f"SELECT * FROM patient_details WHERE Patient_ID = {id}"
        result = con.execute(query)

        i = 0
        x = result.fetchone()
        try:
            e = Label(frame1, width=20, text='Patient_ID', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=0)
        #    e.grid_columnconfigure(0,weigh3t=1)

            e = Label(frame1, width=20, text='Name', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=1)
        #    e.grid_columnconfigure(1,weight=2)

            e = Label(frame1, width=20, text='sex', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=2)
        #    e.grid_columnconfigure(2,weight=3)

            e = Label(frame1, width=20, text='age', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=3)

            e = Label(frame1, width=20, text='Address', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=4)

            e = Label(frame1, width=20, text='Ph. Num', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=5)

            for patient in x:
                e = Label(frame1, width=20,bg="#2b2d42",fg="white", text=patient, borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor="w")
                e.grid(row=1, column=i)

                i += 1

            button_del = Button(frame1, text="Confirm Delete", command=lambda: del_data(), height=3, width=13, bd=7,
                                bg="#242424", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
            button_del.place(x=510, y=180, width=130, height=53)
        except:
            messagebox.showerror("Error","No records Found")

button_del = Button(frame, text="Search", command=lambda: conf_del(), height=3, width=13, bd=7,
                    bg="#242424", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_del.place(x=600, y=500, width=130, height=53)

button_add = Button(frame, text="Go Back", command=lambda: swap(F_pdetails), height=3, width=13, bd=7,
                    bg="#242424", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_add.place(x=400, y=500, width=130, height=53)


# ======================================================================PATIENT DETAILS-Delete ENDS=========================================================================================


# ======================================================================PATIENT DETAILS-Add=========================================================================================


F_pd_add = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pd_add.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_pd_add, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pd_add, bd=5, relief=RIDGE, text="Add New Patient",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)

Label(F_pd_add, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
    font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)

engine = sqlalchemy.create_engine('mysql+pymysql://root:vyasa@localhost/hospital_management')
con = engine.connect()

frame = Frame(F_pd_add, bg="#2b2d42")
frame.place(x=400, y=225, width=1180, height=620)


Label(frame, fg="white",bg="#2b2d42", text="Patient ID", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
P_ID = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
P_ID.place(x=550, y=50, width=290, height=33)

Label(frame, fg="white",bg="#2b2d42", text="Patient Name", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=85)
name = Entry(frame, font=("cascadia code mono", 16, "bold"),
            bg="#2b2d42", fg="white", bd=5, justify='center')
name.place(x=550, y=85, width=290, height=33)

Label(frame, fg="white",bg="#2b2d42", text="sex", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=120)
sex = Entry(frame, font=("cascadia code mono", 16, "bold"),
            bg="#2b2d42", fg="white", bd=5, justify='center')
sex.place(x=550, y=120, width=290, height=33)

Label(frame, fg="white",bg="#2b2d42", text="age", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=155)
age = Entry(frame, font=("cascadia code mono", 16, "bold"),
            bg="#2b2d42", fg="white", bd=5, justify='center')
age.place(x=550, y=155, width=290, height=33)

Label(frame, fg="white",bg="#2b2d42", text="Address", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=190)
add = Entry(frame, font=("cascadia code mono", 16, "bold"),
            bg="#2b2d42", fg="white", bd=5, justify='center')
add.place(x=550, y=190, width=290, height=33)

Label(frame, fg="white",bg="#2b2d42", text="Phone Number", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=225)
ph = Entry(frame, font=("cascadia code mono", 16, "bold"),
            bg="#2b2d42", fg="white", bd=5, justify='center')
ph.place(x=550, y=225, width=290, height=33)


def clr_entry():
    P_ID.delete(0,'end')
    name.delete(0,'end')
    age.delete(0,'end')
    sex.delete(0,'end')
    add.delete(0,'end')
    ph.delete(0,'end')

def add_data():
    flag_validation = True  # set the flag
    ID = P_ID.get()  # read ID
    name_ = name.get()  # read ID
    sex_ = sex.get()    # read sex
    age_ = age.get()  # read age
    adr = add.get()   # read address
    cont = ph.get()  # read contact


    if (len(name_) < 2 or len(ID) < 1 or len(cont) > 10):
        flag_validation = False
    try:
        val = int(ID)
    except:
        flag_validation = False

    if (flag_validation):
        #            query = "INSERT INTO  `doctor_details` (`Doc_ID` ,`name` ,`specialisation` ,`age`,`address`,`contact`,`fees`,`monthly_salary`)  VALUES(ID, name_, spc, age_, adr, adr, cont, fee, sal)"
        #query = "INSERT INTO doctor_details('Doc_ID' ,'name' ,'specialisation' ,'age','address','contact','fees','monthly_salary')  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"  # insert data 
        query = f"INSERT INTO patient_details VALUES ({ID}, '{name_}', '{sex_}', {age_}, '{adr}', {cont})"
        # insert data 
        
        #data = (ID, name_, spc, age_, adr, cont, fee, sal)
        id = engine.execute(query)
        messagebox.showinfo("Success", "One record added successfully")

        swap(F_pdetails)
            
    else:
        l5.config(fg='red', bg='yellow')
        chk_str.set("Check inputs")


button_add = Button(frame, text="Add New Patient", font=("cascadia code", 18), command=lambda: [add_data(),clr_entry()], height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_add.place(x=700, y=500, width=250, height=53)

button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_pdetails), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=300, y=500, width=250, height=53)


# ======================================================================PATIENT DETAILS-Add ENDS=========================================================================================

def F_pd_all():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()

    x = con.execute("select * from patient_details")
    i = 1
    
    e = Label(frame, width=20, text='Patient_ID', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
#    e.grid_columnconfigure(0,weigh3t=1)

    e = Label(frame, width=20, text='Name', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
#    e.grid_columnconfigure(1,weight=2)

    e = Label(frame, width=20, text='sex', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
#    e.grid_columnconfigure(3,weight=1)

    e = Label(frame, width=20, text='age', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
#    e.grid_columnconfigure(4,weight=2)

    e = Label(frame, width=20, text='Address', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
#    e.grid_columnconfigure(5,weight=2)

    e = Label(frame, width=20, text='Ph. Num', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
#    e.grid_columnconfigure(7,weight=2)

    for doctors in x:
        for j in range(len(doctors)):
            e = Label(frame, width=20, text=doctors[j], borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor="w",bg="#2b2d42",fg="white")
            e.grid(row=i, column=j)
            # e.insert(END,students[j])
        i += 1

    button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Exit.place(x=400, y=510, width=390, height=53)
    root.mainloop()








def F_pd_id():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()
    con.execute("use hospital_management")

    Label(frame,bg="#2b2d42" ,fg="white", text="Patient ID", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    ent = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    ent.place(x=550, y=50, width=290, height=33)


    def dis_id():
        frame1 = Frame(frame,bd=5,bg="#2b2d42")
        frame1.place(x=0, y=0, width=1180, height=620)
        id = ent.get()

        if id == '' or id == ' ':
            messagebox.showinfo("Please enter an ID")
        else:
            query = f"select * from patient_details where Patient_ID = {id}"
            result = con.execute(query)
    
            e = Label(frame1, width=20, text='Patient_ID', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=0)
        #    e.grid_columnconfigure(0,weigh3t=1)

            e = Label(frame1, width=20, text='Name', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=1)
        #    e.grid_columnconfigure(1,weight=2)

            e = Label(frame1, width=20, text='sex', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=2)
        #    e.grid_columnconfigure(3,weight=1)

            e = Label(frame1, width=20, text='age', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=3)
        #    e.grid_columnconfigure(4,weight=2)

            e = Label(frame1, width=20, text='Address', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=4)
        #    e.grid_columnconfigure(5,weight=2)

            e = Label(frame1, width=20, text='Ph. Num', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=5)
        #    e.grid_columnconfigure(7,weight=2)

            rs = result.fetchone()
            try:
                i = 0
                for j in rs:
                    e = Label(frame1, width=20, text=j, borderwidth=3, font=(
                        "Cascadia Code", 13), relief='ridge', anchor='w',bg="#2b2d42",fg="white")
                    e.grid(row=1, column=i)
                    i+=1
                    
                button_Exit = Button(frame1, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
                button_Exit.place(x=400, y=510, width=390, height=53)

            except:
                messagebox.showerror("Error","No record found")




    button_Search = Button(frame, text="Search", command=lambda: dis_id(), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Search.place(x=600, y=510, width=350, height=53)

    button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                        bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Exit.place(x=200, y=510, width=350, height=53)
    root.mainloop()











def F_pd_sex():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()
    con.execute("use hospital_management")

    Label(frame, fg="white",bg="#2b2d42", text="Enter SEX", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    sex = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    sex.place(x=550, y=50, width=290, height=33)


    def dis_sex():
        frame1 = Frame(frame,bd=5,bg="#2b2d42")
        frame1.place(x=0, y=0, width=1180, height=620)
        sex_ = sex.get()

        query = f"select * from patient_details where sex = '{sex_}'"
        x = con.execute(query)
        i = 1
        
        e = Label(frame1, width=20, text='Patient_ID', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=0)
    #    e.grid_columnconfigure(0,weigh3t=1)

        e = Label(frame1, width=20, text='Name', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=1)
    #    e.grid_columnconfigure(1,weight=2)

        e = Label(frame1, width=20, text='sex', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=2)
    #    e.grid_columnconfigure(3,weight=1)

        e = Label(frame1, width=20, text='age', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=3)
    #    e.grid_columnconfigure(4,weight=2)

        e = Label(frame1, width=20, text='Address', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=4)
    #    e.grid_columnconfigure(5,weight=2)

        e = Label(frame1, width=20, text='Ph. Num', borderwidth=3, font=(
            "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
        e.grid(row=0, column=5)
    #    e.grid_columnconfigure(7,weight=2)

        x = x.fetchall()

        for doctors in x:
            for j in range(len(doctors)):
                e = Label(frame1,bg="#2b2d42",fg="white", width=20, text=doctors[j], borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor="w")
                e.grid(row=i, column=j)
            # e.insert(END,students[j])
            i += 1
        
        button_Exit = Button(frame1, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                            bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
        button_Exit.place(x=400, y=510, width=390, height=53)




    button_Search = Button(frame, text="Search", command=lambda: dis_sex(), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Search.place(x=600, y=510, width=350, height=53)

    button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                        bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Exit.place(x=200, y=510, width=350, height=53)
    root.mainloop()





def F_pd_age():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()
    con.execute("use hospital_management")

    Label(frame, fg="white",bg="#2b2d42", text="Enter AGE", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    age = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    age.place(x=550, y=50, width=290, height=33)


    def dis_sex():
        frame1 = Frame(frame,bd=5,bg="#2b2d42")
        frame1.place(x=0, y=0, width=1180, height=620)
        age_ = age.get()

        if age_ == '' or age_ == ' ':
            messagebox.showerror("Error","Enter the age!")

        else:
            query = f"select * from patient_details where age = {age_}"
            x = con.execute(query)
            i = 1
            
            e = Label(frame1, width=20, text='Patient_ID', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=0)
        #    e.grid_columnconfigure(0,weigh3t=1)

            e = Label(frame1, width=20, text='Name', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=1)
        #    e.grid_columnconfigure(1,weight=2)

            e = Label(frame1, width=20, text='sex', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=2)
        #    e.grid_columnconfigure(3,weight=1)

            e = Label(frame1, width=20, text='age', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=3)
        #    e.grid_columnconfigure(4,weight=2)

            e = Label(frame1, width=20, text='Address', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=4)
        #    e.grid_columnconfigure(5,weight=2)

            e = Label(frame1, width=20, text='Ph. Num', borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=5)
        #    e.grid_columnconfigure(7,weight=2)

            x = x.fetchall()
            try:
                for doctors in x:
                    for j in range(len(doctors)):
                        e = Label(frame1, width=20,bg="#2b2d42",fg="white", text=doctors[j], borderwidth=3, font=(
                            "Cascadia Code", 13), relief='ridge', anchor="w")
                        e.grid(row=i, column=j)
                    # e.insert(END,students[j])
                    i += 1
            except:
                messagebox.showerror("Error","No record with the age {age_}")                
            button_Exit = Button(frame1, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                                bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
            button_Exit.place(x=400, y=510, width=390, height=53)




    button_Search = Button(frame, text="Search", command=lambda: dis_sex(), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Search.place(x=600, y=510, width=350, height=53)

    button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_pd_dis), font=("cascadia code", 18), height=3, width=13,
                        bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Exit.place(x=200, y=510, width=350, height=53)
    root.mainloop()










# ======================================================================PATIENT DETAILS-DISPLAY=========================================================================================

F_pd_dis = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pd_dis.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_pd_dis, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pd_dis, bd=5, relief=RIDGE, text="ADMINISTRATION",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_pd_dis, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="DISPLAY PATIENT DETAILS")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(lblfrm, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)




button_Display_all = Button(lblfrm, text="DISPLAY ALL PATEINTS", font=("cascadia code", 16), command=lambda: F_pd_all(), height=3,
                            width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_all.place(x=250, y=100, width=280, height=80)

button_Display_pid = Button(lblfrm, text="DISPLAY BY PATIENT ID", font=("cascadia code", 16), command=lambda: F_pd_id(), height=3,
                            width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_pid.place(x=630, y=100, width=280, height=80)

button_Display_sex = Button(lblfrm, text="DISPLAY BY SEX", command=lambda: F_pd_sex(), font=("cascadia code", 16), height=3, width=13,
                            bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_sex.place(x=250, y=250, width=280, height=80)


button_Display_age = Button(lblfrm, text="DISPLAY BY AGE", font=("cascadia code", 16), height=3, width=13, command=lambda: F_pd_age(),
                            bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_age.place(x=630, y=250, width=280, height=80)


button_exit = Button(lblfrm, text="Go Back", font=("cascadia code", 16), height=3, width=13, command=lambda: swap(F_pdetails),
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_exit.place(x=430, y=450, width=280, height=80)

# ======================================================================PATIENT DETAILS-display ENDS=========================================================================================


# ================================================================PATIENT DETAILS===================================================================================

F_pdetails = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pdetails.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_pdetails, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pdetails, bd=5, relief=RIDGE, text="PATIENT DETAILS",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_pdetails, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=400, y=225, width=1180, height=620)

#l = Label(lblfrm, bg="Black", fg="white", text="PATIENT DETAILS", justify=CENTER, cursor="xterm").place(x=5, y=820)


Label(F_pdetails, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)


button_Display = Button(lblfrm, text="DISPLAY DETAILS", font=("cascadia code", 18), command=lambda: swap(F_pd_dis), height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=250, y=150, width=280, height=103)

button_Add_member = Button(lblfrm, text="ADD NEW PATIENT", font=("cascadia code", 18), command=lambda: swap(F_pd_add), height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=630, y=150, width=280, height=103)

button_Discharge = Button(lblfrm, text="DISCHARGE", command=lambda: swap(F_pd_del), font=("cascadia code", 18), height=3, width=13,
                          bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Discharge.place(x=250, y=350, width=280, height=103)

button_Exit = Button(lblfrm, text="Go Back", font=("cascadia code", 18), height=3, width=13, command=lambda: swap(F_Home),
                        bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=630, y=350, width=280, height=103)


# ================================================================PATIENT DETAILS PAGE ENDS===================================================================================




def del_doc():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=235, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()
    con.execute("use hospital_management")

    Label(frame,bg="#2b2d42", fg="white", text="Doctor ID", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    Doc_ID = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    Doc_ID.place(x=550, y=50, width=290, height=33)


    def del_data():
        flag_validation = True  # set the flag
        ID = Doc_ID.get()  # read ID

        if (len(ID) < 1):
            flag_validation = False
        try:
            val = int(ID)
        except:
            flag_validation = False

        if (flag_validation):

            query = f"DELETE FROM doctor_details WHERE Doc_ID ={ID}"
            
            id = engine.execute(query)
            messagebox.showinfo("Success", "One record deleted successfully")

            swap(F_adm_del)
                
        else:
            l5.config(fg='red', bg='yellow')
            chk_str.set("Check inputs")

    def conf_del():
        frame1 = Frame(frame,bd=5, bg="#2b2d42") 
        frame1.place(x=0,y=150,width=1180,height=200)

        id = Doc_ID.get()

        if id == '' or id == ' ':
            messagebox.showerror("Error","Please Enter an ID to continue")
        else:
            result = con.execute(f"SELECT * FROM doctor_details WHERE Doc_ID='{id}'")


            try:
                e = Label(frame1, width=14, text='Doc_ID', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=0)
            #    e.grid_columnconfigure(0,weigh3t=1)

                e = Label(frame1, width=14, text='Name', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=1)
            #    e.grid_columnconfigure(1,weight=2)

                e = Label(frame1, width=14, text='Dept', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=2)
            #    e.grid_columnconfigure(2,weight=3)

                e = Label(frame1, width=14, text='age', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=3)
            #    e.grid_columnconfigure(3,weight=1)

                e = Label(frame1, width=14, text='Address', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=4)
            #    e.grid_columnconfigure(4,weight=2)

                e = Label(frame1, width=14, text='Ph. Num', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=5)
            #    e.grid_columnconfigure(5,weight=2)

                e = Label(frame1, width=14, text='fee', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=6)
            #    e.grid_columnconfigure(6,weight=1)

                e = Label(frame1, width=14, text='monthly sal', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg='#2b2d42')
                e.grid(row=0, column=7)

                rs = result.fetchone()
                i = 0
                for j in rs:
                    e = Label(frame1, width=14, text=j, borderwidth=3, font=(
                        "Cascadia Code", 13), relief='ridge', anchor='w', bg='#2b2d42',fg="white")
                    e.grid(row=1, column=i)
                    i+=1
            
                button_del = Button(frame, text="Confirm Delete", command=lambda: del_data(), height=3, width=13, bd=7,
                                    bg="#242424", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
                button_del.place(x=800, y=500, width=130, height=53)
            except:
                messagebox.showerror("Error","No record found")


    button_del = Button(frame, text="Search", command=lambda: conf_del(), height=3, width=13, bd=7,
                        bg="black", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_del.place(x=600, y=500, width=130, height=53)

    button_add = Button(frame, text="Go Back", command=lambda: swap(F_adm_del), height=3, width=13, bd=7,
                        bg="black", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_add.place(x=400, y=500, width=130, height=53)









def del_nurse():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()
    con.execute("use hospital_management")

    Label(frame, fg="white",bg="#2b2d42", text="NURSE ID", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    Doc_ID = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    Doc_ID.place(x=550, y=50, width=290, height=33)


    def del_data():
        flag_validation = True  # set the flag
        ID = Doc_ID.get()  # read ID

        if (len(ID) < 1):
            flag_validation = False
        try:
            val = int(ID)
        except:
            flag_validation = False

        if (flag_validation):

            query = f"DELETE FROM nurse_details WHERE Nurse_ID ={ID}"
            
            id = engine.execute(query)
            messagebox.showinfo("Success", "One record deleted successfully")

            swap(F_adm_del)
                
        else:
            l5.config(fg='red', bg='yellow')
            chk_str.set("Check inputs")

    def conf_del():
        frame1 = Frame(frame,bd=5, bg="#2b2d42") 
        frame1.place(x=0,y=150,width=1180,height=200)

        id = Doc_ID.get()


        if id == '' or id == ' ':
            messagebox.showerror("Error","Please Enter an ID to continue")
        else:
            result = con.execute(f"SELECT * FROM nurse_details WHERE Nurse_ID='{id}'")

            try:
                e = Label(frame1, width=20, text='Nurse_ID', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
                e.grid(row=0, column=0)
            #    e.grid_columnconfigure(0,weigh3t=1)

                e = Label(frame1, width=20, text='Name', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
                e.grid(row=0, column=1)
            #    e.grid_columnconfigure(1,weight=2)

                e = Label(frame1, width=20, text='age', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
                e.grid(row=0, column=2)
            #    e.grid_columnconfigure(3,weight=1)

                e = Label(frame1, width=20, text='Address', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
                e.grid(row=0, column=3)
            #    e.grid_columnconfigure(4,weight=2)

                e = Label(frame1, width=20, text='Ph. Num', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
                e.grid(row=0, column=4)
            #    e.grid_columnconfigure(5,weight=2)

                e = Label(frame1, width=20, text='monthly sal', borderwidth=3, font=(
                    "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
                e.grid(row=0, column=5)

                rs = result.fetchone()
                i = 0
                for j in rs:
                    e = Label(frame1, width=20, text=j, borderwidth=3, font=(
                        "Cascadia Code", 13), relief='ridge', anchor='w')
                    e.grid(row=1, column=i)
                    i+=1
            
                button_del = Button(frame, text="Confirm Delete", command=lambda: del_data(), height=3, width=13, bd=7,
                                    bg="#242424", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
                button_del.place(x=800, y=500, width=130, height=53)

            except:
                messagebox.showerror("Error","No record found")
            

    


    button_del = Button(frame, text="Search", command=lambda: conf_del(), height=3, width=13, bd=7,
                        bg="black", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_del.place(x=600, y=500, width=130, height=53)

    button_add = Button(frame, text="Go Back", command=lambda: swap(F_adm_del), height=3, width=13, bd=7,
                        bg="black", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_add.place(x=400, y=500, width=130, height=53)











# ======================================================================ADMINISTRATION-Delete=========================================================================================

F_adm_del = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm_del.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_adm_del, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm_del, bd=5, relief=RIDGE, text="Administration - Delete",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm_del, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration - Delete")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(F_adm_del, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)


button_Display = Button(lblfrm, text="Delete  Doctor", font=("cascadia code", 18), command=lambda: del_doc(), height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=400, y=150, width=390, height=53)

button_Add_member = Button(lblfrm, text="Delete  Nurse", font=("cascadia code", 18), command=lambda: del_nurse(), height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=400, y=250, width=390, height=53)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=400, y=350, width=390, height=53)


# ======================================================================ADMINISTRATION-Delete ENDS=========================================================================================


def add_doc():
    frame = Frame(root,bd=8, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()


    Label(frame, bg="#2b2d42", fg="white", text="Doctor ID", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    Doc_ID = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    Doc_ID.place(x=550, y=50, width=290, height=33)

    Label(frame, bg="#2b2d42", fg="white", text="Doctor Name", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=85)
    name = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    name.place(x=550, y=85, width=290, height=33)

    Label(frame, bg="#2b2d42", fg="white", text="spc", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=120)
    spec = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    spec.place(x=550, y=120, width=290, height=33)

    Label(frame, bg="#2b2d42", fg="white", text="age", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=155)
    age = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    age.place(x=550, y=155, width=290, height=33)

    Label(frame,  bg="#2b2d42",fg="white", text="Address", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=190)
    add = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    add.place(x=550, y=190, width=290, height=33)

    Label(frame, bg="#2b2d42", fg="white", text="Phone Number", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=225)
    ph = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    ph.place(x=550, y=225, width=290, height=33)

    Label(frame, bg="#2b2d42", fg="white", text="Fees", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=260)
    fees = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    fees.place(x=550, y=260, width=290, height=33)

    Label(frame, bg="#2b2d42", fg="white", text="Monthly salary", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=295)
    ms = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    ms.place(x=550, y=295, width=290, height=33)

    
    def add_data():
        flag_validation = True  # set the flag
        ID = Doc_ID.get()  # read ID
        name_ = name.get()  # read ID
        spc = spec.get()    # read spc
        age_ = age.get()  # read age
        adr = add.get()   # read address
        cont = ph.get()  # read contact
        fee = fees.get()   # read fee
        sal = ms.get()   # read monthly sal

        if (len(name_) < 2 or len(ID) < 1 or len(cont) > 10):
            flag_validation = False
        try:
            val = int(ID)
        except:
            flag_validation = False

        if (flag_validation):
            #            query = "INSERT INTO  `doctor_details` (`Doc_ID` ,`name` ,`specialisation` ,`age`,`address`,`contact`,`fees`,`monthly_salary`)  VALUES(ID, name_, spc, age_, adr, adr, cont, fee, sal)"
            #query = "INSERT INTO doctor_details('Doc_ID' ,'name' ,'specialisation' ,'age','address','contact','fees','monthly_salary')  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"  # insert data 
            query = f"INSERT INTO doctor_details VALUES ({ID}, '{name_}', '{spc}', {age_}, '{adr}', {cont}, {fee}, {sal})"
            # insert data 
            
            #data = (ID, name_, spc, age_, adr, cont, fee, sal)
            id = engine.execute(query)
            messagebox.showinfo("Success", "One record added successfully")

            swap(F_adm_add)
                

    button_add = Button(frame, text="Add record", command=lambda: add_data(), height=3, width=13, bd=7,
                        bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_add.place(x=700, y=500, width=130, height=53)

    button_exit = Button(frame, text="Go Back", command=lambda: swap(F_adm_add), height=3, width=13, bd=7,
                        bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_exit.place(x=500, y=500, width=130, height=53)









def add_nurse():
    frame = Frame(root,bd=8, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()

    Label(frame, fg="white",bg="#2b2d42", text="Nurse ID", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=50)
    Doc_ID = Entry(frame, font=("cascadia code mono", 16, "bold"),
                    bg="#2b2d42", fg="white", bd=5, justify='center')
    Doc_ID.place(x=550, y=50, width=290, height=33)

    Label(frame, fg="white",bg="#2b2d42", text="Nurse Name", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=85)
    name = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    name.place(x=550, y=85, width=290, height=33)

    Label(frame, fg="white",bg="#2b2d42", text="age", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=120)
    age = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    age.place(x=550, y=120, width=290, height=33)

    Label(frame, fg="white",bg="#2b2d42", text="Address", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=155)
    add = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    add.place(x=550, y=155, width=290, height=33)

    Label(frame, fg="white",bg="#2b2d42", text="Phone Number", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=190)
    ph = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    ph.place(x=550, y=190, width=290, height=33)

    Label(frame, fg="white",bg="#2b2d42", text="Monthly salary", font=(
        "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=225)
    ms = Entry(frame, font=("cascadia code mono", 16, "bold"),
                bg="#2b2d42", fg="white", bd=5, justify='center')
    ms.place(x=550, y=225, width=290, height=33)


    def add_data():
        flag_validation = True  # set the flag
        ID = Doc_ID.get()  # read ID
        name_ = name.get()  # read ID
        age_ = age.get()  # read age
        adr = add.get()   # read address
        cont = ph.get()  # read contact
        sal = ms.get()   # read monthly sal

        if (len(name_) < 2 or len(ID) < 1 or len(cont) > 10):
            flag_validation = False
        try:
            val = int(ID)
        except:
            flag_validation = False

        if (flag_validation):
            #            query = "INSERT INTO  `doctor_details` (`Doc_ID` ,`name` ,`specialisation` ,`age`,`address`,`contact`,`fees`,`monthly_salary`)  VALUES(ID, name_, spc, age_, adr, adr, cont, fee, sal)"
            #query = "INSERT INTO doctor_details('Doc_ID' ,'name' ,'specialisation' ,'age','address','contact','fees','monthly_salary')  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"  # insert data 
            query = f"INSERT INTO nurse_details VALUES ({ID}, '{name_}', {age_}, '{adr}','{cont}', {sal})"
            # insert data 
            
            #data = (ID, name_, spc, age_, adr, cont, fee, sal)
            id = engine.execute(query)
            messagebox.showinfo("Success", "One record added successfully")

            swap(F_adm_add)
                

    button_add = Button(frame, text="Add record", command=lambda: add_data(), height=3, width=13, bd=7,
                        bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_add.place(x=700, y=500, width=130, height=53)

    button_exit = Button(frame, text="Go Back", command=lambda: swap(F_adm_add), height=3, width=13, bd=7,
                        bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_exit.place(x=500, y=500, width=130, height=53)






# ======================================================================ADMINISTRATION-Add=========================================================================================

F_adm_add = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm_add.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_adm_add, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm_add, bd=5, relief=RIDGE, text="Add New - ADMINISTRATION",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm_add, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Add New - Administration")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(F_adm_add, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)


button_Display = Button(lblfrm, text="Add New Doctor", font=("cascadia code", 18), command=lambda: add_doc(), height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=400, y=150, width=390, height=53)

button_Add_member = Button(lblfrm, text="Add New Nurse", font=("cascadia code", 18), command=lambda: add_nurse(), height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=400, y=250, width=390, height=53)


button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=400, y=350, width=390, height=53)


# ======================================================================ADMINISTRATION-Add ENDS=========================================================================================


def doctordetails():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1185, height=650)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()
    

    x = con.execute("select * from doctor_details")
    i = 1
    e = Label(frame, width=14, text='Doc_ID', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=0)
#    e.grid_columnconfigure(0,weigh3t=1)

    e = Label(frame, width=14, text='Name', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=1)
#    e.grid_columnconfigure(1,weight=2)

    e = Label(frame, width=14, text='Dept', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=2)
#    e.grid_columnconfigure(2,weight=3)

    e = Label(frame, width=14, text='age', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=3)
#    e.grid_columnconfigure(3,weight=1)

    e = Label(frame, width=14, text='Address', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=4)
#    e.grid_columnconfigure(4,weight=2)

    e = Label(frame, width=14, text='Ph. Num', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=5)
#    e.grid_columnconfigure(5,weight=2)

    e = Label(frame, width=14, text='fee', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=6)
#    e.grid_columnconfigure(6,weight=1)

    e = Label(frame, width=14, text='monthly sal', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=7)
#    e.grid_columnconfigure(7,weight=2)

    for doctors in x:
        for j in range(len(doctors)):
            e = Label(frame, width=14, text=doctors[j], borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor="w",fg="white",bg="#2b2d42")
            e.grid(row=i, column=j)
           # e.insert(END,students[j])
        i += 1


    
    button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_adm_dis), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Exit.place(x=400, y=600, width=390, height=53)

    root.mainloop()




def nursedetails():
    frame = Frame(root, bg="#2b2d42")
    frame.place(x=400, y=225, width=1180, height=620)

    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:vyasa@localhost/hospital_management')
    con = engine.connect()

    x = con.execute("select * from nurse_details")
    i = 1
    
    e = Label(frame, width=20, text='Nurse_ID', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=0)
#    e.grid_columnconfigure(0,weigh3t=1)

    e = Label(frame, width=20, text='Name', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=1)
#    e.grid_columnconfigure(1,weight=2)

    e = Label(frame, width=20, text='age', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=2)
#    e.grid_columnconfigure(3,weight=1)

    e = Label(frame, width=20, text='Address', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=3)
#    e.grid_columnconfigure(4,weight=2)

    e = Label(frame, width=20, text='Ph. Num', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=4)
#    e.grid_columnconfigure(5,weight=2)

    e = Label(frame, width=20, text='monthly sal', borderwidth=3, font=(
        "Cascadia Code", 13), relief='ridge', anchor='w', bg='yellow',fg="#2b2d42")
    e.grid(row=0, column=5)
#    e.grid_columnconfigure(7,weight=2)

    for nurse in x:
        for j in range(len(nurse)):
            e = Label(frame, width=20, text=nurse[j], borderwidth=3, font=(
                "Cascadia Code", 13), relief='ridge', anchor="w",bg="#2b2d42",fg="white")
            e.grid(row=i, column=j)
           # e.insert(END,students[j])
        i += 1

    button_Exit = Button(frame, text="Go Back", command=lambda: swap(F_adm_dis), font=("cascadia code", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
    button_Exit.place(x=400, y=560, width=390, height=53)
    root.mainloop()


# ======================================================================ADMINISTRATION-DISPLAY=========================================================================================
F_adm_dis = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm_dis.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_adm_dis, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm_dis, bd=5, relief=RIDGE, text="ADMINISTRATION",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm_dis, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(F_adm_dis, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)




button_Display = Button(lblfrm, text="Display Doctor Details", font=("cascadia code", 18), command=lambda: doctordetails(), height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=400, y=150, width=390, height=53)

button_Add_member = Button(lblfrm, text="Display Nurse Details", font=("cascadia code", 18), command=lambda: nursedetails(), height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=400, y=250, width=390, height=53)


button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=400, y=350, width=390, height=53)


# ======================================================================ADMINISTRATION-display ENDS=========================================================================================


# ======================================================================ADMINISTRATION=========================================================================================

F_adm = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_adm, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm, bd=5, relief=RIDGE, text="ADMINISTRATION",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(F_adm, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)


button_Display = Button(lblfrm, text="DISPLAY DETAILS", font=("cascadia code", 16), command=lambda: swap(F_adm_dis), height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=250, y=150, width=280, height=103)

button_Add_member = Button(lblfrm, text="ADD NEW MEMBER", font=("cascadia code", 16), command=lambda: swap(F_adm_add), height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=630, y=150, width=280, height=103)

button_Delete_member = Button(lblfrm, text="DELETE A MEMBER", command=lambda: swap(F_adm_del), font=("cascadia code", 16), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=250, y=350, width=280, height=103)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_Home), font=("cascadia code", 16), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=630, y=350, width=280, height=103)


# ======================================================================ADMINISTRATION ENDS=========================================================================================


# ================================================================HOME PAGE===================================================================================

F_Home = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_Home.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_Home, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_Home, bd=5, relief=RIDGE, text="HOME PAGE",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_Home, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(F_Home, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)


def close_tkinter():
    root.destroy()


button_Administration = Button(lblfrm, text="Administration", command=lambda: swap(F_adm), font=("cascadia code", 19), height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Administration.place(x=400, y=150, width=390, height=53)

button_PatientDetails = Button(lblfrm, text="Patient Details", command=lambda: swap(F_pdetails), font=("cascadia code", 19),  height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_PatientDetails.place(x=400, y=250, width=390, height=53)

button_Exit = Button(lblfrm, text="Exit",  font=("cascadia code", 19), height=3, width=13, command=lambda: close_tkinter(),
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=400, y=350, width=390, height=53)

# ======================================================================HOME PAGE ENDS=========================================================================================


# ================================================================LOGIN PAGE=========================================================================


F_login = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_login.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_login, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_login, bd=5, relief=RIDGE, text="LOGIN",
                      fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


global entry1
global entry2


lblfrm = LabelFrame(F_login, bd=8, relief=RIDGE, padx=10, fg="white", bg="#2b2d42", font=(
    "akrobat black", 16, "bold", "underline",), text="Login to your mysql Database")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(lblfrm, bg="#2b2d42", fg="white", text="USERNAME", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=180)
entry1 = Entry(lblfrm, font=("cascadia code mono", 16, "bold"),
               bg="#2b2d42", fg="white", bd=5, justify='center')
entry1.insert(0, "root")
entry1.place(x=550, y=180, width=290, height=33)

Label(lblfrm, bg="#2b2d42", fg="white", text="PASSWORD", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=280)
entry2 = Entry(lblfrm, font=("cascadia code mono", 16, "bold"),
               bg="#2b2d42", fg="white", bd=5, justify='center', show="*")
entry2.place(x=550, y=280, width=290, height=33)


def login():
    user = entry1.get()
    passw = entry2.get()

   # swap(F_Home)

    try:
        con = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=passw,
        )

        mycursor = con.cursor()
        mycursor.execute("create database if not exists hospital_management")
        mycursor.execute("use hospital_management")
        # creating the tables we need
        mycursor.execute("create table if not exists patient_details(Patient_ID int(7) Primary key,name varchar(30) NOT NULL, sex varchar(6) NOT NULL,age int(2) NOT NULL,address varchar(50) NOT NULL,contact bigint(12) NOT NULL)")
        mycursor.execute("create table if not exists doctor_details(Doc_ID int(4) primary key, name varchar(30) NOT NULL,specialisation varchar(40) NOT NULL,age int(2) NOT NULL,address varchar(30),contact bigint(12) NOT NULL,fees int(10) NOT NULL,monthly_salary int(10) NOT NULL)")
        mycursor.execute("create table if not exists nurse_details(Nurse_ID int(5) primary key,name varchar(30) NOT NULL,age int(2) NOT NULL,address varchar(30),contact bigint(15) NOT NULL,monthly_salary bigint(11) NOT NULL)")

        messagebox.showinfo("Success", "Welcome to Hospital Management")
        swap(F_Home)
    except:
        messagebox.showerror("error", "Inavlid Credentials")

    return mycursor


Label(F_login, bg="#212121", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=400, y=1000)


button_login = Button(lblfrm, text="login", command=lambda: login(), height=3, width=13, bd=7,
                      bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_login.place(x=500, y=390, width=130, height=53)

# ================================================================LOGIN PAGE ENDS HERE=======================================================================

root.mainloop()
