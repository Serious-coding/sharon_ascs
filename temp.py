# Insert data
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


def insert_salary():
    sal_id= int(input("Enter id of employee: "))
    Salary_amt=input("Enter name of employee: ")
    sql = "INSERT INTO salary (sal_id, Salary_amt) VALUES (%s, %s)"
    sal_id  =sal_id
    Salary_amt =  Salary_amt
    cursor.execute(sql, (sal_id, Salary_amt))
    db.commit()
        
#delete

def delete_dept():
    id_x = int(input('Enter id: '))
    sql = "DELETE FROM department_1 WHERE id = %s"
    id_x=id_x
    cursor.execute(sql, (id_x,))
    #cursor.execute(sql )
    db.commit()
    print(cursor.rowcount, "record(s) deleted")
    

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


#
