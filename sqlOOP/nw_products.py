import pyodbc


class NwProducts:

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)  # basically just gets the table from sql into python. allows you to perform actions on the table.

    def print_all_product_records(self):
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        query_records = self._sql_query("SELECT * FROM Products")
        total_record = 0
        count = 0
        while True:
            record = query_records.fetchone()

            if record is None:
                break
            total_record += record.UnitPrice
            count += 1
        print(total_record / count)
