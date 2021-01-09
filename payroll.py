import mysql.connector as m
import datetime  #to genrate the timestamp of the payslip"
from tabulate import tabulate
db=input("enter name of database:")
mydb=m.connect(host='localhost',user='root',password='12345')
mycursor=mydb.cursor()
sql=" create database if not exists %s " %(db,)
mycursor.execute(sql)
print("Your database has been created successfully...")
mycursor=mydb.cursor()
mycursor.execute("Use "+db)
tablename=input("name of the table to be created")
query="create table if not exists " + tablename + "(Empno int primary key, Name varchar(20) not null,Job varchar(20),Basicsalary int,DA float,HRA float,GrossSalary float,Tax float,NetSalary float)"
print("Table"+ tablename +" created successfully...")
mycursor.execute(query)
while True:
    print('\n\n\n')
    print("*"*90)
    print('\t\t\t\t\tMAIN MENU')
    print('*' * 90)
    print('\t\t\t\t1. Adding Employee Details')
    print('\t\t\t\t2. For Displaying Records of all the employees ')
    print('\t\t\t\t3. For Displaying Records of a particular employees ')
    print('\t\t\t\t4. For Deleting Records of all the employees ')
    print('\t\t\t\t5. For Deleting Records of a particular employees ')
    print('\t\t\t\t6. For Modifying a record ')
    print('\t\t\t\t7. For Displaying a Payroll ')
    print('\t\t\t\t8. For Displaying Salary Slips for all the Employees ')
    print('\t\t\t\t9. For Displaying Salary Slip of a particular employees ')
    print('\t\t\t\t10. For Exit')
    print('Enter Choice :',end='')
    choice=int(input())
    if choice==1:
        try:
            print("Enter employee Information :")
            mempno=int(input('Enter Employee Number'))
            mname=input("Enter Employee Name")
            mjob=input('Enter Employee Job.')
            mbasic=float(input('Enter basic Salary:'))
            if mjob.upper()=='OFFICER':
                mda=mbasic*0.5
                mhra=mbasic*0.35
                mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                mda=mbasic*0.45
                mhra=mbasic*0.30
                mtax=mbasic*0.15
            else:
                mda=mbasic*0.40
                mhra=mbasic*0.25
                mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            query="insert into " + tablename +" values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print("Records addd successfully..")
        except:
            print("Something went wrong..")
            
    elif choice==2:
        try:
            query='select *from '+tablename
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['Empno','Name','Job','Basic Salary','DA',"HRA",'Gross Salary','Tax','Net Salary'],tablefmt='psql'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)'''
        except:
            print("something went wrong...")

    elif choice==3:
        try:
            en=input("enter employee number of the record to be displayed...")
            query="select* from "+ tablename +" where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\n record of employe No:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print("Nothing to display")
        except:
            print('Something went wrong')

    elif choice==4:
        try:
            ch=input('Do you want to delete all the records (y/n)')
            if ch.upper()=='Y':
                mycursor.execute('delete from '+ tablename)
                mydb.commit()
                print('all the records are deleted...')
        except:
            print('Something went wrong')

    elif choice==5:
        try:
            en=input('Enter Employee number of the record to be deleted...')
            query='delete from ' +tablename+ ' where empno='+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print('Deletion Done')
            else:
                print('employee Number', en,' not found')
        except:
            print('Something went wrong')

    elif choice==6:
    
            en=input('Enter Employee number of the record to be modified...')
            query='select *from ' +tablename+ ' where empno='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('Employee number ' + en +'does not exsist')
            else:
                mname=myrecord[1]
                mjob=myrecord[2]
                mbasic=myrecord[3]
                print('empno :',myrecord[0])
                print('name :',myrecord[1])
                print('job :',myrecord[2])
                print('basic:',myrecord[3])
                print('da:',myrecord[4])
                print('hra :',myrecord[5])
                print('gross :',myrecord[6])
                print('tax :',myrecord[7])
                print('net :',myrecord[8])
                print('--------------------')
                print('Type value to modify or just press for no change')
                x=input('Enter Name')
                if len(x)>0:
                    mname=x
                x=input('Enter Job')
                if len(x)>0:
                    mjob=x
                x=input('Enter basic salary')
                if len(x)>0:
                    mbasic=float(x)
                query='update ' +tablename+ ' set name='+"'" +mname+ "'" +','+'job='+"'"+mjob+"'"+","+'basicsalary='+ (str(mbasic))+' where empno='+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print('Record Modified')
         
    elif choice==7:
        
            query='select *from ' +tablename
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print('*'*95)
            print('Employee Payroll'.center(90))
            print('*' * 95)
            now=datetime.datetime.now()
            print("Current Date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))  #this is stringfunction time
            print()
            print('-' *95)
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'%('Empno','Name','Job','Basic','DA',"HRA",'Gross','Tax','Net'))
            print(95*'-')
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
                print(95*'-')
    
    elif choice==8:
        try:
            query='select * from ' + tablename
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n")
            print("-"*95)
            print("\t\t\t\t Salary Slip")
            print("-"*95)
            print("Current date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            myrecords=mycursor.fetchall()
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
        except:
            print('Something went wrong')

    elif choice==9:
        try:
            en=input("Enter employee number whose pay slip you want to retreive:")
            query='select *from ' + tablename + ' where empno=' +en
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n\t\t\t\ SALARY SLIP")
            print("Current date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(tabulate(mycursor,headers=['EmpNo','Name','Job','Basic Salary','DA',"HRA",'Gross Salary','Tax','Net Salary'],tablefmt='psql'))
        except:
            print('Something went wrong')

    elif choice==10:
        break
    else:
        print("Wrong Choice...")
        
                
                
                      
                
            
        

                  
        
             



