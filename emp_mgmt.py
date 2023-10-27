import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
print("Press a : Enter into department module")
print("Press b : Enter into position module")
print("Press c : Enter into Employee module")
print("Press d : Enter into xyz module")
print("---------------------Press 1 : INSERT into employee")
print("---------------------Press 2 : Show records of all employees")
print("---------------------Press 3 : Delete an employee")
print("---------------------Press 4 : update employee information")
print("---------------------Press 5 : INSERT into DEPARTMENT")
print("---------------------Press 2 : showing department table")
print("---------------------Press 3 : deleting department from table")
print("---------------------Press 4 : updating department table")
print("---------------------Press 5 :  INSERT into project ")
print("---------------------Press 6 : showing project table")
print("---------------------Press 7 : updating Project")
print("---------------------Press 8 : delete project")
print("---------------------Press 9 : INSERT into salary table")
print("---------------------Press 10 : showing salary  table")
print("---------------------Press 11: deleting salary  from table")
print("---------------------Press 12: updating salary  table")
print("---------------------Press B1 : BAR")
print("---------------------Press L1 : LINE")
print("---------------------Press B2 : BAR")
print("---------------------Press L2 : LINE")



# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_management"
)

# creation of cursor
cursor = db.cursor()
print("Connection created")


def insert_Employees():
    emp_id = int(input("Enter the ID of the Employee: "))
    name= input("Enter the name of employee: ")
    sql = "INSERT INTO Employees (emp_id, name) VALUES (%s, %s)"
    emp_id=emp_id
    name = name
    cursor.execute(sql, (emp_id, name))
    db.commit()

# Retrieve data using lists, dictionaries, and dataframes

def select_emp():
    cursor.execute("SELECT * FROM Employees")
    departments_data = cursor.fetchall()
    lst = list(departments_data)
    print('List: ',lst)
    '''departments_list = [department[1] for department in departments_data]
    departments_dict = {department[0]: department[1] for department in departments_data}
    print("Departments List:", departments_list)
    print("Departments Dictionary:\n\n")'''
    df=pd.DataFrame(lst, columns=['dept_id' ,'name'])
    print("Dataframe", df)

#delete employee

def delete_empl():
    id_x = int(input('Enter id of employee: '))
    sql = "DELETE FROM Employees WHERE emp_id = %s"
    id_x=id_x
    cursor.execute(sql, (id_x,))
    db.commit()
    print(cursor.rowcount, "record(s) deleted")
    
#delete dep

def delete_dept():
    id_x = int(input('Enter id: '))
    sql = "DELETE FROM department_1 WHERE id = %s"
    id_x=id_x
    cursor.execute(sql, (id_x,))
    #cursor.execute(sql )
    db.commit()
    print(cursor.rowcount, "record(s) deleted")
    


# Insert data
def insert_dept():
    dept_id= input("Enter id of employee's department: ")
    emp_id=int(input("Enter id of employee"))
    name=input("Enter name of employee: ")
    sql = "INSERT INTO department (dept_id, emp_id, name) VALUES (%s, %s,%s)"
    dept_id= dept_id
    emp_id=emp_id
    name=name
    cursor.execute(sql, (dept_id,emp_id,name))
    db.commit()
        




def insert_salary():
    sal_id= int(input("Enter salary id of employee: "))
    Salary_amt=int(input("Enter salary amount of employee: "))
    sql = "INSERT INTO salary (sal_id, Salary_amt) VALUES (%s, %s)"
    sal_id  =sal_id
    Salary_amt =  Salary_amt
    cursor.execute(sql, (sal_id, Salary_amt))
    db.commit()

# Create tables 
'''def create_tables():
    cursor.execute("CREATE TABLE Employees (emp_id INT  PRIMARY KEY, name VARCHAR(25)")
    cursor.execute("CREATE TABLE department (dept_id char(3) PRIMARY KEY, emp_id int, name VARCHAR(25),FOREIGN KEY (emp_id) REFERENCES Employees(emp_id) on delete cascade on update cascade)")
    cursor.execute("CREATE TABLE project (project_id char(3) PRIMARY KEY, name VARCHAR(25), emp_id int, FOREIGN KEY (emp_id) REFERENCES Employees(emp_id))''''''
    cursor.execute("CREATE TABLE salary ("sal_id char(3) primary key, name varchar(25), emp_id INT, FOREIGN KEY(emp_id) references"Employees(emp_id))")
'''


