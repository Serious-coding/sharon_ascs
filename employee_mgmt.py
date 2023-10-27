import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
print("Press a : Enter into department module")
print("Press b : Enter into position module")
print("Press c : Enter into Employee module")
print("Press d : Enter into xyz module")
print("---------------------Press 1 : creating department table")
print("---------------------Press 2 : showing department table")
print("---------------------Press 3 : deleting department from table")
print("---------------------Press 4 : updating department table")
print("---------------------Press 5 : creating department table")
print("---------------------Press 6 : showing department table")
print("---------------------Press 7 : deleting department from table")
print("---------------------Press 8 : updating department table")
print("---------------------Press 9 : creating department table")
print("---------------------Press 10 : showing department table")
print("---------------------Press 11: deleting department from table")
print("---------------------Press 12: updating department table")
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

# Create tables
def create_tables_dept():
        cursor.execute("CREATE TABLE Department_1 (id char(3) PRIMARY KEY, name VARCHAR(255))")
        cursor.execute("CREATE TABLE Positions (id INT PRIMARY KEY, title VARCHAR(255))")
        cursor.execute("CREATE TABLE Employees (id INT  PRIMARY KEY, name VARCHAR(255),department_id INT, position_id INT, FOREIGN KEY (department_id) REFERENCES Departments(id),FOREIGN KEY (position_id) REFERENCES Positions(id))")
# Insert data
def insert_dept():
    id_x= int(input("Enter id of employee: "))
    name=int(input("Enter name of employee: "))
    sql = "INSERT INTO Department_1 (id, name) VALUES (%s, %s)"
    id_x= id_x
    name=name
    cursor.execute(sql, (id_x, name))
    db.commit()
        
#delete

def delete_dept():
    id_x = int(input('Enter id: '))
    sql = "DELETE FROM Department_1 WHERE id = %s"
    id_x=id_x
    cursor.execute(sql, (id_x,))
    #cursor.execute(sql )
    db.commit()
    print(cursor.rowcount, "record(s) deleted")

# Update data
def update_dept():
    id_x = int(input('Enter id: '))
    e_name=input('Enter name')
    sql = "UPDATE Department_1 SET name = %s and id=%s "
    e_name=e_name
    id_x=id_x
    cursor.execute(sql,(e_name, id_x))
    db.commit()
    print(cursor.rowcount, "record(s) affected")

# Retrieve data using lists, dictionaries, and dataframes
def select_dept():
    cursor.execute("SELECT * FROM Department_1")
    departments_data = cursor.fetchall()
    departments_list = [department[1] for department in departments_data]
    departments_dict = {department[0]: department[1] for department in departments_data}
    print("Departments List:", departments_list)
    print("Departments Dictionary:", departments_dict)

def main():
   while True:
        ch= input('Enter your choice: ')
        if ch == '1':
            create_tables_dept()
            
            print('Table created')
        elif ch == '2':
            select_dept()
            
        elif ch == '3':
            delete_dept()
          
        elif ch == '4':
            update_dept()
            
        else:
            print("Exit")
            break
main()

# Close the database connection
db.close()

