#Hari ideas
import mysql.connector
mysql = mysql.connector.connect(host="localhost", user="root", passwd="vyasa")
mycursor = mysql.cursor()
mycursor.execute("use city_hospitals")

def add_doc(n): #function for adding a doctor
    for i in range(n):
        #Asking details
        name=input("Enter doctor's name:  ")
        spec=input("Enter specialistaion:  ")
        age=input("Enter doctor's age:  ")
        add=input("Enter doctor's address:  ")
        cont=input("Enter doctor's phone number:  ")
        fees=input("Enter doctor's consultation fees:  ")
        ms=input("Enter doctors monthly salary: ")
        #Inserting values to table
        mycursor.execute("insert into doctor_details values('" + name + "','" + spec + "','" + age + "','" + add + "','" + cont + "','" + fees + "','" + ms + "')")
        mysql.commit()                                                                                                                                                  
        print("Record successfully added!.!.!")
        print(\
            \
            )
        
def add_nurse(k):
    for i in range(k):
        #Asking details
        name = input("Enter Nurse name:")
        age = input("Enter age:")
        add = input("Enter address:")
        cont = input("Enter Contact No:")
        ms = input("Enter Monthly Salary")
        #inserting values to table
        mycursor.execute("insert into nurse_details values('" + name + "','" + age + "','" + add + "','" + cont + "','" + ms + "')")
        mysql.commit()
        print("SUCCESSFULLY ADDED")
        print(\
            \
            )
def add_patient(num):
    for i in range(num):
        #Asking details
        name = input("Enter your name ")
        sex = input("Enter the gender: ")
        age = input("Enter age: ")
        address = input("Enter address: ")
        contact = input("Contact Details: ")
        #Inserting to tables
        mycursor.execute("insert into patient_detail values('" + name + "','" + sex + "','" +age + "','" + address + "','" + contact + "')")
        mysql.commit()
        mycursor.execute("select * from patient_detail")
        for i in mycursor:
            v = list(i)
            k = ['NAME', 'SEX', 'AGE', 'ADDRESS', 'CONTACT']
            print(dict(zip(k, v))) #Adding key(v):value(k) to dictionary
            print("""
                ====================================
                !!!!!!!Registered Successfully!!!!!!
                ====================================
                                """)
#For adding a new member
ch=int(input("Enter a choice: "))
if ch==1:
    n=int(input("Enter the number of records to add:  "))
    add_doc(n)
elif ch==2:
    k=int(input("Enter the number of records to add:  "))
    add_nurse(k)
elif ch==3:
    num=int(input("Enter the number of records to add:  "))
    add_patient(num)
    



                            
