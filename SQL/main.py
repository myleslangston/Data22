import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()  # cursor is a control structure, executes the call.

# ODBC = Open Data Base Connectivity
cursor.execute("SELECT @@version;")
row = cursor.fetchone()

# cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(cust_rows)

# rows = cursor.execute("SELECT * FROM Products;").fetchall()
#
# for record in rows:
#     print(record.UnitPrice)

rows = cursor.execute("SELECT * FROM Products")

while True:  # don't need to know size of database, it doesn't save all data from table like a for loop would.
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

