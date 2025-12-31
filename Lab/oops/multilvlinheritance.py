class Employee:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name


class Manager(Employee):
    def __init__(self, eid, name, desig):
        super().__init__(eid,name)
        self.desig = desig


class Director(Manager):
    def __init__(self, eid, name, desig, area):
        super().__init__(eid,name,desig)
        self.area = area
    
    def __str__(self):
        return f'''
Eid : {self.eid}
Name : {self.name}
Desig = {self.desig}
Area : {self.area}'''
    
emp = Director(101,"Jack","Director","MIET")
print(emp)