# Update data
def update_dept():
    
    id=input('Enter ID Of employee: ')
    #new_id=input('Enter new ID Of employee: ')
    name = input('Enter Name of employee')
    #new_name = input('Enter New Name of employee')
    query = "UPDATE department_1 SET name = %s WHERE id = %s"
    values = (name, id)
    cursor.execute(query, values)
    db.commit()
    print(cursor.rowcount, "record(s) affected")
    print("Employee details updated successfully!")

    
   

# Retrieve data using lists, dictionaries, and dataframes
def select_dept():
    cursor.execute("SELECT * FROM Department_1")
    departments_data = cursor.fetchall()

    lst = list(departments_data)
    print('List: ',lst)
    '''departments_list = [department[1] for department in departments_data]
    departments_dict = {department[0]: department[1] for department in departments_data}
    print("Departments List:", departments_list)
    print("Departments Dictionary:\n\n")'''
    df=pd.DataFrame(lst, columns=['dept_id','name'])
    print("Dataframe", df)


# Create tables
def create_tables_positions():
        cursor.execute("CREATE TABLE Department (id INT PRIMARY KEY, title VARCHAR(255))")
        cursor.execute("CREATE TABLE Employees (id INT  PRIMARY KEY, name VARCHAR(255),department_id INT, position_id INT, FOREIGN KEY (department_id) REFERENCES Departments(id),FOREIGN KEY (position_id) REFERENCES Positions(id))")
        
# Insert data
def insert_pos():
    id_x= int(input("Enter id of employee: "))
    title=input("Enter Position: ")
    sql = "INSERT INTO Positions (id, title) VALUES (%s, %s)"
    id_x= id_x
    title=title
    cursor.execute(sql, (id_x, title))
    db.commit()
        
#delete

def delete_pos():
    id_x = int(input('Enter id: '))
    sql = "DELETE FROM Positions WHERE id = %s"
    id_x=id_x
    title=title
    cursor.execute(sql, (id_x,))
    db.commit()
    print(cursor.rowcount, "record(s) deleted")

'''# Update data
def update_pos():
    id_pos = int(input('Enter id: '))
    title=input('Enter name')
    sql = "UPDATE Positions SET id=%s and name = %s "
    id=id_pos
    name=title
    cursor.execute(sql,(id, name))
    db.commit()
    print(cursor.rowcount, "record(s) affected")

# Retrieve data using lists, dictionaries, and dataframes
def select_pos():
    cursor.execute("SELECT * FROM Positions")
    departments_data = cursor.fetchall()
    departments_list = [department[1] for department in departments_data]
    departments_dict = {department[0]: department[1] for department in departments_data}
    print("Departments List:", departments_list)
    print("Departments Dictionary:", departments_dict)'''

    #_______________________________________________________

     

#delete

def delete_pos():
    id_pos = int(input('Enter position id: '))
    #title =input('Enter title of position: ')
    sql = "DELETE FROM Positions WHERE id = %s"
    id_pos=id_pos
    #title=title
    cursor.execute(sql, (id_pos, ))
    db.commit()
    print(cursor.rowcount, "record(s) deleted")

# Update data
def update_pos():
    id_pos = int(input('Enter id: '))
    pos =input('Enter title of position: ')
    sql = "UPDATE Positions SET id=%s and position = %s" 
    id=id_pos
    pos=pos
    cursor.execute(sql,(id, pos))
    db.commit()
    print(cursor.rowcount, "record(s) affected")

# Retrieve data using lists, dictionaries, and dataframes
def select_pos():
    cursor.execute("SELECT * FROM Positions")
    departments_data = cursor.fetchall()
    lst_pos = list(departments_data)
    print('List: ',lst_pos)
    '''departments_list = [department[1] for department in departments_data]'''
    departments_dict = {department[0]: department[1] for department in departments_data}
    print("Departments List:", lst_pos)
    print("Departments Dictionary:", departments_dict)
    df_pos=pd.DataFrame(lst_pos, columns=['Position_id', 'Designation'])
    print("Dataframe\n\n", df_pos)



def main():

   while True:
        ch= input('Enter your choice: ')
        if ch == '1':
           insert_Employees()
           print('Record inserted!')
        elif ch == '2':
            select_emp()
            
        elif ch == '3':
            delete_empl()
          
        elif ch == '4':
            update_dept()

        elif ch == '5':
            insert_dept()
            
            print('Inserted')
        elif ch == '6':
            select_pos()
            
        elif ch == '7':
            delete_pos()
          
        elif ch == '8':
            update_pos()
        elif ch == '9':
            create_tables_dept()
        else:
            print("Exit")
            break
main()

# Close the database connection
db.close()

