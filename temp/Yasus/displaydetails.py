#display details of doctors nurses and other
import mysql.connector
from tabulate import tabulate
mysql = mysql.connector.connect(host="localhost", user="root", passwd="yasus")
mycursor = mysql.cursor()
mycursor.execute("create database if not exists city_hospitals")
mycursor.execute("use city_hospitals")
# creating the tables we need
mycursor.execute("create table if not exists patient_detail(name varchar(30) primary key,sex varchar(15),age int(3),address varchar(50),contact varchar(15))")
mycursor.execute("create table if not exists doctor_details(name varchar(30) primary key,specialisation varchar(40),age int(2),address varchar(30),contact varchar(15),fees int(10),monthly_salary int(10))")
mycursor.execute("create table if not exists nurse_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")
mycursor.execute("create table if not exists other_workers_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")

# creating table for storing the username and password of the user
mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")


'''the above 15 lines are temporary'''


def doctordetails():
    mycursor.execute("select * from doctor_details")
    row = mycursor.fetchall()
    for i in row:
        b = 0
        v = list(i)
        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "FEES","MONTHLY_SALARY"]
        d = dict(zip(k, v))
        data = [(k, v) for k, v in d.items()]
        print(tabulate(data))
def nursedetails():
    mycursor.execute("select * from nurse_details")
    row = mycursor.fetchall()
    for i in row:
        v = list(i)
        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "MONTHLY_SALARY"]
        d = dict(zip(k, v))
        data = [(k, v) for k, v in d.items()]
        print(tabulate(data))
def otherdetails():
    mycursor.execute("select * from other_workers_details")
    row = mycursor.fetchall()
    for i in row:
        v = list(i)
        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "MONTHLY_SALARY"]
        d = dict(zip(k, v))
        data = [(k, v) for k, v in d.items()]
        print(tabulate(data))


        
#temporary main
print("""1. Display the details
         2. Add a new member
         3. Delete a member
         4. Make an exit """)

b = int(input("Enter your Choice:"))
if b == 1:
    while True:
        print("""
                1. Doctors Details
                2. Nurse Details
                3. Others
                4. exit
                                 """)

        c = int(input("Enter your Choice:"))
        if c == 1:
            doctordetails()
        elif c == 2:
            nursedetails()
        elif c == 3:
            otherdetails()
        else:
            break
            
