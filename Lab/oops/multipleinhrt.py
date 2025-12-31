class Employee:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name


class Devloper:
    def __init__(self, pl, workex):
        self.pl = pl
        self.workex = workex


class Manager(Employee, Devloper):
    def __init__(self, eid, name, pl, workex, desig):
        Employee.__init__(self, eid, name)
        Devloper.__init__(self, pl, workex)
        self.desig = desig


class Director(Manager):
    def __init__(self, eid, name, pl, workex, desig, area):
        Manager.__init__(self, eid, name, pl, workex, desig)
        self.area = area

    def __str__(self):
        return f"""
Eid : {self.eid}
Name : {self.name}
Lang : {self.pl}
Exp : {self.workex}
Desig = {self.desig}
Area : {self.area}"""


emp = Director(69, "Ankur", "C", 6996, "Guard", "MIET parking")
print(emp)