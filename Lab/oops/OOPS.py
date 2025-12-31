# object oriented programming


class EMP:
    college = "MIET"
    def __init__(self):
        self.eid = None
        self.__sal = None
        self.name = None

    def set_details(self, eid, name):
        self.eid = eid
        self.name = name
    def setsal(self,sal):
        if sal >= 10000:
            self.__sal = sal
        else:
            self.__sal = None
    def print_details(self):
        print(f"COLLEGE : {EMP.college} Eid : {self.eid}\tName : {self.name}\tSal : {self.sal}")
    @staticmethod
    def changecollege(new):
        EMP.college = new
    def __str__(self):
        print(f"Eid : {self.eid}")

e1 = EMP()
e1.set_details(1,"A")
e1.sal = 1000
e2 = EMP()
e2.set_details(2,"B")
e2.sal = 2000000
e1.print_details()
e2.print_details()

EMP.changecollege("XYZ")
e1.print_details()
e2.print_details()
