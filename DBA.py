import pyodbc

def Connection():
    connection = pyodbc.connect(r'Driver=SQL Server; Server=MASIRA\SQLEXPRESS; Database=SQL-Masira')
    cur=connection.cursor()
    return cur

def fetchData():
    cursor=Connection()
    cursor.execute("Select * from EMPLOYEE")
    rows=cursor.fetchall()
    return rows

def insertdata(x):
    cursor=Connection()
    cursor.execute(f"insert into EMPLOYEE (EmpId,EmpName,DOJ,Salary,DID,Age,Country,Contact) values({x.id},'{x.name}','{x.doj}',{x.sal},{x.did},{x.age},'{x.coun}',{x.con})")
    cursor.commit()
    
def deletedata(y):
    cursor=Connection()
    cursor.execute(f"delete from EMPLOYEE where EmpID = {y.id}")
    cursor.commit()
def updatedata(a,b,c):
    cursor=Connection()
    if type(b) == str:
        cursor.execute(f"update EMPLOYEE set {a} = '{b}' where EmpID = {c}")
    else:
        cursor.execute(f"update EMPLOYEE set {a} = {b} where EmpID = {c}")

    cursor.commit()






    
    
