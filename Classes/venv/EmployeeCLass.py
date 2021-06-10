class Employee:
    def __init__(self, name, role, age, employeeid = 1, startdate = 0):
        self.name = name
        self.role = role
        self.__age = age
        self.__employeeid = employeeid
        self.__startdate = startdate


    def employ(self):
        print(self.__employeeid)

    def set_startdate(self, startdate):
        self.__startdate = startdate

    def get_startdate(self):
        print(self.__startdate)

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        print(self.__age)

    def set_employeeid(self, employeeid):
        self.__employeeid += employeeid

    def get_employeeid(self):
        print(self.__employeeid)


Andrew = Employee("Andrew", "CEO", 24, 1)

Andrew.set_age(28)
Andrew.get_age()

Andrew.set_startdate("12/02/2020")
Andrew.get_startdate()

Andrew.set_employeeid(1)
Andrew.get_employeeid()
Andrew.set_employeeid(1)
Andrew.get_employeeid()